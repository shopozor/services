<template>
  <q-layout view="HHH Lpr lFf">
    <q-header>
      <q-toolbar
        color="primary"
      >
        <q-btn
          class="burger-menu"
          flat
          dense
          round
          aria-label="Menu"
          :disable="disableNavigation"
          @click="drawerOpen = !drawerOpen"
        >
          <q-icon name="menu" />
        </q-btn>

        <q-toolbar-title>
          {{ $t('shop') }} - {{ $t(subtitle) }}
        </q-toolbar-title>
        <language-select />
      </q-toolbar>
    </q-header>
    <q-drawer
      id="sideDrawer"
      v-model="drawerOpen"
      content-class="bg-sideDrawer"
    >
      <q-list>
        <q-item-label header>
          ENTER HEADER
        </q-item-label>
        <q-item clickable>
          <q-item-section>
            <q-item-label>ENTER LINK</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import LanguageSelect from '../components/I18n/LanguageSelect'

export default {
  name: 'Layout',
  components: { LanguageSelect },
  props: {
    subtitle: {
      type: String,
      required: true
    },
    disableNavigation: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      drawerOpen: this.$q.platform.is.desktop && !this.disableNavigation
    }
  }
}
</script>

<style>
</style>
