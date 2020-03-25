<template>
  <div>
    <client-only>
      <shops-map :center="center" :shops="shops" :zoom="zoom" />
      <project-overview class="py-4" />
      <budzons class="py-4" />
      <project-roadmap class="py-4" />
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
import Budzons from '~/components/ProjectDetails/Budzons'
import Map from '~/components/Map/Map'
import ProjectOverview from '~/components/ProjectDetails/ProjectOverview'
import ProjectRoadmap from '~/components/ProjectDetails/ProjectRoadmap'

import shops from '~graphql/shops'

export default {
  apollo: {
    shops: {
      prefetch: true,
      query: shops
    }
  },
  components: {
    Budzons,
    ClientOnly,
    'shops-map': Map,
    ProjectOverview,
    ProjectRoadmap
  },
  data: () => ({
    center: [46.718852, 7.097669],
    zoom: 11
  }),
  head () {
    return {
      title: this.$i18n.t('budzonnerie')
    }
  },
  layout: 'home'
}
</script>
