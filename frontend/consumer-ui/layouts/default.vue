<template>
  <div>
    <shopozor-header />
    <nuxt />
    <shopozor-footer />
  </div>
</template>

<script>
import ShopozorHeader from '~/components/Header'
import ShopozorFooter from '~/components/Footer'

export default {
  components: {
    ShopozorHeader,
    ShopozorFooter
  }
}
</script>
