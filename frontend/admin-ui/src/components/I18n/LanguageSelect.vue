<template>
  <div class="locale-changer">
    <q-select v-model="$i18n.locale" :options="['fr', 'en'] " :for="id" dark />
  </div>
</template>

<script>
export default {
  name: 'LanguageSelect',
  props: {
    id: {
      type: String,
      default: () => null
    }
  }
}
</script>
