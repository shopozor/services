<template>
  <div>
    <client-only>
      <l-map class="mini-map" :zoom="13" :center="position">
        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png" />
        <shop-marker v-for="shop in shops" :key="shop.id" :shop="shop" />
      </l-map>
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
import gql from 'graphql-tag'
import ShopMarker from './ShopMarker'
// TODO: is it possible to use a shortcut like ~/shared/graphql?
// import shops from '../../../shared/graphql/shops'
// import author from '../apollo/queries/fetchAuthor.gql'

const shopsQuery = gql`
  query Shops {
    shops {
      description
      latitude
      longitude
      id
      name
    }
  }
`

export default {
  apollo: {
    shops: {
      query: shopsQuery
    }
  },
  components: {
    'shop-marker': ShopMarker,
    ClientOnly
  },
  data: () => ({
    position: [46.775406, 7.037900]
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
