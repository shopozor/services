<template>
  <div>
    <client-only>
      <loading class="z-999" :active="loadingMapData" :can-cancel="true" :is-full-page="false" :color="spinnerColor" />
      <l-map class="w-full fill-partial-height" :zoom="zoom" :center="center" :options="options" @click="clearDescription">
        <shop-card v-if="shop" :shop="shop" class="absolute left-0 bottom-0 z-999" />
        <l-tile-layer :url="tilesUrl" />
        <shop-marker v-for="shop in shops" :key="shop.id" :shop="shop" @display-description="displayDescription" />
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
    },
    tilesUrl: {
      type: String,
      // cf. https://sosm.ch/projects/tile-service/
      default: 'https://tile.osm.ch/switzerland/{z}/{x}/{y}.png'
    }
  },
  data: () => ({
    options: {
      gestureHandling: true,
      gestureHandlingOptions: {
        // TODO: put the following text in a file for the sake of translations
        text: {
          touch: 'Utiliser 2 doigts pour bouger la carte',
          scroll: 'CTRL + scroll pour zoomer',
          scrollMac: '\u2318 + scroll pour zoomer'
        },
        duration: 2000
      },
      zoomControl: false
    },
    shop: undefined,
    spinnerColor: '#e78000ff'
  }),
  computed: {
    loadingMapData () {
      return this.$apollo.queries.shops.loading
    }
  },
  methods: {
    displayDescription (id) {
      this.shop = this.shops.find(item => item.id === id)
    },
    clearDescription () {
      this.shop = undefined
    }
  }
}
</script>

<style src="vue-loading-overlay/dist/vue-loading.css"></style>
<style src="leaflet/dist/leaflet.css"></style>
<style src="leaflet-gesture-handling/dist/leaflet-gesture-handling.css"></style>
<style>
/* .leaflet-tile-pane {
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
} */
/* TODO: add the following utilities to tailwindcss */
.z-999 {
  z-index: 999;
}
.fill-partial-height {
  height: 75vh !important;
}
</style>
