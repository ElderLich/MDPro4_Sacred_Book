import DefaultTheme from 'vitepress/theme';
import type { Theme } from 'vitepress';
import ScriptExplorer from './components/ScriptExplorer.vue';
import './custom.css';

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ScriptExplorer', ScriptExplorer);
  },
} satisfies Theme;
