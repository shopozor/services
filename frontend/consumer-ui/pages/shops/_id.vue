<template>
  <div>
    <h1>{{ shop.name }}</h1>
    C'est la Budzonnerie numéro {{ shop.id }}
  </div>
</template>

<script>
import shop from '~graphql/shop'

export default {
  apollo: {
    shop: {
      query: shop,
      // TODO: what is this for exactly?
      prefetch: ({ route }) => ({ id: route.params.id }),
      variables () {
        return { shopId: this.$route.params.id }
      }
    }
  },
  head () {
    return {
      title: shop ? shop.name : 'Loading'
    }
  }
}
</script>
