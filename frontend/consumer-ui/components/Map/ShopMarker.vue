<template>
  <l-marker :lat-lng="position" :icon="icon" @click="onClick" />
</template>

<script>
import Marker from '~/assets/img/marker.png'
import ValidatedObjectProp from '~/mixins/ValidatedObjectProp'

export default {
  mixins: [
    ValidatedObjectProp('shop',
      ['description', 'id', 'latitude', 'longitude', 'name'])//, 'image']) + address
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
  },
  methods: {
    onClick () {
      this.$emit('display-description', this.shop.id)
    }
  }
}
</script>
