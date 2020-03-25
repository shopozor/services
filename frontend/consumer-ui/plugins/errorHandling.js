import Vue from 'vue'

function VueWarningException (message) {
  this.message = message
  this.name = 'VueWarningException'
}

Vue.config.warnHandler = function (msg, vm, trace) {
  console.warn(`Warning: ${msg}`)
  console.warn(`Trace: ${trace}`)
  throw new VueWarningException(`Warn: ${msg}\nTrace: ${trace}`)
}
