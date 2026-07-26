<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { withBase } from 'vitepress';

type SearchMode = 'all' | 'cards' | 'text' | 'code';

type ScriptRecord = {
  id: number;
  name: string;
  script: string;
  desc?: string;
  card_type_labels?: string[];
  category_labels?: string[];
  api_calls: string[];
  script_constants?: string[];
  script_length: number;
  desc_length: number;
};

const resultLimit = 200;
const query = ref('');
const mode = ref<SearchMode>('all');
const typeFilter = ref('all');
const categoryFilter = ref('all');
const featuredOnly = ref(false);
const loading = ref(true);
const error = ref('');
const records = ref<ScriptRecord[]>([]);
const featuredIds = ref(new Set<number>());

onMounted(async () => {
  try {
    const [cardsResponse, featuredResponse, constantsResponse] = await Promise.all([
      fetch(withBase('/data/card-examples.json')),
      fetch(withBase('/data/featured-card-ids.json')),
      fetch(withBase('/data/constant-usage.json')),
    ]);
    if (!cardsResponse.ok) {
      throw new Error(`${cardsResponse.status} ${cardsResponse.statusText}`);
    }
    if (!featuredResponse.ok) {
      throw new Error(`${featuredResponse.status} ${featuredResponse.statusText}`);
    }
    if (!constantsResponse.ok) {
      throw new Error(`${constantsResponse.status} ${constantsResponse.statusText}`);
    }

    const loadedRecords: ScriptRecord[] = await cardsResponse.json();
    const recordsById = new Map(loadedRecords.map((record) => [Number(record.id), record]));
    const constantUsage: Record<string, number[]> = await constantsResponse.json();
    for (const [name, ids] of Object.entries(constantUsage)) {
      for (const id of ids) {
        const record = recordsById.get(Number(id));
        if (record) {
          (record.script_constants ||= []).push(name);
        }
      }
    }
    records.value = loadedRecords;
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

const constantCounts = computed(() => {
  const counts = new Map<string, number>();
  for (const record of records.value) {
    for (const name of record.script_constants || []) {
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

const matchedConstants = computed(() => {
  const q = normalizedQuery.value;
  if (!q) {
    return [];
  }
  return constantCounts.value
    .filter((entry) => entry.name.toLowerCase().includes(q))
    .slice(0, 60);
});

const featuredCount = computed(() => featuredIds.value.size);
const totalApiCalls = computed(() =>
  records.value.reduce((sum, record) => sum + (record.api_calls?.length || 0), 0),
);

const typeOptions = computed(() => buildOptionCounts((record) => record.card_type_labels || []));
const categoryOptions = computed(() => buildOptionCounts((record) => record.category_labels || []));
const hasActiveFilters = computed(
  () => typeFilter.value !== 'all' || categoryFilter.value !== 'all' || featuredOnly.value,
);

const filteredRecords = computed(() => {
  return records.value.filter((record) => {
    if (featuredOnly.value && !isFeatured(record)) {
      return false;
    }
    if (typeFilter.value !== 'all' && !(record.card_type_labels || []).includes(typeFilter.value)) {
      return false;
    }
    if (categoryFilter.value !== 'all' && !(record.category_labels || []).includes(categoryFilter.value)) {
      return false;
    }
    if (
      mode.value === 'code'
      && !tokens.value.length
      && !(record.api_calls?.length || record.script_constants?.length || 0)
    ) {
      return false;
    }
    return !tokens.value.length || tokens.value.every((token) => recordMatchesToken(record, token));
  });
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
  mode.value = 'code';
}

function searchConstant(name: string) {
  query.value = name;
  mode.value = 'code';
}

function setTypeFilter(label: string) {
  typeFilter.value = label;
}

function setCategoryFilter(label: string) {
  categoryFilter.value = label;
}

function clearFilters() {
  typeFilter.value = 'all';
  categoryFilter.value = 'all';
  featuredOnly.value = false;
}

function recordMatchesToken(record: ScriptRecord, token: string) {
  const cardHaystack = [
    record.id,
    record.name,
    record.script,
    ...(record.card_type_labels || []),
    ...(record.category_labels || []),
  ]
    .join(' ')
    .toLowerCase();
  const textHaystack = (record.desc || '').toLowerCase();
  const functionHaystack = (record.api_calls || []).join(' ').toLowerCase();
  const constantHaystack = (record.script_constants || []).join(' ').toLowerCase();

  if (mode.value === 'cards') {
    return cardHaystack.includes(token);
  }
  if (mode.value === 'text') {
    return textHaystack.includes(token);
  }
  if (mode.value === 'code') {
    return functionHaystack.includes(token) || constantHaystack.includes(token);
  }
  return (
    cardHaystack.includes(token)
    || textHaystack.includes(token)
    || functionHaystack.includes(token)
    || constantHaystack.includes(token)
  );
}

function recordScore(record: ScriptRecord, q: string) {
  if (!q) {
    return record.api_calls?.length || 0;
  }

  const exactFunction = (record.api_calls || []).some((name) => name.toLowerCase() === q);
  const exactConstant = (record.script_constants || []).some((name) => name.toLowerCase() === q);
  const exactId = String(record.id) === q;
  const exactName = record.name.toLowerCase() === q;
  const nameStarts = record.name.toLowerCase().startsWith(q);
  const textMatch = q && (record.desc || '').toLowerCase().includes(q);
  const typeMatch = (record.card_type_labels || []).some((label) => label.toLowerCase() === q);
  const categoryMatch = (record.category_labels || []).some((label) => label.toLowerCase() === q);

  return (
    (exactId ? 8000 : 0) +
    (exactName ? 6000 : 0) +
    (nameStarts ? 3000 : 0) +
    (exactFunction ? 5000 : 0) +
    (exactConstant ? 4500 : 0) +
    (categoryMatch ? 1800 : 0) +
    (typeMatch ? 1200 : 0) +
    (textMatch ? 500 : 0) +
    (isFeatured(record) ? 80 : 0) +
    (record.api_calls?.length || 0)
  );
}

function matchingConstants(record: ScriptRecord) {
  const q = normalizedQuery.value;
  if (!q) {
    return [];
  }
  return (record.script_constants || []).filter((name) => name.toLowerCase().includes(q));
}

function visibleConstants(record: ScriptRecord) {
  return matchingConstants(record).slice(0, 10);
}

function hiddenConstantCount(record: ScriptRecord) {
  return Math.max(0, matchingConstants(record).length - visibleConstants(record).length);
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

function visibleTags(values: string[] | undefined, limit = 6) {
  return (values || []).slice(0, limit);
}

function textSnippet(record: ScriptRecord) {
  const text = (record.desc || '').replace(/\s+/g, ' ').trim();
  if (!text) {
    return '';
  }
  const q = normalizedQuery.value;
  if (!q) {
    return truncateText(text, 220);
  }
  const index = text.toLowerCase().indexOf(q);
  if (index === -1) {
    return truncateText(text, 220);
  }
  const start = Math.max(0, index - 80);
  const end = Math.min(text.length, index + q.length + 140);
  const prefix = start > 0 ? '...' : '';
  const suffix = end < text.length ? '...' : '';
  return `${prefix}${text.slice(start, end)}${suffix}`;
}

function truncateText(text: string, limit: number) {
  if (text.length <= limit) {
    return text;
  }
  return `${text.slice(0, limit).trim()}...`;
}

function buildOptionCounts(getLabels: (record: ScriptRecord) => string[]) {
  const counts = new Map<string, number>();
  for (const record of records.value) {
    for (const label of getLabels(record)) {
      counts.set(label, (counts.get(label) || 0) + 1);
    }
  }
  return Array.from(counts, ([label, count]) => ({ label, count })).sort(
    (a, b) => b.count - a.count || a.label.localeCompare(b.label),
  );
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
          placeholder="Card name, text, 62091148, Duel.SpecialSummon, EVENT_ADJUST"
        />
      </label>

      <div class="explorer-modes" aria-label="Search mode">
        <button type="button" :class="{ active: mode === 'all' }" @click="setMode('all')">All</button>
        <button type="button" :class="{ active: mode === 'cards' }" @click="setMode('cards')">Cards</button>
        <button type="button" :class="{ active: mode === 'text' }" @click="setMode('text')">Text</button>
        <button type="button" :class="{ active: mode === 'code' }" @click="setMode('code')">Code</button>
      </div>
    </div>

    <div class="explorer-filters" aria-label="Script filters">
      <label>
        <span>Card type</span>
        <select v-model="typeFilter">
          <option value="all">All card types</option>
          <option v-for="option in typeOptions" :key="option.label" :value="option.label">
            {{ option.label }} ({{ option.count.toLocaleString() }})
          </option>
        </select>
      </label>

      <label>
        <span>Category</span>
        <select v-model="categoryFilter">
          <option value="all">All categories</option>
          <option v-for="option in categoryOptions" :key="option.label" :value="option.label">
            {{ option.label }} ({{ option.count.toLocaleString() }})
          </option>
        </select>
      </label>

      <label class="explorer-check">
        <input v-model="featuredOnly" type="checkbox" />
        <span>Featured pages only</span>
      </label>

      <button v-if="hasActiveFilters" class="filter-clear" type="button" @click="clearFilters">
        Clear filters
      </button>
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
          <strong>{{ constantCounts.length.toLocaleString() }}</strong>
          <span>constants detected</span>
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

      <section
        v-if="matchedFunctions.length"
        class="explorer-section"
        aria-labelledby="function-matches-heading"
      >
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

      <section
        v-if="matchedConstants.length"
        class="explorer-section"
        aria-labelledby="constant-matches-heading"
      >
        <div class="explorer-section-head">
          <h2 id="constant-matches-heading">Constant Matches</h2>
          <span>{{ matchedConstants.length.toLocaleString() }} shown</span>
        </div>
        <div class="function-chip-list">
          <button
            v-for="entry in matchedConstants"
            :key="entry.name"
            class="api-chip button-chip"
            type="button"
            @click="searchConstant(entry.name)"
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
              <span v-if="record.desc_length">{{ record.desc_length.toLocaleString() }} text chars</span>
            </div>

            <div class="result-tags" v-if="record.card_type_labels?.length || record.category_labels?.length">
              <button
                v-for="label in visibleTags(record.card_type_labels, 5)"
                :key="`type-${record.id}-${label}`"
                class="tag-chip type-tag"
                type="button"
                @click="setTypeFilter(label)"
              >
                {{ label }}
              </button>
              <button
                v-for="label in visibleTags(record.category_labels, 7)"
                :key="`category-${record.id}-${label}`"
                class="tag-chip category-tag"
                type="button"
                @click="setCategoryFilter(label)"
              >
                {{ label }}
              </button>
            </div>

            <p v-if="textSnippet(record)" class="result-text">
              {{ textSnippet(record) }}
            </p>

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

            <div class="matched-call-list" v-if="visibleConstants(record).length">
              <button
                v-for="name in visibleConstants(record)"
                :key="name"
                class="api-chip button-chip"
                type="button"
                @click="searchConstant(name)"
              >
                {{ name }}
              </button>
              <span v-if="hiddenConstantCount(record)" class="more-chip">
                +{{ hiddenConstantCount(record).toLocaleString() }} more matching constants
              </span>
            </div>
          </article>
        </div>
      </section>
    </template>
  </div>
</template>
