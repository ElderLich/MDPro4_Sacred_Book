import { defineConfig } from 'vitepress';

export default defineConfig({
  title: 'MDPro4 Sacred Book',
  description: 'MDPro4/YGOPro Lua card scripting reference.',
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: 'API', link: '/api/' },
      { text: 'Functions', link: '/api/functions/' },
      { text: 'Constants', link: '/api/constants' },
    ],
    sidebar: {
      '/api/functions/': [
        { text: 'Function Index', link: '/api/functions/' },
        {
          text: 'Namespaces',
          collapsed: false,
          items: [
              { text: 'Auxiliary', link: '/api/functions/Auxiliary/' },
              { text: 'Card', link: '/api/functions/Card/' },
              { text: 'Debug', link: '/api/functions/Debug/' },
              { text: 'Duel', link: '/api/functions/Duel/' },
              { text: 'Effect', link: '/api/functions/Effect/' },
              { text: 'Global', link: '/api/functions/Global/' },
              { text: 'Group', link: '/api/functions/Group/' },
              { text: 'bit', link: '/api/functions/bit/' },
          ],
        },
      ],
      '/api/': [
        { text: 'API Overview', link: '/api/' },
        { text: 'Functions', link: '/api/functions/' },
        { text: 'Constants', link: '/api/constants' },
      ],
    },
  },
});
