import { defineConfig } from 'vitepress';

function renderSearchMarkdown(src: string, env: any, md: any) {
  const relativePath = String(env.relativePath || '').replace(/\\/g, '/');
  if (relativePath.startsWith('examples/cards/')) {
    return '';
  }
  if (relativePath.startsWith('api/functions/')) {
    src = src.split(/\n## Used By\n/)[0];
  }
  return md.render(src, env);
}

export default defineConfig({
  title: 'MDPro3 Sacred Book',
  description: 'MDPro3/YGOPro Lua card scripting lessons, examples, and API reference.',
  base: '/MDPro3_Sacred_Book/',
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Learn', link: '/learn/' },
      { text: 'API', link: '/api/' },
      { text: 'Examples', link: '/examples/' },
      { text: 'Tools', link: '/tools/script-explorer' },
      { text: 'Roadmap', link: '/roadmap' },
    ],
    sidebar: {
      '/learn/': [
        {
          text: 'Learning Path',
          items: [
            { text: 'Overview', link: '/learn/' },
            { text: 'Script Structure', link: '/learn/script-structure' },
            { text: 'Effect Object', link: '/learn/effect-object' },
            { text: 'Effect Types', link: '/learn/effect-types' },
            { text: 'Categories and Properties', link: '/learn/categories-properties-and-hints' },
            { text: 'Callbacks', link: '/learn/effect-callbacks' },
            { text: 'Activated Effects', link: '/learn/activated-effects' },
            { text: 'Activation Legality', link: '/learn/activation-legality' },
            { text: 'Spell Cards', link: '/learn/spell-card-patterns' },
            { text: 'Trap Cards', link: '/learn/trap-card-patterns' },
            { text: 'Ritual Procedure', link: '/learn/ritual-procedure' },
            { text: 'Fusion Procedure', link: '/learn/fusion-procedure' },
            { text: 'Synchro Procedure', link: '/learn/synchro-procedure' },
            { text: 'Xyz Procedure', link: '/learn/xyz-procedure' },
            { text: 'Link Procedure', link: '/learn/link-procedure' },
            { text: 'Pendulum Procedure', link: '/learn/pendulum-procedure' },
            { text: 'Special Summon-only Monsters', link: '/learn/special-summon-only-monsters' },
            { text: 'Gemini Monsters', link: '/learn/gemini-monsters' },
            { text: 'Toon Monsters', link: '/learn/toon-monsters' },
            { text: 'Union Monsters', link: '/learn/union-monsters' },
            { text: 'Spirit Monsters', link: '/learn/spirit-monsters' },
            { text: 'Tribute Summon Materials', link: '/learn/tribute-summon-materials' },
            { text: 'Counters', link: '/learn/counters' },
            { text: 'Filters and Groups', link: '/learn/filters-and-groups' },
            { text: 'Moving Cards', link: '/learn/moving-cards' },
            { text: 'Negation and Immunity', link: '/learn/negation-and-immunity' },
            { text: 'Control Change', link: '/learn/control-change' },
            { text: 'Battle Position Effects', link: '/learn/battle-position-effects' },
            { text: 'Field Zones', link: '/learn/field-zones-and-sequences' },
            { text: 'Field Spells', link: '/learn/field-spells' },
            { text: 'Targeting Flow', link: '/learn/targeting-flow' },
            { text: 'Effect Lifecycle', link: '/learn/cost-target-operation-lifecycle' },
            { text: 'Continuous Effects', link: '/learn/continuous-effects' },
            { text: 'Stat Modifiers', link: '/learn/continuous-stat-modifiers' },
            { text: 'Equip Spells', link: '/learn/equip-spells' },
            { text: 'LP and Damage', link: '/learn/lp-recovery-and-damage' },
            { text: 'Player-Targeted Effects', link: '/learn/player-targeted-effects' },
            { text: 'Player Restrictions', link: '/learn/player-restrictions' },
            { text: 'Draw, Hand, and Deck Effects', link: '/learn/draw-hand-and-deck-effects' },
            { text: 'Flag Effects', link: '/learn/flag-effects' },
            { text: 'Count Limits', link: '/learn/count-limits' },
            { text: 'Affecting Cards', link: '/learn/affecting-cards' },
            { text: 'Archetypes and Set Codes', link: '/learn/archetypes-and-setcodes' },
          ],
        },
      ],
      '/getting-started/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Overview', link: '/getting-started/' },
            { text: 'Setup', link: '/getting-started/setup' },
            { text: 'Your First Card', link: '/getting-started/first-card' },
            { text: 'Reading Card Scripts', link: '/getting-started/reading-scripts' },
          ],
        },
      ],
      '/guides/': [
        {
          text: 'Guides',
          items: [
            { text: 'Overview', link: '/guides/' },
            { text: 'Effect Anatomy', link: '/guides/effect-anatomy' },
            { text: 'Card Database', link: '/guides/card-database' },
            { text: 'Common Patterns', link: '/guides/common-patterns' },
          ],
        },
      ],
      '/tools/': [
        {
          text: 'Tools',
          items: [
            { text: 'Script Explorer', link: '/tools/script-explorer' },
            { text: 'Translation Review', link: '/tools/translation-review' },
            { text: 'Source Plan', link: '/tools/source-plan' },
            { text: 'Page Analysis', link: '/tools/page-analysis' },
          ],
        },
      ],
      '/api/functions/': [
        { text: 'Function Index', link: '/api/functions/' },
        {
          text: 'Namespaces',
          collapsed: false,
          items: [
              { text: "Auxiliary", link: '/api/functions/Auxiliary/' },
              { text: "bit", link: '/api/functions/bit/' },
              { text: "Card", link: '/api/functions/Card/' },
              { text: "Debug", link: '/api/functions/Debug/' },
              { text: "Duel", link: '/api/functions/Duel/' },
              { text: "Effect", link: '/api/functions/Effect/' },
              { text: "Global", link: '/api/functions/Global/' },
              { text: "Group", link: '/api/functions/Group/' },
          ],
        },
      ],
      '/api/': [
        { text: 'API Overview', link: '/api/' },
        { text: 'Functions', link: '/api/functions/' },
        { text: 'Constants', link: '/api/constants' },
      ],
      '/examples/': [
        {
          text: 'Examples',
          items: [
            { text: 'Overview', link: '/examples/' },
            { text: "Salamandra with Chain", link: '/examples/cards/62091148' },
            { text: "Astrograph Sorcerer, the Star Magician", link: '/examples/cards/48171151' },
            { text: "Artmage Non-Finito", link: '/examples/cards/74631897' },
            { text: "Pendulum Evolution", link: '/examples/cards/55795155' },
            { text: "Lady's Dragonmaid", link: '/examples/cards/48658295' },
            { text: "Surprise Fusion", link: '/examples/cards/35167375' },
            { text: "Eternal Favorite", link: '/examples/cards/87532344' },
            { text: "Astrograph Sorcerer", link: '/examples/cards/76794549' },
            { text: "Spellbook of the Grand Circle", link: '/examples/cards/11911336' },
            { text: "Ultra Polymerization", link: '/examples/cards/76647978' },
            { text: "Goyo Emperor", link: '/examples/cards/59255742' },
            { text: "Accel Synchro Stardust Dragon", link: '/examples/cards/30983281' },
            { text: "Exciting Melffy Time", link: '/examples/cards/58036097' },
            { text: "Deftero Enneacraft - \"alazoneIA\"", link: '/examples/cards/92171126' },
            { text: "Fiendsmith's Sequence", link: '/examples/cards/49867899' },
            { text: "D/D/D Alfred the Divine Sage King", link: '/examples/cards/11852093' },
            { text: "El Shaddoll Apkallone", link: '/examples/cards/50907446' },
            { text: "Mementotlan Fusion", link: '/examples/cards/66518509' },
            { text: "Meteoroa Drytron", link: '/examples/cards/24166324' },
            { text: "Favorite HERO Flame Wingman", link: '/examples/cards/13243124' },
            { text: "Gem-Knight Dispersion", link: '/examples/cards/24220368' },
            { text: "Invoked Sorath", link: '/examples/cards/43989315' },
            { text: "Performage Cup Tricker", link: '/examples/cards/6812770' },
            { text: "Ehther the Heavenly Monarch", link: '/examples/cards/96570609' },
          ],
        },
      ],
    },
    outline: {
      label: 'Contents',
      level: [2, 4],
    },
    search: {
      provider: 'local',
      options: {
        detailedView: true,
        disableQueryPersistence: true,
        miniSearch: {
          searchOptions: {
            prefix: true,
            fuzzy: 0.2,
            boost: { title: 4, titles: 2, text: 1 },
          },
        },
        _render: renderSearchMarkdown,
      },
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ElderLich/MDPro3_Sacred_Book' },
    ],
  },
});
