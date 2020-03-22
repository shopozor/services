<template>
  <div class="locale-changer">
    <q-select v-model="$i18n.locale" :options="['fr', 'en'] " dark />
  </div>
</template>

<script>
export default {
  name: 'LanguageSelect'
}
</script>
