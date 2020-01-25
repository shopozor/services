<template>
  <div>
    <shopozor-header />
    <nuxt />
    <shopozor-footer />
  </div>
</template>

<script>
import PreviewModal from '~/components/PreviewModal'
import ShopozorHeader from '~/components/Header'
import ShopozorFooter from '~/components/Footer'

export default {
  components: {
    ShopozorHeader,
    ShopozorFooter
  },
  mounted () {
    this.$nextTick(function () {
      this.$modal.show(
        PreviewModal,
        {},
        {
          // height: '80%'
          scrollable: true
        }
      )
    })
  }
}
</script>
