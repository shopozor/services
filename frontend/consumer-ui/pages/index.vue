<template>
  <div>
    <shops-map :center="center" :zoom="zoom" />
    <project-overview class="py-4" />
    <budzons class="py-4" />
    <project-roadmap class="py-4" />
  </div>
</template>

<script>
import Budzons from '~/components/ProjectDetails/Budzons'
import Map from '~/components/Map/Map'
import ProjectOverview from '~/components/ProjectDetails/ProjectOverview'
import ProjectRoadmap from '~/components/ProjectDetails/ProjectRoadmap'

export default {
  components: {
    Budzons,
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
  layout: 'default'
}
</script>
