#!/usr/bin/env python3
"""Build complete, static Card Explorer catalogs from the vendored CDBs.

No external checkout, runtime SQLite, image service, or network API is needed.
The first request loads only a format's metadata index. Full card descriptions
for search are optional; individual card details are fetched in small shards.
"""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import json
import re
import sqlite3
import unicodedata
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
ARCHETYPES = Path(__file__).with_name('card_archetypes.json')
SCHEMA_VERSION = 2
SHARD_SIZE = 128
LOCALES = {
    'de-DE': ('German', 'Deutsch'), 'en-US': ('English', 'English'),
    'es-ES': ('Spanish', 'Español'), 'fr-FR': ('French', 'Français'),
    'it-IT': ('Italian', 'Italiano'), 'ja-JP': ('Japanese', '日本語'),
    'ko-KR': ('Korean', '한국어'), 'pt-PT': ('Portuguese', 'Português'),
    'th-TH': ('Thai', 'ไทย'), 'zh-CN': ('Simplified Chinese', '简体中文'),
    'zh-TW': ('Traditional Chinese', '繁體中文'),
}
FORMATS = (('standard', 'Standard', 'cards.cdb', 'Scripts'),
           ('rush', 'Rush Duel', 'rush_cards.cdb', 'Rush/Scripts'))
# Values are from the vendored Utilities/constant.lua and Rush/Utilities/RDBase.lua,
# RDLegend.lua and RDMaximum.lua. English labels match the MDPro4 locale catalog.
TYPE_LABELS = (
    (0x1, 'Monster'), (0x2, 'Spell'), (0x4, 'Trap'), (0x10, 'Normal'),
    (0x20, 'Effect'), (0x40, 'Fusion'), (0x80, 'Ritual'), (0x100, 'Trap Monster'),
    (0x200, 'Spirit'), (0x400, 'Union'), (0x800, 'Gemini'), (0x1000, 'Tuner'),
    (0x2000, 'Synchro'), (0x4000, 'Token'), (0x10000, 'Quick-Play'),
    (0x20000, 'Continuous'), (0x40000, 'Equip'), (0x80000, 'Field'),
    (0x100000, 'Counter'), (0x200000, 'Flip'), (0x400000, 'Toon'),
    (0x800000, 'Xyz'), (0x1000000, 'Pendulum'), (0x2000000, 'Special Summon'),
    (0x4000000, 'Link'),
)
RUSH_TYPE_LABELS = TYPE_LABELS + ((0x8, 'Legend'), (0x8000, 'Maximum'))
RACE_NAMES = (
    'Warrior', 'Spellcaster', 'Fairy', 'Fiend', 'Zombie', 'Machine', 'Aqua',
    'Pyro', 'Rock', 'Winged Beast', 'Plant', 'Insect', 'Thunder', 'Dragon',
    'Beast', 'Beast-Warrior', 'Dinosaur', 'Fish', 'Sea Serpent', 'Reptile',
    'Psychic', 'Divine-Beast', 'Creator God', 'Wyrm', 'Cyberse', 'Illusion',
    'Magical Knight', 'High Dragon', 'Omega Psychic', 'Celestial Warrior',
    'Galaxy', 'Cyborg',
)
RACE_LABELS = tuple((1 << i, name) for i, name in enumerate(RACE_NAMES))
ATTRIBUTE_LABELS = tuple((1 << i, name) for i, name in enumerate(
    ('Earth', 'Water', 'Fire', 'Wind', 'Light', 'Dark', 'Divine')))
LINK_LABELS = ((0x40, 'Top-left'), (0x80, 'Top'), (0x100, 'Top-right'),
               (0x8, 'Left'), (0x20, 'Right'), (0x1, 'Bottom-left'),
               (0x2, 'Bottom'), (0x4, 'Bottom-right'))
