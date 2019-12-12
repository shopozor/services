<template>
  <div>
    <client-only>
      <l-map class="mini-map" :zoom="13" :center="position">
        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png" />
        <!-- TODO: we need to loop over the shops here! -->
        <shop-marker :shop="shop" />
      </l-map>
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
import ShopMarker from './ShopMarker'

export default {
  components: {
    'shop-marker': ShopMarker,
    ClientOnly
  },
  data: () => ({
    position: [46.775406, 7.037900],
    shop: {
      latitude: 46.775406,
      longitude: 7.037900,
      name: 'Budzonnerie d\'Onnens',
      description: 'blablabli blablabla'
    }
  })
}
</script>

<style src="leaflet/dist/leaflet.css"></style>
<style>
.mini-map {
  width: 100%;
  height: 100vh !important;
}
</style>
