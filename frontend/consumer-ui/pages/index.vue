<template>
  <div>
    <shops-map :center="center" :zoom="zoom" />
    <project-overview class="py-4" />
    <budzons class="py-4" />
  </div>
</template>

<script>
import Budzons from '~/components/ProjectDetails/Budzons'
import Map from '~/components/Map/Map'
import ProjectOverview from '~/components/ProjectDetails/ProjectOverview'

export default {
  components: {
    Budzons,
    'shops-map': Map,
    ProjectOverview
  },
  data: () => ({
    center: [46.718852, 7.097669],
    zoom: 11
  }),
  head: {
    title: 'La Budzonnerie'
  },
  layout: 'default'
}
</script>
