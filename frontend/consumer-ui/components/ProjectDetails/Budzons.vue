<template>
  <div>
    <h2 class="overview-title">
      {{ $t('budzons.title') }}
    </h2>
    <div class="p-6 text-justify">
      <span v-html="$t('budzons.description')" />
    </div>
    <img class="w-1/2 rounded-full mx-auto lg:max-w-lg" :src="budzons">
  </div>
</template>
<script>
import BudzonsImg from '~/assets/img/budzons.jpg'

export default {
  data: () => ({
    budzons: BudzonsImg
  })
}
</script>
