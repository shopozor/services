<template>
  <l-marker :lat-lng="position" :icon="icon">
    <l-popup>
      <shop-card :name="shop.name" :description="shop.description" />
    </l-popup>
  </l-marker>
</template>

<script>
import Marker from '~/assets/img/marker.png'
import ValidatedObjectProp from '~/mixins/ValidatedObjectProp'
import ShopCard from '~/components/Map/ShopCard'

export default {
  components: {
    'shop-card': ShopCard
  },
  mixins: [
    ValidatedObjectProp('shop',
      ['latitude', 'longitude', 'name', 'description'])//, 'image']) + address
  ],
  computed: {
    position () {
      return [this.shop.latitude, this.shop.longitude]
    },
    icon () {
      // if we don't disable the following eslint error,
      // then we need to import { L } from 'leaflet'
      // which must not be done on the server-side and is more
      // difficult to setup as just disabling the eslint error
      // eslint-disable-next-line no-undef
      return L.icon({
        iconUrl: Marker
      })
    }
  }
}
</script>