# These labels are read from the supplied localized CDB snapshots. Matching all
# known languages permits partially translated sources without dropping text.
PENDULUM_LABELS = {
    'pendulum effect', 'pendeleffekt', 'efecto de péndulo', 'effet pendule',
    'effetto pendulum', '펜듈럼 효과', 'efeito de pêndulo', '靈擺效果',
}
MONSTER_LABELS = {
    'monster effect', 'flavor text', 'monstereffekt', 'efecto de monstruo',
    'effet de monstre', 'effetto di un mostro', 'モンスター効果', '몬스터 효과',
    'efeito de monstro', '怪兽效果', '怪兽描述', '怪獸效果', '怪獸敘述', '怪獸描述',
}
RUSH_LABELS = {}
for _kind, _labels in {
    'REQUIREMENT': ('requirement', 'bedingung', 'requisito', 'condition', '条件', '조건', '條件'),
    'EFFECT': ('effect', 'effekt', 'efecto', 'effet', 'effetto', '効果', '효과', 'efeito', '效果'),
    'CONTINUOUS EFFECT': ('continuous effect', 'permanenter effekt', 'dauereffekt',
        'efecto continuo', 'effet continu', 'effetto continuo', '永続効果', '지속 효과',
        'efeito contínuo', '永续效果', '永續效果'),
    'MULTI-CHOICE EFFECT': ('multi-choice effect', 'mehrfachauswahl-effekt',
        'efecto de opción múltiple', 'efecto de elección múltiple', 'effet multi-choix',
        'effetto a scelta', 'effetto scelta multipla', '選択効果', '선택 효과',
        'efeito de múltipla escolha', '选择效果', '選擇效果'),
}.items():
    RUSH_LABELS.update({label: _kind for label in _labels})
PACK_LINE = re.compile(r'^(?=[A-Za-z0-9/-]*/)(?=[A-Za-z0-9/-]*-)[A-Za-z0-9/-]+$')
MAXIMUM_LINE = re.compile(r'^(?:Maximum\s+ATK|极大攻击|極大攻擊)\s*[:=]?\s*([\d,]+)\s*$', re.I)


def heading_label(line: str) -> str:
    line = unicodedata.normalize('NFKC', line).strip()
    if len(line) > 1 and ((line[0] == '[' and line[-1] == ']') or (line[0] == '【' and line[-1] == '】')):
        return ' '.join(line[1:-1].lower().split())
    return ''


def is_pendulum_heading(line: str) -> bool:
    label = heading_label(line)
    return (label in PENDULUM_LABELS or label.startswith('pスケール:')
            or bool(re.fullmatch(r'←\d+\s*【灵摆】\s*\d+→', line.strip())))


def is_scale_or_divider(line: str) -> bool:
    normalized = unicodedata.normalize('NFKC', line).strip()
    return not normalized or bool(re.fullmatch(
        r'(?:[-━─]{3,}|(?:Pendulum Scale|Pendelbereich|Échelle Pendule|Valore Pendulum|Escala de Pêndulo)\s*=\s*\d+|←◊\d+ Escala \d+◊→)', normalized, re.I))


def normalize_search(value: str) -> str:
    """Lowercase and collapse whitespace; leave punctuation searchable."""
    return ' '.join(unicodedata.normalize('NFKC', value).lower().split())


def decode_mask(value: int, labels: tuple, bits: int = 32) -> list[str]:
    value &= (1 << bits) - 1
    result = [name for bit, name in labels if value & bit]
    known = 0
    for bit, _ in labels:
        known |= bit
    if value & ~known:
        result.append(f'Unknown ({hex(value & ~known)})')
    return result


def decode_setcodes(value: int, names: dict[int, str]) -> list[dict]:
    # SQLite stores these as signed int64; JavaScript must not receive this
    # packed value as a number because precision can be lost above 2**53.
    value &= (1 << 64) - 1
    seen: set[int] = set()
    result = []
    for shift in (0, 16, 32, 48):
        code = (value >> shift) & 0xffff
        if code and code not in seen:
            result.append({'code': hex(code), 'name': names.get(code)})
            seen.add(code)
    return result


def clean_block(lines: list[str]) -> str:
    # Display whitespace is cleaned, but originalText preserves the CDB exactly.
    return '\n'.join(line.rstrip() for line in lines).strip()


