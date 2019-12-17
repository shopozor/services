<template>
  <div>
    <shops-map :center="center" :zoom="zoom" />
  </div>
</template>

<script>
import Map from '~/components/Map'

export default {
  components: {
    'shops-map': Map
  },
  data: () => ({
    center: [46.718852, 7.097669],
    zoom: 11
  }),
  head: {
    title: 'La Budzonnerie'
  }
}
</script>
