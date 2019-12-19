import { createLocalVue, mount } from '@vue/test-utils'
import { LMap, LMarker, LPopup, LTileLayer } from 'vue2-leaflet'
// eslint-disable-next-line no-unused-vars
import { GestureHandling } from 'leaflet-gesture-handling'
// import { Icon } from 'leaflet'
import Map from '../Map'

// delete Icon.Default.prototype._getIconUrl

// Icon.Default.mergeOptions({
//   iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
//   iconUrl: require('leaflet/dist/images/marker-icon.png'),
//   shadowUrl: require('leaflet/dist/images/marker-shadow.png')
// })

const localVue = createLocalVue()
localVue.component('l-map', LMap)
localVue.component('l-tile-layer', LTileLayer)
localVue.component('l-marker', LMarker)
localVue.component('l-popup', LPopup)

describe('Map', () => {
  const center = [46.718852, 7.097669]
  const zoom = 11

  it('renders correctly when loading shops', () => {
    const wrapper = mount(Map, {
      localVue,
      propsData: {
        center,
        zoom
      },
      mocks: {
        $apollo: {
          queries: {
            shops: {
              loading: true
            }
          }
        }
      }
    })
    expect(wrapper.element).toMatchSnapshot()
  })
})
