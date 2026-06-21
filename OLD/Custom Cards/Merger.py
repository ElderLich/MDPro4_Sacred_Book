import json
import os

TEXTS_FILE = "texts.json"
SCRIPTS_DIR = "script"  # make sure this is correct
OUTPUT_JSON = "merged_cards.json"
OUTPUT_SCRIPT_DIR = "scripts_out"

os.makedirs(OUTPUT_SCRIPT_DIR, exist_ok=True)

def load_texts(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def load_script(script_dir, card_id):
    filename = f"c{card_id}.lua"
    path = os.path.join(script_dir, filename)
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None

def save_script_file(card_id, script):
    filename = f"c{card_id}.lua"
    out_path = os.path.join(OUTPUT_SCRIPT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(script)
    return out_path

def extract_strings(card):
    return {
        f"str{n}": card[f"str{n}"]
        for n in range(1, 17)
        if card.get(f"str{n}")
    }

def build_card_entry(card, script_code):
    entry = {
        "id": card["id"],
        "name": card["name"],
        "desc": card["desc"],
        "strings": extract_strings(card)
    }
    if script_code:
        entry["script"] = script_code
        entry["script_path"] = save_script_file(card["id"], script_code)
    else:
        entry["script"] = ""
        entry["script_path"] = None
    return entry

def main():
    cards = load_texts(TEXTS_FILE)
    merged = []

    for card in cards:
        script_code = load_script(SCRIPTS_DIR, card["id"])
        entry = build_card_entry(card, script_code)
        merged.append(entry)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    print(f"✅ Done! {len(merged)} cards written to {OUTPUT_JSON}")
    print(f"📂 Scripts saved to: {OUTPUT_SCRIPT_DIR}/")

if __name__ == "__main__":
    main()
