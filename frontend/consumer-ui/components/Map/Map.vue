<template>
  <div>
    <client-only>
      <loading :active="!shops" :can-cancel="true" :is-full-page="false" :color="spinnerColor" />
      <l-map class="mini-map" :zoom="zoom" :center="center" :options="options">
        <l-tile-layer :url="tilesUrl" />
        <shop-marker v-for="shop in shops" :key="shop.id" :shop="shop" />
      </l-map>
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
import Loading from 'vue-loading-overlay'
import ShopMarker from '~/components/Map/ShopMarker'
import shops from '~graphql/shops'

export default {
  apollo: {
    shops: {
      query: shops
    }
  },
  components: {
    'shop-marker': ShopMarker,
    ClientOnly,
    Loading
  },
  props: {
    center: {
      type: Array,
      required: true
    },
    zoom: {
      type: Number,
      required: true
    }
  },
  data: () => ({
    options: {
      scrollWheelZoom: false
    },
    spinnerColor: '#e78000ff',
    // cf. https://sosm.ch/projects/tile-service/
    tilesUrl: 'https://tile.osm.ch/osm-swiss-style/{z}/{x}/{y}.png'
  })
}
</script>

<style src="vue-loading-overlay/dist/vue-loading.css"></style>
<style src="leaflet/dist/leaflet.css"></style>
<style>
.mini-map {
  width: 100%;
  height: 100vh !important;
}
.leaflet-tile-pane {
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
}
</style>
