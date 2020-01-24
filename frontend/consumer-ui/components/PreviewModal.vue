<template>
  <client-only>
    <modal name="preview-modal">
      hello, world
    </modal>
  </client-only>
</template>

<script>
import ClientOnly from 'vue-client-only'

export default {
  components: {
    ClientOnly
  }
}
</script>
