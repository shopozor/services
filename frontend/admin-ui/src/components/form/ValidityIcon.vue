<template>
  <transition
    mode="out-in"
    leave-active-class="animated flipOutY"
    enter-active-class="animated flipInY"
  >
    <q-icon
      v-if="!knowError"
      id="valid"
      key="valid"
      name="check_circle"
      color="positive"
    />
    <q-icon
      v-else-if="showError"
      id="error"
      key="error"
      name="error"
      color="negative"
    />
    <q-icon
      v-else-if="mandatory"
      id="mandatory"
      key="mandatory"
      name="fiber_manual_record"
      color="ghost"
    />
  </transition>
</template>

<script>
export default {
  name: 'ValidityIcon',
  props: {
    mandatory: {
      type: Boolean,
      default: false
    },
    knowError: {
      type: Boolean,
      default: false
    },
    showError: {
      type: Boolean,
      default: false
    }
  }
}
</script>
