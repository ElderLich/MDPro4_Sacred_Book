import { defineConfig } from 'vitepress';

export default defineConfig({
  title: 'MDPro3 Sacred Book',
  description: 'MDPro3/YGOPro Lua card scripting lessons, examples, and API reference.',
  base: '/MDPro3_Sacred_Book/',
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Getting Started', link: '/getting-started/' },
      { text: 'Guides', link: '/guides/' },
      { text: 'API', link: '/api/' },
      { text: 'Examples', link: '/examples/' },
    ],
    sidebar: {
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
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ElderLich/MDPro3_Sacred_Book' },
    ],
  },
});
