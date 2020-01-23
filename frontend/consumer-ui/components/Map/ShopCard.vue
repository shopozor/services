<template>
  <div class="flex bg-white justify-between w-full h-64 flex-row md:w-64 md:h-full md:flex-col">
    <!-- TODO: we need to put both the url (background-image) and the alt (title) here! -->
    <div
      class="h-auto w-48 md:h-64 md:w-full bg-cover"
      style="background-image: url('https://www.bulledeculture.ch/event_img/5d5fb1d4cf93d699209171.jpg')"
      title="Shop description"
    />
    <div class="p-4">
      <div class="mb-8">
        <div class="text-black font-bold text-xl mb-2">
          {{ shop.name }}
        </div>
        <p class="text-grey-darker text-base">
          {{ shop.description }}
        </p>
      </div>
      <div class="flex items-center">
        <img class="mr-4" :src="~assets/img/marker.png" alt="GPS coordinates">
        <div class="text-sm italic">
          {{ gpsCoordinates }}
        </div>
      </div>
    </div>
  </div>
</template>

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
