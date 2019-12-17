<template>
  <div>
    <my-header />
    <nuxt />
  </div>
</template>

<script>
import Header from '~/components/Header'

export default {
  components: {
    'my-header': Header
  }
}
</script>
