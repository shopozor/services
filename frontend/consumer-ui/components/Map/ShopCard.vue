<template>
  <div>
    <h1 class="font-extrabold">
      {{ name }}
    </h1>
    {{ description }}
    <!-- TODO: put an image -->
    <!-- TODO: put an address / GPS coordinates -->
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
    // TODO: id is missing
  }
}
</script>

<!-- style src="leaflet/dist/leaflet.css"></style-->
<style src="~/assets/css/tailwind.css"></style>
