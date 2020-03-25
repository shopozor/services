<template>
  <div>
    <l-map class="w-full h-3/4" :zoom="zoom" :center="center" :options="options">
      <shop-card v-if="shop" :shop="shop" class="absolute left-0 bottom-0 z-999" @close="clearDescription" />
      <l-tile-layer :url="tilesUrl" />
      <shop-marker v-for="shop in shops" :key="shop.id" :shop="shop" @display-description="displayDescription" />
    </l-map>
  </div>
</template>

<script>
import ShopCard from '~/components/Map/ShopCard'
import ShopMarker from '~/components/Map/ShopMarker'

export default {
  components: {
    ShopCard,
    ShopMarker
  },
  props: {
    center: {
      type: Array,
      required: true
    },
    shops: {
      type: Array,
      default: null
    },
    tilesUrl: {
      type: String,
      // cf. https://sosm.ch/projects/tile-service/
      default: 'https://tile.osm.ch/switzerland/{z}/{x}/{y}.png'
    },
    zoom: {
      type: Number,
      required: true
    }
  },
  data: () => ({
    shop: undefined
  }),
  computed: {
    options () {
      return {
        gestureHandling: true,
        gestureHandlingOptions: {
          text: {
            touch: this.$i18n.t('gestureHandling.touch'),
            scroll: this.$i18n.t('gestureHandling.scroll'),
            scrollMac: this.$i18n.t('gestureHandling.scrollMac')
          },
          duration: 2000
        },
        zoomControl: false
      }
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

<style src="leaflet/dist/leaflet.css"></style>
<style src="leaflet-gesture-handling/dist/leaflet-gesture-handling.css"></style>
<style>
/* .leaflet-tile-pane {
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
} */
</style>
