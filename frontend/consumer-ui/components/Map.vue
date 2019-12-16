<template>
  <div>
    <client-only>
      <l-map class="mini-map" :zoom="13" :center="position">
        <!-- cf. https://sosm.ch/projects/tile-service/ -->
        <l-tile-layer url="https://tile.osm.ch/osm-swiss-style/{z}/{x}/{y}.png" />
        <shop-marker v-for="shop in shops" :key="shop.id" :shop="shop" />
      </l-map>
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
import ShopMarker from './ShopMarker'
import shops from '~graphql/shops'

export default {
  apollo: {
    shops: {
      query: shops
    }
  },
  components: {
    'shop-marker': ShopMarker,
    ClientOnly
  },
  data: () => ({
    position: [46.7716, 7.0382]
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
