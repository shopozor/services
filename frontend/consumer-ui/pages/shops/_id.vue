<template>
  <div v-if="shop">
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
      variables () {
        return { shopId: this.$route.params.id }
      },
      update: data => data.shops_by_pk
    }
  },
  head () {
    return {
      title: this.$i18n.t('budzonnerie')
    }
  },
  validate ({ params }) {
    // shop id must be a number
    return /^\d+$/.test(params.id)
  }
}
</script>
