<template>
  <q-input
    :value="value"
    :type="type"
    :label="label"
    :hint="hint"
    :error-message="errorMessage"
    :error="showError && knowError"
    no-error-icon
    @input="$emit('input', $event)"
    @blur="$emit('touched')"
  >
    <template v-slot:before>
      <q-icon :name="iconName" />
    </template>
    <template v-slot:append>
      <validity-icon
        :know-error="knowError"
        :show-error="showError"
        :mandatory="mandatory"
      />
    </template>
  </q-input>
</template>

<script>
import ValidityIcon from './ValidityIcon.vue'

export default {
  name: 'InputWithValidation',
  components: { ValidityIcon },
  props: {
    value: {
      type: String, // thok: this was added during porting
      required: true
    },
    type: {
      type: String,
      default: () => 'text'
    },
    label: {
      type: String,
      default: () => ''
    },
    hint: {
      type: String,
      default: () => ''
    },
    errorMessage: {
      type: String,
      default: () => ''
    },
    iconName: {
      type: String,
      default: () => 'edit'
    },
    showError: {
      type: Boolean,
      default: () => false
    },
    knowError: {
      type: Boolean,
      default: () => true
    },
    mandatory: {
      type: Boolean,
      default: () => false
    }
  }
}
</script>
