<script setup lang="ts">
import { computed, nextTick, onMounted, onUnmounted, ref, shallowRef, watch } from 'vue';
import { withBase } from 'vitepress';
type Format = 'standard' | 'rush';
type CardSummary = {
  id: number; name: string; archetypes: string[]; types: string[];
  attribute: string | null; race: string | null; level: number | null;
  attack: number | null; defense: number | null; detail: string; searchText: string;
  levelLabel?: string; legend?: boolean;
};
type CardDetail = CardSummary & {
  source: string; format: Format; scriptPath: string | null; alias: number;
  originalText: string; pendulumText: string; effectText: string; requirementText: string;
  preambleText: string; effectHeading: string; maximumAttack: number | null; packCode: string | null;
  scales: { left: number; right: number } | null; linkMarkers: string[];
  setcodes: { code: string; name: string | null }[];
  strings: { index: number; text: string }[]; raw: Record<string, string | number>;
};
type FormatInfo = { id: Format; label: string; count: number; index: string; searchText: string; sourceSha256: string };
type LocaleInfo = { id: string; label: string; nativeLabel: string; formats: FormatInfo[] };
type Manifest = { schemaVersion: number; defaultLocale: string; locales: LocaleInfo[] };
type Catalog = { format: Format; source: string; cards: CardSummary[] };
const PAGE_SIZE = 24;
const format = ref<Format>('standard');
const locale = ref('en-US');
const LANGUAGE_PREFERENCE = 'sacred-book-card-language';
const query = ref('');
const appliedQuery = ref('');
const typeFilter = ref('');
const archetypeFilter = ref('');
const searchCardText = ref(false);
const page = ref(1);
const selectedId = ref<number | null>(null);
const manifest = shallowRef<Manifest | null>(null);
const catalog = shallowRef<Catalog | null>(null);
const cardTexts = shallowRef<Record<string, string> | null>(null);
const selectedCard = shallowRef<CardDetail | null>(null);
const loading = ref(true);
const textLoading = ref(false);
const detailLoading = ref(false);
const error = ref('');
const textError = ref('');
const detailError = ref('');
const copyStatus = ref('');
const detailPanel = ref<HTMLElement>();
const resultsHeading = ref<HTMLElement>();
const indexCache = new Map<string, Catalog>();
const textCache = new Map<string, Record<string, string>>();
const detailCache = new Map<string, Record<string, CardDetail>>();
let indexRequest: AbortController | undefined;
let textRequest: AbortController | undefined;
let detailRequest: AbortController | undefined;
let debounce: ReturnType<typeof setTimeout> | undefined;
let copyTimer: ReturnType<typeof setTimeout> | undefined;
let restoring = false;
let mounted = false;
let loadVersion = 0;
const localeInfo = computed(() => manifest.value?.locales.find((item) => item.id === locale.value));
const formatInfo = computed(() => localeInfo.value?.formats.find((item) => item.id === format.value));
const catalogKey = computed(() => locale.value + ':' + format.value);
const records = computed(() => catalog.value?.cards || []);
const typeOptions = computed(() => [...new Set(records.value.flatMap((card) => card.types))].sort());
const archetypeOptions = computed(() => [...new Set(records.value.flatMap((card) => card.archetypes))].sort());
const tokens = computed(() => appliedQuery.value.normalize('NFKC').toLowerCase().trim().split(/\s+/).filter(Boolean));
const filteredCards = computed(() => records.value.filter((card) => {
  if (typeFilter.value && !card.types.includes(typeFilter.value)) return false;
  if (archetypeFilter.value && !card.archetypes.includes(archetypeFilter.value)) return false;
  if (!tokens.value.length) return true;
  const search = `${card.searchText} ${searchCardText.value ? cardTexts.value?.[card.id] || '' : ''}`;
  return tokens.value.every((token) => search.includes(token));
}));
const totalPages = computed(() => Math.max(1, Math.ceil(filteredCards.value.length / PAGE_SIZE)));
const currentPage = computed(() => Math.min(page.value, totalPages.value));
const visibleCards = computed(() => filteredCards.value.slice((currentPage.value - 1) * PAGE_SIZE, currentPage.value * PAGE_SIZE));
const hasFilters = computed(() => !!(query.value || typeFilter.value || archetypeFilter.value || searchCardText.value));
const filterBusy = computed(() => loading.value || (searchCardText.value && textLoading.value));
const selectedSummary = computed(() => records.value.find((card) => card.id === selectedId.value));
const scriptLink = computed(() => selectedCard.value?.scriptPath ? withBase(`/tools/script-explorer?format=${format.value}&q=${selectedCard.value.scriptPath.match(/c(\d+)\.lua$/)?.[1] || selectedCard.value.id}&mode=cards`) : '');
const markerPositions = [
  ['Top-left', '↖'], ['Top', '↑'], ['Top-right', '↗'],
  ['Left', '←'], ['', '◆'], ['Right', '→'],
  ['Bottom-left', '↙'], ['Bottom', '↓'], ['Bottom-right', '↘'],
];
function stat(value: number | null | undefined) { return value == null ? '—' : value < 0 ? '?' : String(value); }
function levelLabel(card: CardSummary) { return card.levelLabel || (card.types.includes('Link') ? 'Link' : card.types.includes('Xyz') ? 'Rank' : 'Level'); }
function cardTone(card: CardSummary) {
  for (const type of ['Spell', 'Trap', 'Link', 'Xyz', 'Synchro', 'Fusion', 'Ritual', 'Normal']) {
    if (card.types.includes(type)) return type.toLowerCase();
  }
  return 'effect';
}
function cardKind(card: CardSummary) { return card.types.includes('Spell') ? 'S' : card.types.includes('Trap') ? 'T' : 'M'; }
function isMonster(card: CardSummary) { return card.types.includes('Monster'); }
function formatCount(value: number) { return value.toLocaleString('en-US'); }
function urlForCurrentState() {
  const url = new URL(window.location.href);
  const values: Record<string, string> = {
    format: format.value === 'rush' ? 'rush' : '', lang: locale.value, q: query.value.trim(),
    type: typeFilter.value, archetype: archetypeFilter.value,
    text: searchCardText.value ? '1' : '', page: currentPage.value > 1 ? String(currentPage.value) : '',
    id: selectedId.value == null ? '' : String(selectedId.value),
  };
  for (const [key, value] of Object.entries(values)) {
    if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
  }
  return url;
}
function updateUrl(push = false) {
  if (!mounted || restoring) return;
  const url = urlForCurrentState();
  if (url.href === window.location.href) return;
  window.history[push ? 'pushState' : 'replaceState'](window.history.state, '', url);
}
async function fetchJson<T>(path: string, controller: AbortController): Promise<T> {
  const revision = path === 'manifest.json' ? '' : formatInfo.value?.sourceSha256;
  const resource = `${path}${revision ? `?v=${revision}` : ''}`;
  const response = await fetch(withBase(`/data/cards/${resource}`), { signal: controller.signal, ...(path === 'manifest.json' ? { cache: 'no-cache' as RequestCache } : {}) });
  if (!response.ok) throw new Error(`The card catalog could not be loaded (${response.status}). Please try again.`);
  return response.json();
}
function message(err: unknown) { return err instanceof Error ? err.message : 'The card catalog could not be loaded. Please try again.'; }
function clearSelection() {
  detailRequest?.abort(); selectedId.value = null; selectedCard.value = null;
  detailError.value = ''; detailLoading.value = false; copyStatus.value = '';
}
async function loadCardTexts() {
  textRequest?.abort(); textError.value = '';
  if (!searchCardText.value || !formatInfo.value) { textLoading.value = false; return; }
  const requestedKey = catalogKey.value;
  const cached = textCache.get(requestedKey);
  if (cached) { cardTexts.value = cached; textLoading.value = false; return; }
  const controller = new AbortController(); textRequest = controller; textLoading.value = true;
  try {
    const texts = await fetchJson<Record<string, string>>(formatInfo.value.searchText, controller);
    if (controller.signal.aborted || requestedKey !== catalogKey.value) return;
    if (textCache.size >= 2) textCache.delete(textCache.keys().next().value!);
    textCache.set(requestedKey, texts); cardTexts.value = texts;
  } catch (err) { if (!controller.signal.aborted) textError.value = message(err); }
  finally { if (!controller.signal.aborted) textLoading.value = false; }
}
async function loadSelectedCard() {
  detailRequest?.abort(); selectedCard.value = null; detailError.value = ''; copyStatus.value = '';
  if (detailPanel.value) detailPanel.value.scrollTop = 0;
  if (selectedId.value == null) { detailLoading.value = false; return; }
  const summary = selectedSummary.value;
  if (!summary) { detailError.value = 'This card ID is not in the selected database. Try the other format or return to the results.'; detailLoading.value = false; return; }
  const controller = new AbortController(); detailRequest = controller;
  const requestedId = selectedId.value; detailLoading.value = true;
  try {
    let shard = detailCache.get(summary.detail);
    if (!shard) {
      shard = await fetchJson<Record<string, CardDetail>>(summary.detail, controller);
      if (controller.signal.aborted) return;
      // Bound retained detail data when browsing many pages on a phone.
      if (detailCache.size >= 12) detailCache.delete(detailCache.keys().next().value!);
      detailCache.set(summary.detail, shard);
    }
    if (controller.signal.aborted || requestedId !== selectedId.value) return;
    if (!shard[requestedId]) throw new Error('Details for this card could not be found. Please reload the catalog.');
    selectedCard.value = shard[requestedId];
  } catch (err) { if (!controller.signal.aborted) detailError.value = message(err); }
  finally { if (!controller.signal.aborted) detailLoading.value = false; }
}
async function loadCatalog() {
  const version = ++loadVersion;
  indexRequest?.abort(); textRequest?.abort(); detailRequest?.abort();
  const controller = new AbortController(); indexRequest = controller;
  loading.value = true; error.value = ''; textError.value = '';
  catalog.value = null; cardTexts.value = null; selectedCard.value = null;
  detailLoading.value = false; textLoading.value = false;
  try {
    if (!manifest.value) manifest.value = await fetchJson<Manifest>('manifest.json', controller);
    if (controller.signal.aborted || version !== loadVersion) return;
    if (!localeInfo.value) locale.value = manifest.value.defaultLocale || 'en-US';
    const info = formatInfo.value;
    if (!info) throw new Error('This format is not available in the card catalog.');
    let loaded = indexCache.get(catalogKey.value);
    if (!loaded) {
      loaded = await fetchJson<Catalog>(info.index, controller);
      if (controller.signal.aborted || version !== loadVersion) return;
      if (indexCache.size >= 3) indexCache.delete(indexCache.keys().next().value!);
      indexCache.set(catalogKey.value, loaded);
    }
    catalog.value = loaded;
    await loadCardTexts();
    if (controller.signal.aborted || version !== loadVersion) return;
    page.value = currentPage.value; loading.value = false;
    await loadSelectedCard();
  } catch (err) { if (!controller.signal.aborted && version === loadVersion) error.value = message(err); }
  finally { if (!controller.signal.aborted && version === loadVersion) loading.value = false; }
}
function applyFilters() {
  if (!mounted || restoring) return;
  clearTimeout(debounce); appliedQuery.value = query.value; page.value = 1; clearSelection(); updateUrl();
}
watch(query, () => {
  if (!mounted || restoring) return;
  clearTimeout(debounce); debounce = setTimeout(applyFilters, 180);
}, { flush: 'sync' });
watch([typeFilter, archetypeFilter], applyFilters, { flush: 'sync' });
watch(searchCardText, () => {
  if (!mounted || restoring) return;
  applyFilters(); void loadCardTexts();
}, { flush: 'sync' });
function resetFilters() {
  restoring = true;
  query.value = ''; appliedQuery.value = ''; typeFilter.value = ''; archetypeFilter.value = ''; searchCardText.value = false;
  restoring = false;
  textRequest?.abort(); textLoading.value = false; textError.value = ''; applyFilters();
}
function savedLanguage() {
  try { return window.localStorage.getItem(LANGUAGE_PREFERENCE) || 'en-US'; }
  catch { return 'en-US'; }
}
function changeLanguage(event: Event) {
  const value = (event.target as HTMLSelectElement).value;
  if (!manifest.value?.locales.some((item) => item.id === value) || value === locale.value) return;
  clearTimeout(debounce);
  locale.value = value;
  try { window.localStorage.setItem(LANGUAGE_PREFERENCE, value); } catch { /* Storage can be unavailable in private browsing. */ }
  // Retain the same card and format when moving between translations.
  // Missing translated cards show the explicit unavailable state after loading.
  restoring = true;
  query.value = ''; appliedQuery.value = ''; archetypeFilter.value = ''; page.value = 1;
  restoring = false;
  updateUrl(true);
  void loadCatalog();
}
function changeFormat(value: Format) {
  if (format.value === value) return;
  clearTimeout(debounce); clearSelection(); restoring = true;
  format.value = value; query.value = ''; appliedQuery.value = ''; typeFilter.value = ''; archetypeFilter.value = ''; page.value = 1;
  restoring = false; updateUrl(true); void loadCatalog();
}
async function selectCard(card: CardSummary) {
  clearTimeout(debounce); appliedQuery.value = query.value;
  selectedId.value = card.id; updateUrl(true);
  const loadingCard = loadSelectedCard();
  await nextTick();
  if (window.matchMedia('(max-width: 760px)').matches) {
    detailPanel.value?.focus({ preventScroll: true }); detailPanel.value?.scrollIntoView({ block: 'start' });
  }
  await loadingCard;
}
async function backToResults() {
  const previous = selectedId.value; clearSelection(); updateUrl(); await nextTick();
  const button = document.getElementById(`card-result-${previous}`);
  (button || resultsHeading.value)?.focus({ preventScroll: true });
  if (window.matchMedia('(max-width: 760px)').matches) (button || resultsHeading.value)?.scrollIntoView({ block: 'nearest' });
}
async function changePage(delta: number) {
  page.value = Math.max(1, Math.min(totalPages.value, currentPage.value + delta));
  clearSelection(); updateUrl(); await nextTick();
  resultsHeading.value?.focus({ preventScroll: true }); resultsHeading.value?.scrollIntoView({ block: 'start' });
}
function restoreLocation() {
  clearTimeout(debounce);
  const params = new URLSearchParams(window.location.search); restoring = true;
  format.value = params.get('format') === 'rush' ? 'rush' : 'standard';
  locale.value = params.get('lang') || savedLanguage();
  query.value = params.get('q') || ''; appliedQuery.value = query.value;
  typeFilter.value = params.get('type') || ''; archetypeFilter.value = params.get('archetype') || '';
  searchCardText.value = params.get('text') === '1';
  const requestedPage = Number(params.get('page'));
  page.value = Number.isSafeInteger(requestedPage) && requestedPage > 0 ? requestedPage : 1;
  const id = params.get('id');
  selectedId.value = id && /^\d+$/.test(id) && Number.isSafeInteger(Number(id)) ? Number(id) : null;
  restoring = false; void loadCatalog();
}
async function copyLink() {
  try { updateUrl(); await navigator.clipboard.writeText(window.location.href); copyStatus.value = 'Link copied'; }
  catch { copyStatus.value = 'Copy the URL from your address bar to share this card.'; }
  clearTimeout(copyTimer); copyTimer = setTimeout(() => { copyStatus.value = ''; }, 4000);
}
onMounted(() => { mounted = true; restoreLocation(); window.addEventListener('popstate', restoreLocation); });
onUnmounted(() => {
  mounted = false; indexRequest?.abort(); textRequest?.abort(); detailRequest?.abort();
  clearTimeout(debounce); clearTimeout(copyTimer); window.removeEventListener('popstate', restoreLocation);
});
</script>
<template>
  <section class="card-explorer" :class="{ 'has-selection': selectedId !== null, 'is-rush': format === 'rush' }" aria-label="Card Explorer">
    <div class="catalog-toolbar">
      <div class="catalog-overview">
        <div class="format-switch" role="group" aria-label="Card format">
          <button type="button" :aria-pressed="format === 'standard'" @click="changeFormat('standard')">Standard</button>
          <button type="button" :aria-pressed="format === 'rush'" @click="changeFormat('rush')">Rush Duel</button>
        </div>
        <label class="language-select" for="card-language"><span>Card language</span><select id="card-language" :value="locale" @change="changeLanguage"><option v-if="!manifest" value="en-US">English</option><option v-for="language in manifest?.locales" :key="language.id" :value="language.id">{{ language.nativeLabel === language.label ? language.label : language.nativeLabel + ' · ' + language.label }}</option></select></label>
        <span class="catalog-count">{{ formatCount(formatInfo?.count || 0) }} cards<span class="count-note"> · {{ format === 'rush' ? 'Rush database' : 'Standard database' }}</span></span>
      </div>
      <p class="language-note">Your language choice is remembered on this device. Card text follows the selected database; some cards may still use English.</p>
      <div class="catalog-filters">
        <label class="search-field" for="card-search"><span>Find a card</span>
          <div class="search-input"><svg aria-hidden="true" viewBox="0 0 24 24"><circle cx="10" cy="10" r="6" /><path d="m15 15 6 6" /></svg><input id="card-search" v-model="query" type="search" placeholder="Name, card ID, or archetype…" autocomplete="off" spellcheck="false" /></div>
        </label>
        <label for="card-type"><span>Card type</span><select id="card-type" v-model="typeFilter" :disabled="loading"><option value="">All types</option><option v-for="type in typeOptions" :key="type" :value="type">{{ type }}</option></select></label>
        <label for="card-archetype"><span>Archetype</span><select id="card-archetype" v-model="archetypeFilter" :disabled="loading"><option value="">All archetypes</option><option v-for="archetype in archetypeOptions" :key="archetype" :value="archetype">{{ archetype }}</option></select></label>
      </div>
      <div class="filter-options">
        <label class="text-search"><input v-model="searchCardText" type="checkbox" /> Search card text <span class="optional-note">(loads on demand)</span></label>
        <button v-if="hasFilters" type="button" class="quiet-button" @click="resetFilters">Clear filters</button>
      </div>
      <p class="search-help">{{ searchCardText ? 'Every search word can match the name, ID, archetype, or printed card text.' : 'Search names, IDs, and archetypes. Enable card text to find wording inside effects.' }}</p>
    </div>
    <div v-if="error" class="catalog-state error-state" role="alert"><strong>Card catalog unavailable</strong><p>{{ error }}</p><button type="button" class="secondary-button" @click="loadCatalog">Try again</button><button v-if="selectedId !== null" type="button" class="quiet-button" @click="backToResults">Back to results</button></div>
    <div v-else-if="filterBusy" class="catalog-state" role="status"><span class="loading-indicator" aria-hidden="true"></span><strong>{{ textLoading ? 'Loading searchable card text…' : `Loading ${format === 'rush' ? 'Rush Duel' : 'Standard'} cards…` }}</strong><p>Only the selected database is loaded.</p></div>
    <div v-else-if="textError" class="catalog-state error-state" role="alert"><strong>Card text search unavailable</strong><p>{{ textError }}</p><button type="button" class="secondary-button" @click="loadCardTexts">Try again</button><button type="button" class="quiet-button" @click="searchCardText = false">Search without card text</button></div>
    <div v-else class="catalog-workspace">
      <section class="catalog-results" aria-label="Card results">
        <div class="results-topline"><h2 ref="resultsHeading" tabindex="-1">{{ formatCount(filteredCards.length) }} {{ filteredCards.length === 1 ? 'card' : 'cards' }}</h2><span v-if="filteredCards.length">{{ (currentPage - 1) * PAGE_SIZE + 1 }}–{{ Math.min(currentPage * PAGE_SIZE, filteredCards.length) }}</span></div>
        <p class="visually-hidden" role="status" aria-live="polite">{{ formatCount(filteredCards.length) }} matching cards. Page {{ currentPage }} of {{ totalPages }}.</p>
        <div v-if="!filteredCards.length" class="empty-results"><span aria-hidden="true">⌕</span><h3>No matching cards</h3><p>Try fewer words, another archetype, or the other format.</p><button type="button" class="secondary-button" @click="resetFilters">Clear filters</button></div>
        <ul v-else class="card-results-list">
          <li v-for="card in visibleCards" :key="card.id">
            <button :id="`card-result-${card.id}`" type="button" class="card-result" :class="[`tone-${cardTone(card)}`, { selected: selectedId === card.id }]" :aria-pressed="selectedId === card.id" @click="selectCard(card)">
              <span class="card-kind" aria-hidden="true">{{ cardKind(card) }}</span>
              <span class="result-main"><strong :lang="locale">{{ card.name }}</strong><span class="result-type">{{ card.types.join(' / ') }}</span><span class="result-stats"><span>#{{ card.id }}</span><span v-if="isMonster(card)">{{ levelLabel(card) }} {{ card.level }} · ATK {{ stat(card.attack) }}</span></span></span>
              <span class="result-arrow" aria-hidden="true">›</span>
            </button>
          </li>
        </ul>
        <nav v-if="filteredCards.length" class="results-pagination" aria-label="Card result pages"><button type="button" class="secondary-button" :disabled="currentPage <= 1" @click="changePage(-1)"><span aria-hidden="true">← </span>Previous</button><span>{{ currentPage }} / {{ totalPages }}</span><button type="button" class="secondary-button" :disabled="currentPage >= totalPages" @click="changePage(1)">Next<span aria-hidden="true"> →</span></button></nav>
      </section>
      <section ref="detailPanel" class="card-detail-panel" :class="selectedCard ? `tone-${cardTone(selectedCard)}` : ''" tabindex="-1" aria-label="Card details">
        <template v-if="selectedId !== null">
          <div class="detail-actions"><button type="button" class="quiet-button back-button" @click="backToResults">← Back to results</button><button type="button" class="quiet-button" @click="copyLink">Copy card link</button></div>
          <p v-if="copyStatus" class="copy-status" role="status">{{ copyStatus }}</p>
          <div v-if="detailLoading" class="catalog-state" role="status"><span class="loading-indicator" aria-hidden="true"></span><strong>Loading card details…</strong></div>
          <div v-else-if="detailError" class="catalog-state error-state" role="alert"><strong>Card details unavailable</strong><p>{{ detailError }}</p><button v-if="selectedSummary" type="button" class="secondary-button" @click="loadSelectedCard">Try again</button></div>
          <article v-else-if="selectedCard" class="card-sheet">
            <header class="card-sheet-header"><div class="detail-eyebrow"><span>{{ format === 'rush' ? 'RUSH DUEL' : 'STANDARD' }}</span><span>#{{ selectedCard.id }}</span></div><h2 :lang="locale">{{ selectedCard.name }}</h2><div class="type-line">{{ selectedCard.types.join(' / ') }}</div><div class="card-tags"><span v-if="selectedCard.attribute" class="attribute-tag">{{ selectedCard.attribute }}</span><span v-if="selectedCard.race">{{ selectedCard.race }}</span><span v-if="selectedCard.legend" class="legend-tag">Legend</span></div></header>
            <div v-if="isMonster(selectedCard)" class="card-stat-grid"><div><span>{{ levelLabel(selectedCard) }}</span><strong>{{ selectedCard.level }}</strong></div><div><span>ATK</span><strong>{{ stat(selectedCard.attack) }}</strong></div><div v-if="!selectedCard.types.includes('Link')"><span>DEF</span><strong>{{ stat(selectedCard.defense) }}</strong></div><div v-if="selectedCard.maximumAttack !== null && selectedCard.maximumAttack !== undefined" class="maximum-stat"><span>Maximum ATK</span><strong>{{ stat(selectedCard.maximumAttack) }}</strong></div></div>
            <div v-if="selectedCard.scales || selectedCard.linkMarkers?.length" class="card-special-stats"><div v-if="selectedCard.scales" class="pendulum-scales"><span>Pendulum scales</span><strong><span class="left-scale">◀︎ {{ selectedCard.scales.left }}</span><span class="scale-divider">/</span><span class="right-scale">{{ selectedCard.scales.right }} ▶︎</span></strong></div><div v-if="selectedCard.linkMarkers?.length" class="link-marker-section"><div><span>Link markers</span><p>{{ selectedCard.linkMarkers.join(', ') }}</p></div><div class="link-marker-grid" aria-hidden="true"><span v-for="[label, arrow] in markerPositions" :key="label" :class="{ active: selectedCard.linkMarkers.includes(label), center: !label }">{{ arrow }}</span></div></div></div>
            <div class="archetype-section"><h3>Archetype</h3><div v-if="selectedCard.archetypes.length" class="archetype-chips"><span v-for="archetype in selectedCard.archetypes" :key="archetype">{{ archetype }}</span></div><p v-else class="muted">No archetype recorded.</p></div>
            <section v-if="selectedCard.pendulumText" class="printed-text pendulum-text"><h3><span class="text-section-mark" aria-hidden="true">◈</span> Pendulum effect</h3><p :lang="locale">{{ selectedCard.pendulumText }}</p></section>
            <section v-if="selectedCard.preambleText" class="printed-text"><h3>Card conditions</h3><p :lang="locale">{{ selectedCard.preambleText }}</p></section>
            <section v-if="selectedCard.requirementText" class="printed-text requirement-text"><h3><span class="text-section-mark" aria-hidden="true">◇</span> Requirement</h3><p :lang="locale">{{ selectedCard.requirementText }}</p></section>
            <section class="printed-text effect-text"><h3>{{ selectedCard.types.includes('Normal') && !selectedCard.types.includes('Effect') ? 'Card text' : selectedCard.effectHeading || 'Card effect' }}</h3><p v-if="selectedCard.effectText" :lang="locale">{{ selectedCard.effectText }}</p><p v-else class="muted">No effect text recorded.</p></section>
            <div class="card-provenance"><span v-if="selectedCard.packCode"><strong>Rush card code</strong> {{ selectedCard.packCode }}</span><span><strong>Database</strong> {{ selectedCard.source || catalog?.source }}</span><span v-if="selectedCard.alias"><strong>Alias card ID</strong> {{ selectedCard.alias }}</span></div>
            <a v-if="scriptLink" class="script-link" :href="scriptLink">Explore this card’s script <span aria-hidden="true">→</span></a><p v-else class="no-script">No individual script is included for this card.</p>
            <details class="technical-details"><summary>Database details</summary><dl><template v-for="(value, key) in selectedCard.raw" :key="key"><dt>{{ key }}</dt><dd>{{ value }}</dd></template></dl><div v-if="selectedCard.setcodes?.length" class="database-subsection"><h3>Setcodes</h3><p v-for="setcode in selectedCard.setcodes" :key="setcode.code"><code>{{ setcode.code }}</code> {{ setcode.name || 'Unnamed archetype' }}</p></div><div v-if="selectedCard.strings?.length" class="database-subsection"><h3>Script strings</h3><p v-for="entry in selectedCard.strings" :key="entry.index"><code>str{{ entry.index + 1 }}</code> {{ entry.text }}</p></div></details>
            <details class="technical-details original-text"><summary>Original database text</summary><p :lang="locale">{{ selectedCard.originalText || 'No text recorded.' }}</p></details>
          </article>
        </template>
        <div v-else class="detail-placeholder"><div class="placeholder-cards" aria-hidden="true"><span></span><span>✦</span></div><span class="detail-kicker">THE COMPLETE CARD</span><h2>A closer look at every card</h2><p>Select a result to read its effects, archetypes, and stats together. Pendulum text and Rush requirements get their own space.</p><div><span>Full card text</span><span>Database details</span><span>Script connections</span></div></div>
      </section>
    </div>
  </section>
