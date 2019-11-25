// https://korigan.github.io/Vue2Leaflet/#/quickstart
import { LMap, LTileLayer, LMarker, LIcon, LPopup, LControl } from 'vue2-leaflet'
import { Icon } from 'leaflet'
import 'leaflet/dist/leaflet.css'

export default ({ Vue, app }) => {
  Vue.component('l-map', LMap)
  Vue.component('l-tile-layer', LTileLayer)
  Vue.component('l-marker', LMarker)
  Vue.component('l-icon', LIcon)
  Vue.component('l-popup', LPopup)
  Vue.component('l-control', LControl)

  delete Icon.Default.prototype._getIconUrl

  Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
  })
}
