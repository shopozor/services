<template>
  <div class="w-1/4 h-full justify-between flex flex-col bg-white">
    <!-- TODO: we need to put both the url (background-image) and the alt (title) here! -->
    <div
      class="h-64 w-full bg-cover"
      style="background-image: url('https://www.bulledeculture.ch/event_img/5d5fb1d4cf93d699209171.jpg')"
      title="Shop description"
    />
    <div class="mb-8 px-4">
      <div class="text-black font-bold text-xl mb-2">
        {{ shop.name }}
      </div>
      <p class="text-grey-darker text-base">
        {{ shop.description }}
      </p>
    </div>
    <div class="flex items-center px-4">
      <img class="mr-4" src="../../assets/img/marker.png" alt="GPS coordinates">
      <div class="text-sm italic">
        {{ gpsCoordinates }}
      </div>
    </div>
  </div>
</template>

  <!-- TODO: put an image -->
  <!-- TODO: put an address / GPS coordinates -->

<script>
import ValidatedObjectProp from '~/mixins/ValidatedObjectProp'

export default {
  mixins: [
    ValidatedObjectProp('shop',
      ['latitude', 'longitude', 'name', 'description'])//, 'image']) + address + id
  ],
  computed: {
    gpsCoordinates () {
      return `${this.shop.latitude}, ${this.shop.longitude}`
    }
  }
}
</script>

<style src="~/assets/css/tailwind.css"></style>