</template>
<style scoped>
.card-explorer { --card-accent: var(--vp-c-brand-1); margin: 28px 0 40px; min-width: 0; font-size: 14px; }
.card-explorer *, .card-explorer *::before, .card-explorer *::after { box-sizing: border-box; }
.card-explorer button, .card-explorer input, .card-explorer select { font: inherit; }
.card-explorer button { cursor: pointer; }
.card-explorer button:disabled { cursor: default; opacity: .45; }
.card-explorer :is(button, input, select, summary, a):focus-visible { outline: 3px solid var(--vp-c-brand-1); outline-offset: 3px; }
.card-explorer :is(h2,h3,p,ul) { margin: 0; }
.card-explorer h2, .card-explorer h3 { border: 0; padding: 0; letter-spacing: normal; }
.card-explorer .tone-spell { --card-accent: #27a58a; }
.card-explorer .tone-trap { --card-accent: #c65b98; }
.card-explorer .tone-link { --card-accent: #477fd3; }
.card-explorer .tone-xyz { --card-accent: #9b91bc; }
.card-explorer .tone-synchro { --card-accent: #99a7b7; }
.card-explorer .tone-fusion { --card-accent: #a777d0; }
.card-explorer .tone-ritual { --card-accent: #698ed0; }
.card-explorer .tone-normal { --card-accent: #c9a048; }
.card-explorer .tone-effect { --card-accent: #c58953; }
.catalog-toolbar { padding: 20px; border: 1px solid var(--vp-c-divider); border-radius: 16px; background: var(--vp-c-bg-soft); }
.catalog-overview { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; }
.format-switch { display: inline-flex; gap: 4px; padding: 4px; border: 1px solid var(--vp-c-divider); border-radius: 12px; background: var(--vp-c-bg); }
.format-switch button { min-height: 44px; padding: 8px 20px; border-radius: 8px; color: var(--vp-c-text-2); font-weight: 650; }
.format-switch button[aria-pressed='true'] { color: var(--vp-c-brand-1); background: var(--vp-c-brand-soft); box-shadow: inset 0 0 0 1px var(--vp-c-brand-1); }
.is-rush .format-switch button[aria-pressed='true'] { color: var(--vp-c-warning-1); background: var(--vp-c-warning-soft); box-shadow: inset 0 0 0 1px var(--vp-c-warning-1); }
.language-select { display: flex; flex-direction: column; gap: 4px; min-width: 0; max-width: 250px; margin-left: auto; color: var(--vp-c-text-2); font-size: 11px; }
.language-select select { width: 100%; min-width: 0; min-height: 44px; padding: 8px 24px 8px 10px; border: 1px solid var(--vp-c-divider); border-radius: 8px; color: var(--vp-c-text-1); background: var(--vp-c-bg); appearance: auto; font-size: 14px; }
.card-explorer .language-note { margin: -6px 0 18px; color: var(--vp-c-text-2); font-size: 11px; line-height: 1.6; }
.catalog-count { color: var(--vp-c-text-2); font-size: 13px; font-variant-numeric: tabular-nums; }
.catalog-filters { display: grid; grid-template-columns: minmax(0, 1.8fr) minmax(0, 1fr) minmax(0, 1fr); gap: 12px; }
.catalog-filters label { display: flex; min-width: 0; flex-direction: column; gap: 7px; color: var(--vp-c-text-2); font-size: 12px; font-weight: 600; }
.catalog-filters :is(input,select) { min-height: 46px; width: 100%; min-width: 0; border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 10px 12px; background: var(--vp-c-bg); color: var(--vp-c-text-1); font-size: 14px; font-weight: 400; }
.catalog-filters select { padding-right: 24px; appearance: auto; text-overflow: ellipsis; }
.search-input { position: relative; }
.search-input svg { position: absolute; left: 13px; top: 14px; width: 18px; height: 18px; fill: none; stroke: var(--vp-c-text-3); stroke-width: 1.8; pointer-events: none; }
.search-input input { padding-left: 39px; }
.filter-options { display: flex; justify-content: space-between; align-items: center; gap: 10px; flex-wrap: wrap; margin-top: 8px; }
.text-search { display: inline-flex; align-items: center; min-height: 44px; gap: 8px; cursor: pointer; }
.text-search input { width: 18px; height: 18px; accent-color: var(--vp-c-brand-1); flex: 0 0 auto; }
.optional-note, .search-help { color: var(--vp-c-text-2); font-size: 12px; }
.search-help { line-height: 1.6; }
.quiet-button { min-height: 44px; padding: 9px 8px; border-radius: 6px; color: var(--vp-c-brand-1); font-weight: 600; font-size: 13px !important; }
.quiet-button:hover { background: var(--vp-c-brand-soft); }
.secondary-button { min-height: 44px; padding: 9px 13px; border: 1px solid var(--vp-c-divider); border-radius: 8px; background: var(--vp-c-bg); color: var(--vp-c-text-1); font-weight: 600; }
.secondary-button:hover:not(:disabled) { border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); }
.catalog-workspace { display: grid; grid-template-columns: minmax(0, .9fr) minmax(0, 1.25fr); align-items: start; gap: 24px; margin-top: 24px; }
.catalog-results, .card-detail-panel { min-width: 0; }
.results-topline { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 12px; }
.results-topline h2 { font-size: 15px; line-height: 24px; font-weight: 650; scroll-margin-top: 120px; }
.results-topline > span { color: var(--vp-c-text-2); font-size: 12px; font-variant-numeric: tabular-nums; }
.card-explorer .card-results-list { display: flex; flex-direction: column; gap: 7px; padding: 0; list-style: none; }
.card-results-list li { margin: 0; }
.card-result { display: flex; align-items: center; gap: 12px; width: 100%; min-width: 0; border: 1px solid var(--vp-c-divider); border-left: 3px solid var(--card-accent); border-radius: 10px; padding: 13px 12px; text-align: left; background: var(--vp-c-bg); transition: background .15s, border-color .15s; }
.card-result:hover { background: var(--vp-c-bg-soft); }
.card-result.selected { border-color: var(--card-accent); background: var(--vp-c-bg-soft); box-shadow: 0 0 0 1px var(--card-accent); }
.card-kind { display: inline-flex; align-items: center; justify-content: center; width: 29px; height: 38px; flex: 0 0 auto; border: 1px solid var(--card-accent); border-radius: 4px; color: var(--vp-c-text-2); font-size: 11px; font-weight: 700; background: var(--vp-c-bg-soft); }
.result-main { display: flex; min-width: 0; flex: 1; flex-direction: column; align-items: flex-start; gap: 4px; text-align: left; }
.result-main strong { color: var(--vp-c-text-1); font-size: 14px; line-height: 1.45; overflow-wrap: anywhere; }
.result-type { color: var(--vp-c-text-2); font-size: 11px; line-height: 1.5; }
.result-stats { display: flex; gap: 6px 12px; flex-wrap: wrap; color: var(--vp-c-text-2); font-size: 10px; font-variant-numeric: tabular-nums; line-height: 1.5; }
.result-arrow { color: var(--vp-c-text-3); font-size: 24px; }
.results-pagination { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 16px; }
.results-pagination span { color: var(--vp-c-text-2); font-size: 12px; }
.results-pagination .secondary-button { padding: 9px 10px; font-size: 12px; }
.card-detail-panel { position: sticky; top: 88px; border: 1px solid var(--vp-c-divider); border-radius: 16px; overflow-x: hidden; overflow-y: auto; max-height: calc(100dvh - 112px); scrollbar-gutter: stable; background: var(--vp-c-bg); scroll-margin-top: 110px; }
.detail-actions { display: flex; align-items: center; justify-content: space-between; padding: 4px 12px; border-bottom: 1px solid var(--vp-c-divider); }
.copy-status { padding: 8px 20px; color: var(--vp-c-brand-1); background: var(--vp-c-brand-soft); font-size: 12px; overflow-wrap: anywhere; }
.card-sheet-header { padding: 24px; border-top: 4px solid var(--card-accent); background: linear-gradient(130deg, var(--vp-c-bg-soft), var(--vp-c-bg)); }
.detail-eyebrow { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; color: var(--vp-c-text-2); font-size: 10px; font-weight: 650; letter-spacing: 1.2px; }
.is-rush .detail-eyebrow > span:first-child { color: var(--vp-c-warning-1); }
.card-sheet-header h2 { margin: 12px 0 10px; font-size: clamp(22px, 2.2vw, 29px); line-height: 1.25; font-weight: 700; overflow-wrap: anywhere; }
.type-line { color: var(--vp-c-text-2); font-size: 12px; line-height: 1.7; }
.card-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
.card-tags span { padding: 2px 8px; border: 1px solid var(--vp-c-divider); border-radius: 5px; font-size: 10px; font-weight: 600; }
.card-tags .legend-tag { color: var(--vp-c-warning-1); background: var(--vp-c-warning-soft); }
.card-stat-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(85px,1fr)); gap: 1px; background: var(--vp-c-divider); border-block: 1px solid var(--vp-c-divider); }
.card-stat-grid > div { display: flex; align-items: center; flex-direction: column; gap: 5px; padding: 14px 8px; background: var(--vp-c-bg-soft); }
.card-stat-grid span { font-size: 10px; color: var(--vp-c-text-2); text-transform: uppercase; letter-spacing: .7px; }
.card-stat-grid strong { font-size: 23px; line-height: 1.2; font-variant-numeric: tabular-nums; font-weight: 700; }
.maximum-stat strong { color: var(--vp-c-warning-1); }
.card-special-stats { padding: 16px 24px 0; }
.pendulum-scales, .link-marker-section { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 12px; border: 1px solid var(--vp-c-divider); border-radius: 8px; background: var(--vp-c-bg-soft); }
.pendulum-scales > span, .link-marker-section > div > span { font-size: 12px; color: var(--vp-c-text-2); }
.pendulum-scales strong { display: inline-flex; gap: 8px; font-size: 20px; font-variant-numeric: tabular-nums; }
.left-scale { color: var(--vp-c-brand-1); }
.right-scale { color: var(--vp-c-danger-1); }
.scale-divider { color: var(--vp-c-text-3); font-weight: 400; }
.link-marker-section { margin-top: 8px; }
.link-marker-section p { margin-top: 4px; font-size: 11px; line-height: 1.6; color: var(--vp-c-text-2); }
.link-marker-grid { display: grid; grid-template-columns: repeat(3,22px); gap: 2px; flex: 0 0 auto; }
.link-marker-grid span { display: flex; align-items: center; justify-content: center; height: 22px; border-radius: 3px; background: var(--vp-c-bg); color: var(--vp-c-divider) !important; font-size: 18px !important; line-height: 1; }
.link-marker-grid span.active { color: var(--vp-c-brand-1) !important; background: var(--vp-c-brand-soft); }
.link-marker-grid span.center { color: var(--vp-c-text-3) !important; font-size: 9px !important; }
.archetype-section { padding: 20px 24px 0; }
.archetype-section h3 { color: var(--vp-c-text-2); font-size: 11px; font-weight: 600; }
.archetype-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 7px; }
.archetype-chips span { border-radius: 5px; padding: 2px 8px; background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); font-size: 12px; line-height: 1.8; overflow-wrap: anywhere; }
.archetype-section .muted { margin-top: 5px; font-size: 12px; }
.printed-text { margin: 20px 24px 0; }
.printed-text h3 { margin-bottom: 10px; font-size: 12px; font-weight: 650; }
.printed-text p { font-size: 14px; line-height: 1.85; white-space: pre-wrap; overflow-wrap: anywhere; }
.pendulum-text, .requirement-text { padding: 15px; border: 1px solid var(--vp-c-divider); border-left: 3px solid var(--vp-c-brand-1); border-radius: 8px; background: var(--vp-c-bg-soft); }
.requirement-text { border-left-color: var(--vp-c-warning-1); }
.text-section-mark { margin-right: 5px; color: var(--vp-c-brand-1); }
.requirement-text .text-section-mark { color: var(--vp-c-warning-1); }
.muted { color: var(--vp-c-text-2); }
.card-provenance { display: flex; flex-direction: column; gap: 4px; margin: 24px 24px 12px; color: var(--vp-c-text-2); font-size: 11px; line-height: 1.7; overflow-wrap: anywhere; }
.card-provenance strong { display: inline-block; margin-right: 5px; font-weight: 600; }
.script-link { display: flex; justify-content: space-between; align-items: center; gap: 12px; min-height: 46px; margin: 16px 24px; padding: 11px 14px; border: 1px solid var(--vp-c-brand-1); border-radius: 8px; font-size: 13px; text-decoration: none !important; }
.script-link:hover { background: var(--vp-c-brand-soft); }
.card-explorer .no-script { margin: 12px 24px 20px; color: var(--vp-c-text-2); font-size: 12px; }
.technical-details { border-top: 1px solid var(--vp-c-divider); padding: 0 24px; }
.technical-details summary { display: list-item; min-height: 48px; padding: 13px 0; color: var(--vp-c-text-2); font-size: 12px; cursor: pointer; }
.technical-details dl { display: grid; grid-template-columns: minmax(0,.8fr) minmax(0,1.2fr); margin: 0 0 16px; gap: 5px 12px; font-size: 11px; font-family: var(--vp-font-family-mono); }
.technical-details dt { color: var(--vp-c-text-2); }
.technical-details dd { margin: 0; overflow-wrap: anywhere; }
.database-subsection { margin-bottom: 18px; }
.database-subsection h3 { margin-bottom: 7px; font-size: 12px; }
.database-subsection p { margin-top: 5px; font-size: 12px; line-height: 1.7; white-space: pre-wrap; overflow-wrap: anywhere; }
.original-text > p { margin: 0 0 20px; font-size: 12px; line-height: 1.8; white-space: pre-wrap; overflow-wrap: anywhere; }
.catalog-state { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 12px; padding: 40px 20px; text-align: center; }
.catalog-state strong { font-size: 15px; }
.catalog-state p { width: 100%; color: var(--vp-c-text-2); line-height: 1.7; overflow-wrap: anywhere; }
.error-state { border: 1px solid var(--vp-c-divider); border-radius: 12px; margin-top: 18px; }
.card-detail-panel .error-state { border: 0; margin: 0; }
.loading-indicator { width: 15px; height: 15px; border: 2px solid var(--vp-c-divider); border-top-color: var(--vp-c-brand-1); border-radius: 50%; animation: spin .7s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.empty-results { padding: 32px 12px; text-align: center; border: 1px dashed var(--vp-c-divider); border-radius: 12px; }
.empty-results > span { color: var(--vp-c-text-3); font-size: 36px; }
.empty-results h3 { margin: 16px 0 8px; font-size: 16px; }
.empty-results p { color: var(--vp-c-text-2); line-height: 1.7; margin-bottom: 18px; }
.detail-placeholder { display: flex; align-items: center; flex-direction: column; padding: 64px 32px; text-align: center; background: radial-gradient(ellipse at 50% 0,var(--vp-c-brand-soft),transparent 65%); }
.placeholder-cards { position: relative; width: 84px; height: 100px; margin-bottom: 28px; }
.placeholder-cards span { position: absolute; display: flex; align-items: center; justify-content: center; width: 64px; height: 88px; border: 1px solid var(--vp-c-divider); border-radius: 8px; background: var(--vp-c-bg); color: var(--vp-c-brand-1); font-size: 28px; }
.placeholder-cards span:first-child { transform: rotate(-14deg); left: 0; top: 4px; }
.placeholder-cards span:last-child { transform: rotate(8deg); right: 0; }
.detail-kicker { color: var(--vp-c-brand-1); font-size: 10px; font-weight: 650; letter-spacing: 1.6px; }
.detail-placeholder h2 { margin: 12px 0; font-size: 23px; line-height: 1.4; }
.detail-placeholder p { max-width: 340px; color: var(--vp-c-text-2); font-size: 13px; line-height: 1.8; }
.detail-placeholder > div:last-child { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-top: 28px; }
.detail-placeholder > div:last-child span { padding: 4px 8px; border: 1px solid var(--vp-c-divider); border-radius: 5px; color: var(--vp-c-text-2); font-size: 10px; }
.visually-hidden { position: absolute; width: 1px; height: 1px; padding: 0; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }
@media (max-width: 1120px) { .catalog-workspace { gap: 16px; grid-template-columns: minmax(0,.85fr) minmax(0,1.15fr); } .card-kind { display: none; } .card-sheet-header { padding: 20px; } .catalog-filters { grid-template-columns: repeat(2,minmax(0,1fr)); } .search-field { grid-column: 1 / -1; } .count-note { display: none; } }
@media (max-width: 760px) {
  .catalog-toolbar { padding: 16px; border-radius: 12px; }
  .catalog-overview { margin-bottom: 16px; }
  .catalog-workspace { display: block; margin-top: 20px; }
  .card-detail-panel { display: none; position: static; max-height: none; overflow: visible; scrollbar-gutter: auto; border-radius: 12px; }
  .has-selection .card-detail-panel { display: block; }
  .has-selection .catalog-results { display: none; }
  .has-selection .catalog-toolbar { padding: 12px 16px; }
  .has-selection .catalog-overview { margin: 0; }
  .has-selection .catalog-toolbar :is(.format-switch, .catalog-count, .catalog-filters, .filter-options, .search-help, .language-note) { display: none; }
  .has-selection .language-select { width: 100%; max-width: none; margin: 0; }
  .card-kind { display: inline-flex; }
  .card-result { padding: 13px 12px; }
  .result-main strong { font-size: 15px; }
  .result-stats, .result-type { font-size: 12px; }
  .result-stats { gap: 5px 14px; }
  .card-sheet-header h2 { font-size: 27px; }
  .card-detail-panel { scroll-margin-top: 110px; }
  .optional-note { display: none; }
  .card-explorer input[type='search'], .card-explorer select { font-size: 16px; }
  .results-pagination { margin-bottom: 12px; }
}
@media (max-width: 400px) {
  .catalog-toolbar { padding: 12px; }
  .catalog-overview { gap: 10px; }
  .format-switch { width: 100%; }
  .format-switch button { flex: 1; padding: 8px 12px; }
  .language-select { width: 100%; max-width: none; margin: 0; }
  .catalog-count { width: 100%; text-align: center; }
  .catalog-filters { gap: 10px; }
  .catalog-filters select { padding-left: 8px; }
  .filter-options { gap: 0; }
  .text-search { font-size: 12px; }
  .card-kind { display: none; }
  .card-sheet-header { padding: 18px 16px; }
  .card-sheet-header h2 { font-size: 23px; }
  .card-stat-grid { grid-template-columns: repeat(3,minmax(0,1fr)); }
  .card-stat-grid .maximum-stat { grid-column: 1 / -1; flex-direction: row; justify-content: center; gap: 12px; }
  .card-special-stats { padding: 14px 16px 0; }
  .archetype-section { padding: 18px 16px 0; }
  .printed-text { margin: 18px 16px 0; }
  .printed-text p { font-size: 14px; }
  .card-provenance { margin: 20px 16px 10px; }
  .script-link { margin: 14px 16px; padding: 10px; }
  .technical-details { padding: 0 16px; }
  .card-explorer .no-script { margin-inline: 16px; }
  .detail-actions { padding-inline: 8px; }
  .detail-actions .quiet-button { padding-inline: 5px; font-size: 12px !important; }
  .results-pagination .secondary-button { padding-inline: 8px; }
}
@media (prefers-reduced-motion: reduce) { .card-result { transition: none; } .loading-indicator { animation: none; } }
</style>
