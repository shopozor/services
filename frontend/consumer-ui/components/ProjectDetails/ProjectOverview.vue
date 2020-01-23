<template>
  <div>
    <h2 class="overview-title">
      {{ $t('concept') }}
    </h2>
    <div class="p-6 text-justify">
      <span v-html="description" />
    </div>
  </div>
</template>

<script>
import overview from '~graphql/projectOverview'
export default {
  apollo: {
    sites: {
      query: overview
    }
  },
  computed: {
    description () {
      return this.sites ? this.sites[0].description : ''
    }
  }
}
</script>