def split_description(original: str, card_type: int, format_id: str) -> dict:
    lines = original.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    result = {'originalText': original, 'pendulumText': '', 'effectText': '',
              'requirementText': '', 'preambleText': '', 'effectHeading': 'Effect',
              'maximumAttack': None, 'packCode': None}
    if format_id == 'rush':
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and PACK_LINE.fullmatch(lines[0].strip()):
            result['packCode'] = lines.pop(0).strip()
        while lines and not lines[0].strip():
            lines.pop(0)
        maximum = MAXIMUM_LINE.fullmatch(lines[0].strip()) if lines else None
        if maximum and card_type & 0x8000:
            result['maximumAttack'] = int(maximum[1].replace(',', ''))
            lines.pop(0)

    if card_type & 0x1000000:
        pend = next((i for i, line in enumerate(lines) if is_pendulum_heading(line)), None)
        monster = next((i for i, line in enumerate(lines) if heading_label(line) in MONSTER_LABELS), None)
        prefix_end = pend if pend is not None else monster
        metadata_prefix = prefix_end is not None and all(
            is_scale_or_divider(line)
            for line in lines[:prefix_end]
        )
        # Some real cards have no Pendulum effect: only a scale and divider
        # precede Monster Effect. Unknown or misordered headers must not cause
        # meaningful text to disappear from the readable view.
        if monster is not None and (metadata_prefix or pend is not None) and (pend is None or pend < monster):
            if pend is not None:
                prefix_text = clean_block([line for line in lines[:pend] if not is_scale_or_divider(line)])
                if prefix_text:
                    result['preambleText'] = prefix_text
            pend_lines = lines[pend + 1:monster] if pend is not None else []
            result['pendulumText'] = clean_block([line for line in pend_lines if not re.fullmatch(r'\s*[-━─]{3,}\s*', line)])
            result['effectText'] = clean_block(lines[monster + 1:])
            return result
        # If an unfamiliar CDB layout is encountered, retain the whole body
        # instead of silently discarding text based on assumed line numbers.

    if format_id == 'rush':
        headers = [(i, RUSH_LABELS[heading_label(line)]) for i, line in enumerate(lines) if heading_label(line) in RUSH_LABELS]
        if headers:
            result['preambleText'] = clean_block(lines[:headers[0][0]])
            for n, (start, label) in enumerate(headers):
                end = headers[n + 1][0] if n + 1 < len(headers) else len(lines)
                key = 'requirementText' if label == 'REQUIREMENT' else 'effectText'
                body = clean_block(lines[start + 1:end])
                # Preserve repeated sections, rather than overwrite their text.
                if result[key]:
                    result[key] += '\n\n[' + label + ']\n' + body
                else:
                    result[key] = body
                if key == 'effectText':
                    result['effectHeading'] = label.capitalize()
            return result
    result['effectText'] = clean_block(lines)
    return result


def script_path(card_id: int, alias: int, script_dir: Path, workspace: Path) -> str | None:
    for candidate in dict.fromkeys((card_id, alias)):
        if candidate:
            path = script_dir / f'c{candidate}.lua'
            if path.is_file():
                return path.relative_to(workspace).as_posix()
    return None


def read_cards(database: Path) -> list[sqlite3.Row]:
    # Immutable read avoids WAL/SHM writes to the vendored database on Windows.
    connection = sqlite3.connect(database.resolve().as_uri() + '?mode=ro&immutable=1', uri=True)
    connection.row_factory = sqlite3.Row
    try:
        columns = ['d.*', 't.name', 't.desc'] + [f't.str{i}' for i in range(1, 17)]
        # LEFT JOIN preserves every datas row even if a future snapshot omits text.
        return connection.execute(f'SELECT {",".join(columns)} FROM datas d LEFT JOIN texts t ON t.id=d.id ORDER BY d.id').fetchall()
    finally:
        connection.close()


def card_detail(row: sqlite3.Row | dict, format_id: str, source: str,
                names: dict[int, str], workspace: Path, script_dir: Path) -> dict:
    card_type = int(row['type'] or 0) & 0xffffffff
    level = int(row['level'] or 0) & 0xffffffff
    monster = bool(card_type & 0x1)
    link = bool(card_type & 0x4000000)
    setcodes = decode_setcodes(int(row['setcode'] or 0), names)
    archetypes = [item['name'] or f"Unknown ({item['code']})" for item in setcodes]
    alias = int(row['alias'] or 0)
    description = split_description(row['desc'] or '', card_type, format_id)
    detail = {
        'id': int(row['id']), 'name': row['name'] or f"Card {row['id']}",
        'format': format_id, 'source': source, 'alias': alias,
        'types': decode_mask(card_type, RUSH_TYPE_LABELS if format_id == 'rush' else TYPE_LABELS),
        'archetypes': archetypes, 'setcodes': setcodes,
        'attribute': ' / '.join(decode_mask(int(row['attribute'] or 0), ATTRIBUTE_LABELS)),
        'race': ' / '.join(decode_mask(int(row['race'] or 0), RACE_LABELS)),
        'level': (level & 0xff) if monster else None,
        'levelLabel': 'Link' if link else 'Rank' if card_type & 0x800000 else 'Level',
        'attack': int(row['atk'] or 0) if monster else None,
        'defense': int(row['def'] or 0) if monster and not link else None,
        'scales': {'left': (level >> 24) & 0xff, 'right': (level >> 16) & 0xff} if card_type & 0x1000000 else None,
        'linkMarkers': decode_mask(int(row['def'] or 0), LINK_LABELS) if link else [],
        'legend': format_id == 'rush' and bool(card_type & 0x8),
        'scriptPath': script_path(int(row['id']), alias, script_dir, workspace),
        'strings': [{'index': i - 1, 'text': row[f'str{i}']} for i in range(1, 17) if row[f'str{i}']],
        'raw': {'ot': int(row['ot'] or 0), 'setcode': hex(int(row['setcode'] or 0) & ((1 << 64) - 1)),
                'type': hex(card_type), 'race': hex(int(row['race'] or 0) & 0xffffffff),
                'attribute': hex(int(row['attribute'] or 0) & 0xffffffff),
                'category': hex(int(row['category'] or 0) & ((1 << 64) - 1)),
                'level': level, 'attack': int(row['atk'] or 0), 'defense': int(row['def'] or 0)},
        **description,
    }
    return detail


