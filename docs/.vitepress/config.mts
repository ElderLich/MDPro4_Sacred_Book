import { defineConfig } from 'vitepress';
import navigation from './navigation.generated.json';

const analyticsToken = process.env.CLOUDFLARE_WEB_ANALYTICS_TOKEN?.trim();

function renderSearchMarkdown(src: string, env: any, md: any) {
  const relativePath = String(env.relativePath || '').replace(/\\/g, '/');
  if (relativePath.startsWith('examples/cards/') || relativePath.startsWith('examples/rush-cards/')) {
    return '';
  }
  if (relativePath.startsWith('api/functions/') || relativePath.startsWith('rush/api/functions/')) {
    src = src.split(/\n## Used By\n/)[0];
  }
  return md.render(src, env);
}

export default defineConfig({
  title: 'MDPro3 Sacred Book',
  description: 'MDPro3/YGOPro Lua card scripting lessons, examples, and API reference.',
  base: '/MDPro3_Sacred_Book/',
  cleanUrls: true,
  head: analyticsToken
    ? [
        [
          'script',
          {
            type: 'module',
            src: 'https://static.cloudflareinsights.com/beacon.min.js',
            'data-cf-beacon': JSON.stringify({ token: analyticsToken, spa: true }),
          },
        ],
      ]
    : [],
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Learn', link: '/learn/' },
      { text: 'Rush Duel', link: '/learn/rush-duel' },
      { text: 'API', link: '/api/' },
      { text: 'Examples', link: '/examples/' },
      { text: 'Script Explorer', link: '/tools/script-explorer' },
    ],
    sidebar: {
      '/learn/': [
        {
          text: 'Start Here',
          collapsed: false,
          items: [
            { text: 'Overview', link: '/learn/' },
            { text: 'Lua Essentials', link: '/learn/lua-essentials' },
            { text: 'Script Structure', link: '/learn/script-structure' },
            { text: 'First Scripts', link: '/learn/first-scripts' },
            { text: 'Beginner Script Ladder', link: '/learn/beginner-script-ladder' },
            { text: 'First Custom Card', link: '/learn/first-custom-card' },
            { text: 'Card Data and Script Wiring', link: '/learn/card-data-and-script-wiring' },
          ],
        },
        {
          text: 'Effects and Activation',
          collapsed: true,
          items: [
            { text: 'Effect Object', link: '/learn/effect-object' },
            { text: 'Effect Types', link: '/learn/effect-types' },
            { text: 'Categories and Properties', link: '/learn/categories-properties-and-hints' },
            { text: 'Callbacks', link: '/learn/effect-callbacks' },
            { text: 'Activated Effects', link: '/learn/activated-effects' },
            { text: 'Activation Legality', link: '/learn/activation-legality' },
            { text: 'Chain Timing', link: '/learn/chain-timing-and-activation-windows' },
            { text: 'Effect Lifecycle', link: '/learn/cost-target-operation-lifecycle' },
            { text: 'Targeting Flow', link: '/learn/targeting-flow' },
            { text: 'Client UI and Prompts', link: '/learn/client-ui-and-prompt-behavior' },
          ],
        },
        {
          text: 'Rush Duel',
          collapsed: false,
          items: [
            { text: 'Rush Learning Path', link: '/learn/rush-duel' },
            { text: 'Rush Requirements and Effects', link: '/learn/rush-duel-scripting' },
            { text: 'Maximum, Fusion, and Ritual', link: '/learn/rush-summon-procedures' },
          ],
        },
        {
          text: 'Spells and Traps',
          collapsed: true,
          items: [
            { text: 'Spell Cards', link: '/learn/spell-card-patterns' },
            { text: 'Quick-Play Spells', link: '/learn/quick-play-spells' },
            { text: 'Equip Spells', link: '/learn/equip-spells' },
            { text: 'Field Spells', link: '/learn/field-spells' },
            { text: 'Trap Cards', link: '/learn/trap-card-patterns' },
            { text: 'Normal and Continuous Traps', link: '/learn/normal-and-continuous-traps' },
            { text: 'Counter Traps', link: '/learn/counter-traps' },
          ],
        },
        {
          text: 'Summon Procedures',
          collapsed: true,
          items: [
            { text: 'Ritual Procedure', link: '/learn/ritual-procedure' },
            { text: 'Fusion Procedure', link: '/learn/fusion-procedure' },
            { text: 'Synchro Procedure', link: '/learn/synchro-procedure' },
            { text: 'Xyz Procedure', link: '/learn/xyz-procedure' },
            { text: 'Link Procedure', link: '/learn/link-procedure' },
            { text: 'Pendulum Procedure', link: '/learn/pendulum-procedure' },
            { text: 'Special Summon-only Monsters', link: '/learn/special-summon-only-monsters' },
            { text: 'Tribute Summon Materials', link: '/learn/tribute-summon-materials' },
          ],
        },
        {
          text: 'Cards, Groups, and Outcomes',
          collapsed: true,
          items: [
            { text: 'Filters and Groups', link: '/learn/filters-and-groups' },
            { text: 'Selection and Group Handling', link: '/learn/selection-and-group-handling' },
            { text: 'Min/Max Stat Selection', link: '/learn/min-max-stat-selection' },
            { text: 'Moving Cards', link: '/learn/moving-cards' },
            { text: 'Continuous Effects', link: '/learn/continuous-effects' },
            { text: 'Stat Modifiers', link: '/learn/continuous-stat-modifiers' },
            { text: 'Negation and Immunity', link: '/learn/negation-and-immunity' },
            { text: 'Control Change', link: '/learn/control-change' },
            { text: 'Battle Position Effects', link: '/learn/battle-position-effects' },
            { text: 'Field Zones', link: '/learn/field-zones-and-sequences' },
            { text: 'Affecting Cards', link: '/learn/affecting-cards' },
          ],
        },
        {
          text: 'Families and Archetypes',
          collapsed: true,
          items: [
            { text: 'Gemini Monsters', link: '/learn/gemini-monsters' },
            { text: 'Toon Monsters', link: '/learn/toon-monsters' },
            { text: 'Union Monsters', link: '/learn/union-monsters' },
            { text: 'Spirit Monsters', link: '/learn/spirit-monsters' },
            { text: 'Archetypes and Set Codes', link: '/learn/archetypes-and-setcodes' },
          ],
        },
        {
          text: 'Players and Effect Memory',
          collapsed: true,
          items: [
            { text: 'LP and Damage', link: '/learn/lp-recovery-and-damage' },
            { text: 'Player-Targeted Effects', link: '/learn/player-targeted-effects' },
            { text: 'Player Restrictions', link: '/learn/player-restrictions' },
            { text: 'Draw, Hand, and Deck Effects', link: '/learn/draw-hand-and-deck-effects' },
            { text: 'Counters', link: '/learn/counters' },
            { text: 'Flag Effects', link: '/learn/flag-effects' },
            { text: 'Count Limits', link: '/learn/count-limits' },
            { text: 'Reset Flags and Duration', link: '/learn/reset-flags-and-duration' },
          ],
        },
        {
          text: 'Review and Debug',
          collapsed: false,
          items: [
            { text: 'Engine and Script Updates', link: '/learn/engine-updates' },
            { text: 'Common Script Errors', link: '/learn/common-script-errors-and-debugging' },
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
          ],
        },
      ],
      '/rush/': [
        {
          text: 'Rush Duel',
          items: [
            { text: 'Learning Path', link: '/learn/rush-duel' },
            { text: 'Requirements and Effects', link: '/learn/rush-duel-scripting' },
            { text: 'Maximum, Fusion, and Ritual', link: '/learn/rush-summon-procedures' },
            { text: 'Rush API Overview', link: '/rush/api/' },
            { text: 'Helper Reference', link: '/rush/api/functions/' },
            { text: 'RushDuel / RD Namespace', link: '/rush/api/functions/RushDuel/' },
            { text: 'Rush Constants', link: '/rush/api/constants' },
            { text: 'Shared Core API', link: '/api/' },
            { text: 'Card Examples', link: '/examples/rush' },
          ],
        },
      ],
      '/api/functions/': [
        { text: 'API Overview', link: '/api/' },
        { text: 'Function Index', link: '/api/functions/' },
        { text: 'Rush Duel API', link: '/rush/api/' },
        {
          text: 'Namespaces',
          collapsed: false,
          items: navigation.namespaces,
        },
      ],
      '/api/': [
        { text: 'API Overview', link: '/api/' },
        { text: 'Functions', link: '/api/functions/' },
        { text: 'Constants', link: '/api/constants' },
        { text: 'Rush Duel API', link: '/rush/api/' },
        { text: 'Rush Helpers', link: '/rush/api/functions/' },
        { text: 'Rush Constants', link: '/rush/api/constants' },
      ],
      '/examples/': [
        {
          text: 'Examples',
          items: [
            { text: 'Overview', link: '/examples/' },
            { text: 'Rush Duel Examples', link: '/examples/rush' },
            { text: 'Mind Scan', link: '/examples/mind-scan' },
            ...navigation.examples,
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
    footer: {
      message: '<a href="/MDPro3_Sacred_Book/privacy">Privacy & analytics</a>',
    },
  },
});
