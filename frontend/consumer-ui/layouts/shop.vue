<template>
  <div>
    <client-only>
      <nuxt />
    </client-only>
  </div>
</template>

<script>
import ClientOnly from 'vue-client-only'

export default {
  components: {
    ClientOnly
  }
}
</script>
