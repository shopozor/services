<template>
  <div>
    <client-only>
      <l-map class="mini-map" :zoom="13" :center="position">
        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png" />
        <!-- <l-marker :lat-lng="position" :draggable="draggable">
          <l-popup :content="popupContent" />
        </l-marker> -->
      </l-map>
    </client-only>
  </div>
</template>

<script>
export default {
  data: () => ({
    position: [55.607741796855734, 13.018133640289308],
    draggable: true,
    popupContent: 'Sentian HQ'
  })
}
</script>

<style src="leaflet/dist/leaflet.css"></style>
<style>
.mini-map {
  width: 100%;
  height: 100vh !important;
}
</style>
