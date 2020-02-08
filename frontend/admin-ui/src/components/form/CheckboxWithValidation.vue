<template>
  <q-item>
    <q-item-section side>
      <q-btn
        round
        flat
        size="1em"
        icon="help"
        color="primary"
        @click="toggleDialog"
      />
    </q-item-section>

    <q-item-section>
      <q-checkbox
        id="acceptCookies"
        :value="value"
        :label="label"
        @input="input"
      />
    </q-item-section>

    <q-item-section side>
      <validity-icon
        :know-error="!value || !mandatory"
        :show-error="!value && touched && mandatory"
        :mandatory="mandatory"
      />
    </q-item-section>

    <q-dialog v-model="openDialog">
      <q-card>
        <q-card-section>
          <slot />
        </q-card-section>
        <q-card-actions align="right">
          <q-btn
            color="primary"
            @click="toggleDialog"
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-item>
</template>

<script>
import ValidityIcon from './ValidityIcon.vue'

export default {
  name: 'CheckBoxWithValidation',
  components: { ValidityIcon },
  props: {
    value: {
      type: Boolean,
      required: true
    },
    label: {
      type: String,
      default: () => ''
    },
    mandatory: {
      type: Boolean,
      default: () => false
    }
  },
  data () {
    return {
      openDialog: false,
      touched: false
    }
  },
  methods: {
    input (event) {
      this.touched = true
      this.$emit('input', event)
    },
    toggleDialog () { // thok: {{ $t('actions.close') }} was removed from toggeling of helper
      this.openDialog = !this.openDialog
    }
  }
}
</script>
