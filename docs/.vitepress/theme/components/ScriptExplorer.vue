<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { withBase } from 'vitepress';

type SearchMode = 'all' | 'cards' | 'functions';

type ScriptRecord = {
  id: number;
  name: string;
  script: string;
  api_calls: string[];
  script_length: number;
  desc_length: number;
};

const resultLimit = 200;
const query = ref('');
const mode = ref<SearchMode>('all');
const loading = ref(true);
const error = ref('');
const records = ref<ScriptRecord[]>([]);
const featuredIds = ref(new Set<number>());

onMounted(async () => {
  try {
    const [cardsResponse, featuredResponse] = await Promise.all([
      fetch(withBase('/data/card-examples.json')),
      fetch(withBase('/data/featured-card-ids.json')),
    ]);
    if (!cardsResponse.ok) {
      throw new Error(`${cardsResponse.status} ${cardsResponse.statusText}`);
    }
    if (!featuredResponse.ok) {
      throw new Error(`${featuredResponse.status} ${featuredResponse.statusText}`);
    }

    records.value = await cardsResponse.json();
    const ids: number[] = await featuredResponse.json();
    featuredIds.value = new Set(ids.map(Number));
  } catch (err) {
    error.value = err instanceof Error ? err.message : String(err);
  } finally {
    loading.value = false;
  }
});

const normalizedQuery = computed(() => query.value.trim().toLowerCase());
const tokens = computed(() => normalizedQuery.value.split(/\s+/).filter(Boolean));

const functionCounts = computed(() => {
  const counts = new Map<string, number>();
  for (const record of records.value) {
    for (const name of record.api_calls || []) {
      counts.set(name, (counts.get(name) || 0) + 1);
    }
  }
  return Array.from(counts, ([name, count]) => ({ name, count })).sort(
    (a, b) => b.count - a.count || a.name.localeCompare(b.name),
  );
});

const matchedFunctions = computed(() => {
  const q = normalizedQuery.value;
  const list = q
    ? functionCounts.value.filter((entry) => entry.name.toLowerCase().includes(q))
    : functionCounts.value;
  return list.slice(0, q ? 60 : 30);
});

const featuredCount = computed(() => featuredIds.value.size);
const totalApiCalls = computed(() =>
  records.value.reduce((sum, record) => sum + (record.api_calls?.length || 0), 0),
);

const filteredRecords = computed(() => {
  if (!tokens.value.length) {
    return mode.value === 'functions'
      ? records.value.filter((record) => (record.api_calls?.length || 0) > 0)
      : records.value;
  }

  return records.value.filter((record) =>
    tokens.value.every((token) => recordMatchesToken(record, token)),
  );
});

const results = computed(() => {
  const q = normalizedQuery.value;
  return [...filteredRecords.value]
    .sort((a, b) => recordScore(b, q) - recordScore(a, q) || a.name.localeCompare(b.name))
    .slice(0, resultLimit);
});

function setMode(nextMode: SearchMode) {
  mode.value = nextMode;
}

function searchFunction(name: string) {
  query.value = name;
  mode.value = 'functions';
}

function recordMatchesToken(record: ScriptRecord, token: string) {
  const cardHaystack = `${record.id} ${record.name} ${record.script}`.toLowerCase();
  const functionHaystack = (record.api_calls || []).join(' ').toLowerCase();

  if (mode.value === 'cards') {
    return cardHaystack.includes(token);
  }
  if (mode.value === 'functions') {
    return functionHaystack.includes(token);
  }
  return cardHaystack.includes(token) || functionHaystack.includes(token);
}

function recordScore(record: ScriptRecord, q: string) {
  if (!q) {
    return record.api_calls?.length || 0;
  }

  const exactFunction = (record.api_calls || []).some((name) => name.toLowerCase() === q);
  const exactId = String(record.id) === q;
  const exactName = record.name.toLowerCase() === q;
  const nameStarts = record.name.toLowerCase().startsWith(q);

  return (
    (exactId ? 8000 : 0) +
    (exactName ? 6000 : 0) +
    (nameStarts ? 3000 : 0) +
    (exactFunction ? 5000 : 0) +
    (isFeatured(record) ? 80 : 0) +
    (record.api_calls?.length || 0)
  );
}

function visibleCalls(record: ScriptRecord) {
  const calls = record.api_calls || [];
  const q = normalizedQuery.value;
  const directMatches = q ? calls.filter((name) => name.toLowerCase().includes(q)) : calls;
  return (directMatches.length ? directMatches : calls).slice(0, 10);
}