def write_json(path: Path, payload: object) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (json.dumps(payload, ensure_ascii=False, separators=(',', ':')) + '\n').encode('utf-8')
    path.write_bytes(content)
    return len(content)


def load_archetype_snapshots() -> dict:
    data = json.loads(ARCHETYPES.read_text(encoding='utf-8'))
    # Accept the initial English-only fixture while migrating an existing tree.
    return data.get('locales', {'en-US': data})


def import_archetype_snapshots(locales_dir: Path) -> dict:
    repository = locales_dir.resolve().parents[1]
    revision = subprocess.run(['git', '-c', f'safe.directory={repository.as_posix()}',
        '-C', str(repository), 'rev-parse', 'HEAD'], check=True, capture_output=True,
        text=True).stdout.strip()
    snapshots = {}
    for locale in LOCALES:
        source = locales_dir / locale / 'strings.conf'
        if not source.is_file():
            continue
        content = source.read_bytes()
        names = {hex(int(match[1], 16)): match[2].split('\t')[0].strip()
                 for match in re.finditer(r'^!setname\s+(0x[0-9a-fA-F]+)\s+(.+)$', content.decode('utf-8-sig'), re.M)}
        snapshots[locale] = {
            'source': f'MDPro4_Data/Data/locales/{locale}/strings.conf',
            'repository': 'https://github.com/ElderLich/MDPro4_Data', 'commit': revision,
            'sha256': hashlib.sha256(content).hexdigest(), 'names': names,
        }
    ARCHETYPES.write_text(json.dumps({'locales': snapshots}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    return snapshots


def write_locale_catalog(workspace: Path, output: Path, database_dir: Path,
                         locale: str, labels: dict) -> dict:
    names = {int(code, 16): name for code, name in labels['names'].items()}
    label, native_label = LOCALES[locale]
    locale_manifest = {'id': locale, 'label': label, 'nativeLabel': native_label,
                       'formats': [], 'archetypeSource': {key: value for key, value in labels.items() if key != 'names'}}
    for format_id, format_label, filename, script_folder in FORMATS:
        rows = read_cards(database_dir / filename)
        records, text_index, shard = [], {}, {}
        written_shards: set[Path] = set()
        for position, row in enumerate(rows):
            detail = card_detail(row, format_id, filename, names, workspace, workspace / script_folder)
            detail['locale'] = locale
            shard_name = f'{position // SHARD_SIZE:04d}.json'
            detail_path = f'{locale}/{format_id}/details/{shard_name}'
            index_fields = ('id', 'name', 'types', 'archetypes', 'attribute', 'race', 'level', 'levelLabel', 'attack', 'defense', 'legend')
            record = {key: detail[key] for key in index_fields}
            record['searchText'] = normalize_search(' '.join((str(detail['id']), detail['name'], *detail['archetypes'], *detail['types'], detail['attribute'], detail['race'])))
            record['detail'] = detail_path
            records.append(record)
            text_index[str(detail['id'])] = normalize_search(detail['originalText'])
            shard[str(detail['id'])] = detail
            if len(shard) == SHARD_SIZE or position == len(rows) - 1:
                destination = output / detail_path
                write_json(destination, shard)
                written_shards.add(destination)
                shard = {}
        for stale in (output / locale / format_id / 'details').glob('[0-9][0-9][0-9][0-9].json'):
            if stale not in written_shards:
                stale.unlink()
        index_path = f'{locale}/{format_id}/index.json'
        search_path = f'{locale}/{format_id}/search-text.json'
        index_bytes = write_json(output / index_path, {'schemaVersion': SCHEMA_VERSION, 'locale': locale, 'format': format_id, 'source': filename, 'cards': records})
        search_bytes = write_json(output / search_path, text_index)
        locale_manifest['formats'].append({
            'id': format_id, 'label': format_label, 'source': filename, 'count': len(rows),
            'index': index_path, 'searchText': search_path,
            'indexBytes': index_bytes, 'searchTextBytes': search_bytes,
            'detailShardCount': len(written_shards), 'detailShardSize': SHARD_SIZE,
            'sourceSha256': hashlib.sha256((database_dir / filename).read_bytes()).hexdigest(),
        })
    return locale_manifest


def validate_locale_snapshot(output: Path, locale: dict) -> None:
    """Offline generation must not advertise missing imported resources."""
    for format_data in locale['formats']:
        index_file = output / format_data['index']
        search_file = output / format_data['searchText']
        if not index_file.is_file() or not search_file.is_file():
            raise FileNotFoundError(f"Incomplete imported Card Explorer locale {locale['id']}; re-import localized CDBs")
        index = json.loads(index_file.read_text(encoding='utf-8'))
        if len(index['cards']) != format_data['count']:
            raise ValueError(f"Card Explorer index count mismatch for {locale['id']}/{format_data['id']}")
        for detail in {item['detail'] for item in index['cards']}:
            if not (output / detail).is_file():
                raise FileNotFoundError(f'Missing imported Card Explorer detail shard: {detail}')


def remove_legacy_catalog_paths(output: Path) -> None:
    # Schema 1 used standard/ and rush/ directly. Remove only the exact files
    # this generator owned, leaving unrelated files and directories untouched.
    for format_id, *_ in FORMATS:
        old = output / format_id
        for item in (old / 'details').glob('[0-9][0-9][0-9][0-9].json'):
            item.unlink()
        for name in ('index.json', 'search-text.json'):
            (old / name).unlink(missing_ok=True)
        for directory in (old / 'details', old):
            if directory.exists() and not any(directory.iterdir()):
                directory.rmdir()


def write_card_catalogs(workspace: Path = WORKSPACE, output: Path | None = None,
                        locales_dir: Path | None = None) -> dict:
    workspace = Path(workspace)
    output = Path(output) if output is not None else workspace / 'docs/public/data/cards'
    labels = import_archetype_snapshots(Path(locales_dir)) if locales_dir is not None else load_archetype_snapshots()
    manifest = {'schemaVersion': SCHEMA_VERSION, 'defaultLocale': 'en-US', 'locales': []}
    manifest_path = output / 'manifest.json'
    if locales_dir is None and manifest_path.exists():
        previous = json.loads(manifest_path.read_text(encoding='utf-8'))
        for locale in previous.get('locales', []):
            if locale['id'] != 'en-US':
                validate_locale_snapshot(output, locale)
                manifest['locales'].append(locale)
    if locales_dir is None:
        manifest['locales'].append(write_locale_catalog(workspace, output, workspace, 'en-US', labels['en-US']))
    else:
        for locale in LOCALES:
            directory = Path(locales_dir) / locale
            if not directory.is_dir():
                continue
            if locale not in labels:
                raise FileNotFoundError(f'Missing localized archetype names: {directory / "strings.conf"}')
            manifest['locales'].append(write_locale_catalog(workspace, output, directory, locale, labels[locale]))
    manifest['locales'].sort(key=lambda entry: (entry['id'] != 'en-US', entry['id']))
    write_json(manifest_path, manifest)
    remove_legacy_catalog_paths(output)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--locales-dir', type=Path, help='Import all localized MDPro4_Data CDBs into committed static snapshots. Normal site generation needs no external repository.')
    args = parser.parse_args()
    manifest = write_card_catalogs(locales_dir=args.locales_dir)
    for locale in manifest['locales']:
        for source in locale['formats']:
            print(f"Card Explorer: {locale['id']} {source['label']}: {source['count']:,} cards, {source['detailShardCount']} detail shards, {source['indexBytes']:,}-byte index")


if __name__ == '__main__':
    main()
