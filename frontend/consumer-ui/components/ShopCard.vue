<template>
  <div>
    <h1>{{ name }}</h1>
    {{ description }}
    <!-- TODO: put an image -->
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    }
  }
}
</script>
