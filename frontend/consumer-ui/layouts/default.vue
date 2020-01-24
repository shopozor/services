<template>
  <div>
    <preview-modal />
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
    PreviewModal,
    ShopozorHeader,
    ShopozorFooter
  },
  mounted () {
    this.$nextTick(function () {
      this.$modal.show('preview-modal')
    })
  }
}
</script>
