<template>
  <div style="height: 1vh">
    <!-- <client-only> -->
    <l-map :zoom="50" :center="[47.413220, -1.219482]">
      <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png" />
      <l-marker :lat-lng="[47.413220, -1.219482]" />
    </l-map>
    <!-- <input type='text'/> -->
  <!-- </client-only> -->
  </div>
</template>

<script>
export default {
  // data () { },
  // methods: { },
  // components: { }
}
</script>
