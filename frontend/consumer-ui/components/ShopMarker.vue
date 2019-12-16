<template>
  <l-marker :lat-lng="position" :icon="icon">
    <l-popup>
      <shop-card :name="shop.name" :description="shop.description" />
    </l-popup>
  </l-marker>
</template>

<script>
import L from 'leaflet'
import ValidatedObjectProp from '../mixins/ValidatedObjectProp'
import ShopCard from './ShopCard'
import Marker from './marker.png'

export default {
  components: {
    'shop-card': ShopCard
  },
  mixins: [
    ValidatedObjectProp('shop',
      ['latitude', 'longitude', 'name', 'description'])//, 'image'])
  ],
  computed: {
    position () {
      return [this.shop.latitude, this.shop.longitude]
    },
    icon () {
      return L.icon({
        iconUrl: Marker
      })
    }
  }
}
</script>
