import DefaultTheme from 'vitepress/theme';
import type { Theme } from 'vitepress';
import { onMounted, onUnmounted } from 'vue';
import ScriptExplorer from './components/ScriptExplorer.vue';
import './custom.css';

export default {
  extends: DefaultTheme,
  setup() {
    let removeSearchFallback: (() => void) | undefined;

    onMounted(() => {
      const handleSearchClick = (event: MouseEvent) => {
        const target = event.target instanceof Element ? event.target : null;
        const button = target?.closest('#local-search .DocSearch-Button');
        if (!button) {
          return;
        }

        window.setTimeout(() => {
          if (document.querySelector('.VPLocalSearchBox')) {
            return;
          }

          window.dispatchEvent(
            new KeyboardEvent('keydown', {
              key: 'k',
              code: 'KeyK',
              ctrlKey: true,
              bubbles: true,
              cancelable: true,
            }),
          );
        }, 0);
      };

      document.addEventListener('click', handleSearchClick, true);
      removeSearchFallback = () => document.removeEventListener('click', handleSearchClick, true);
    });

    onUnmounted(() => {
      removeSearchFallback?.();
    });
  },
  enhanceApp({ app }) {
    app.component('ScriptExplorer', ScriptExplorer);
  },
} satisfies Theme;
