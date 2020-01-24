<template>
  <div>
    <client-only>
      <modal name="hello-world">
        hello, world
      </modal>
    </client-only>
    <shopozor-header />
    <nuxt />
    <shopozor-footer />
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'
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
      this.$modal.show('hello-world')
    })
  }
}
</script>
