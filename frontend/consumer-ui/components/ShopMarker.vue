<template>
  <l-marker :lat-lng="position">
    <l-popup>
      <shop-card :name="shop.name" :description="shop.description" />
    </l-popup>
  </l-marker>
</template>

<script>
import ValidatedObjectProp from '../mixins/ValidatedObjectProp'
import ShopCard from './ShopCard'

export default {
  components: {
    'shop-card': ShopCard
  },
  data: () => ({
    popupContent: 'trouduc'
  }),
  computed: {
    position () {
      return [this.shop.latitude, this.shop.longitude]
    }
  },
  mixins: [
    ValidatedObjectProp('shop',
      ['latitude', 'longitude', 'name', 'description'])//, 'image'])
  ]
}
</script>
