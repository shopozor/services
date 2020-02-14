<template>
  <div class="flex bg-white justify-between w-full h-64 flex-row md:w-64 md:h-full md:flex-col">
    <div id="close-shop-card" class="absolute top-0 left-0 text-black font-extrabold m-2 cursor-pointer" @click="onClose">
      &#10008;
    </div>
    <div class="p-4">
      <div class="mb-8">
        <div id="shop-name" class="text-black font-bold text-xl mb-2">
          <nuxt-link :to="{name: 'shops-id___fr', params: {id: shop.id}}">
            {{ shop.name }}
          </nuxt-link>
        </div>
        <p id="shop-description" class="text-grey-darker text-base">
          {{ shop.description }}
        </p>
      </div>
      <div class="flex items-center">
        <img class="mr-4" :src="markerImgUrl" alt="GPS coordinates">
        <div class="text-sm italic">
          {{ gpsCoordinates }}
        </div>
      </div>
    </div>
    <div
      id="shop-img"
      class="h-auto w-48 md:h-64 md:w-full bg-cover"
      :style="{ backgroundImage: 'url(' + assetUrl(shop.image.url) + ')' }"
      :title="shop.image.alt"
    />
  </div>
</template>

<script>
import AssetUrl from '~/mixins/AssetUrl'
import ValidatedObjectProp from '~/mixins/ValidatedObjectProp'
import MarkerImg from '~/assets/img/marker.png'

export default {
  mixins: [
    AssetUrl,
    ValidatedObjectProp('shop',
      ['description', 'id', 'image', 'latitude', 'longitude', 'name'])// + address
  ],
  data () {
    return {
      // without this hack, storybook doesn't seem to understand how to get the marker image from the assets location!
      markerImgUrl: MarkerImg
    }
  },
  computed: {
    gpsCoordinates () {
      return `${this.shop.latitude}, ${this.shop.longitude}`
    }
  },
  methods: {
    onClose () {
      this.$emit('close')
    }
  }
}
</script>