function hiddenCallCount(record: ScriptRecord) {
  return Math.max(0, (record.api_calls?.length || 0) - visibleCalls(record).length);
}

function apiHref(name: string) {
  const index = name.lastIndexOf('.');
  if (index === -1) {
    return withBase('/api/functions/');
  }
  const namespace = safeSegment(name.slice(0, index));
  const short = safeSegment(name.slice(index + 1));
  return withBase(`/api/functions/${namespace}/${short}`);
}

function isFeatured(record: ScriptRecord) {
  return featuredIds.value.has(Number(record.id));
}

function cardHref(record: ScriptRecord) {
  return withBase(`/examples/cards/${record.id}`);
}

function scriptHref(record: ScriptRecord) {
  return `https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/${record.script}`;
}

function safeSegment(value: string) {
  return value.replace(/[^A-Za-z0-9_.-]+/g, '_');
}
</script>

<template>
  <div class="script-explorer">
    <div class="explorer-toolbar">
      <label class="explorer-search">
        <span>Search scripts</span>
        <input
          v-model="query"
          type="search"
          placeholder="Card name, 62091148, Duel.SpecialSummon, IsSetCard"
        />
      </label>

      <div class="explorer-modes" aria-label="Search mode">
        <button type="button" :class="{ active: mode === 'all' }" @click="setMode('all')">All</button>
        <button type="button" :class="{ active: mode === 'cards' }" @click="setMode('cards')">Cards</button>
        <button type="button" :class="{ active: mode === 'functions' }" @click="setMode('functions')">Functions</button>
      </div>
    </div>

    <p v-if="loading" class="explorer-state">Loading script index...</p>
    <p v-else-if="error" class="explorer-state">Could not load the script index: {{ error }}</p>

    <template v-else>
      <div class="explorer-stats" aria-label="Script index statistics">
        <div>
          <strong>{{ records.length.toLocaleString() }}</strong>
          <span>scripts indexed</span>
        </div>
        <div>
          <strong>{{ functionCounts.length.toLocaleString() }}</strong>
          <span>functions detected</span>
        </div>
        <div>
          <strong>{{ totalApiCalls.toLocaleString() }}</strong>
          <span>script/function links</span>
        </div>
        <div>
          <strong>{{ featuredCount.toLocaleString() }}</strong>
          <span>featured pages</span>
        </div>
      </div>

      <section class="explorer-section" aria-labelledby="function-matches-heading">
        <div class="explorer-section-head">
          <h2 id="function-matches-heading">Function Matches</h2>
          <span>{{ matchedFunctions.length.toLocaleString() }} shown</span>
        </div>
        <div class="function-chip-list">
          <button
            v-for="entry in matchedFunctions"
            :key="entry.name"
            class="api-chip button-chip"
            type="button"
            @click="searchFunction(entry.name)"
          >
            <span>{{ entry.name }}</span>
            <small>{{ entry.count.toLocaleString() }}</small>
          </button>
        </div>
      </section>

      <section class="explorer-section" aria-labelledby="cards-heading">
        <div class="explorer-section-head">
          <h2 id="cards-heading">Cards</h2>
          <span>
            Showing {{ results.length.toLocaleString() }} of
            {{ filteredRecords.length.toLocaleString() }} matches
          </span>
        </div>

        <div class="explorer-results">
          <article v-for="record in results" :key="record.id" class="explorer-result">
            <div class="result-main">
              <a v-if="isFeatured(record)" :href="cardHref(record)">{{ record.name }}</a>
              <strong v-else>{{ record.name }}</strong>
              <code>{{ record.id }}</code>
            </div>

            <div class="result-meta">
              <span>{{ record.script }}</span>
              <span>{{ (record.api_calls?.length || 0).toLocaleString() }} detected calls</span>
              <span>{{ record.script_length.toLocaleString() }} script chars</span>
            </div>

            <div class="result-links">
              <a :href="scriptHref(record)" target="_blank" rel="noreferrer">Script</a>
              <a v-if="isFeatured(record)" :href="cardHref(record)">Example page</a>
            </div>

            <div class="matched-call-list" v-if="record.api_calls?.length">
              <a v-for="name in visibleCalls(record)" :key="name" class="api-chip" :href="apiHref(name)">
                {{ name }}
              </a>
              <span v-if="hiddenCallCount(record)" class="more-chip">
                +{{ hiddenCallCount(record).toLocaleString() }} more
              </span>
            </div>
          </article>
        </div>
      </section>
    </template>
  </div>
</template>
