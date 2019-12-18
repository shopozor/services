<template>
  <div>
    <client-only>
      <loading :active="!shops" :can-cancel="true" :is-full-page="false" :color="spinnerColor" />
      <l-map class="w-full mini-map" :zoom="zoom" :center="center" :options="options">
        <shop-card v-if="shop" :shop="shop" class="shop-card" />
        <l-tile-layer :url="tilesUrl" />
        <shop-marker v-for="shop in shops" :key="shop.id" :shop="shop" @display-description="onDisplayDescription" />
      </l-map>
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
import Loading from 'vue-loading-overlay'
import ShopCard from '~/components/Map/ShopCard'
import ShopMarker from '~/components/Map/ShopMarker'
import shops from '~graphql/shops'

export default {
  apollo: {
    shops: {
      query: shops
    }
  },
  components: {
    ShopCard,
    ShopMarker,
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
  // TODO: test the value of the map's options!
  data: () => ({
    options: {
      gestureHandling: true,
      zoomControl: false
    },
    // TODO: test that shop is initialized with undefined
    shop: undefined,
    spinnerColor: '#e78000ff',
    // cf. https://sosm.ch/projects/tile-service/
    tilesUrl: 'https://tile.osm.ch/osm-swiss-style/{z}/{x}/{y}.png'
  }),
  methods: {
    onDisplayDescription (id) {
      this.shop = this.shops.find(item => item.id === id)
    }
  }
}
</script>

<style src="vue-loading-overlay/dist/vue-loading.css"></style>
<style src="leaflet/dist/leaflet.css"></style>
<style src="leaflet-gesture-handling/dist/leaflet-gesture-handling.css"></style>
<style>
.leaflet-tile-pane {
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
}
.shop-card {
  right: 0px;
  top: 0px;
  position: absolute;
  z-index: 999;
}
.mini-map {
  height: 75vh !important;
}
</style>
