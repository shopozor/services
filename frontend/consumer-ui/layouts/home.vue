<template>
  <div>
    <client-only>
      <shopozor-header />
      <nuxt />
      <shopozor-footer />
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
import PreviewModal from '~/components/PreviewModal'
import ShopozorHeader from '~/components/Header'
import ShopozorFooter from '~/components/Footer'

export default {
  components: {
    ClientOnly,
    ShopozorHeader,
    ShopozorFooter
  },
  mounted () {
    this.$nextTick(function () {
      this.$modal.show(
        PreviewModal,
        {},
        {
          scrollable: true
        }
      )
    })
  }
}
</script>
