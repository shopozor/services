<template>
  <div>
    <h2 class="overview-title">
      {{ $t('concept.title') }}
    </h2>
    <div class="p-6 text-justify">
      <span v-html="$t('concept.description')" />
    </div>
  </div>
</template>
