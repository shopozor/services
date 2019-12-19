import { createLocalVue, mount } from '@vue/test-utils'
import { LMap, LMarker, LTileLayer } from 'vue2-leaflet'
// eslint-disable-next-line no-unused-vars
import { GestureHandling } from 'leaflet-gesture-handling'
import Map from '../Map'

function getLocalVue () {
  const localVue = createLocalVue()
  localVue.component('l-map', LMap)
  localVue.component('l-tile-layer', LTileLayer)
  localVue.component('l-marker', LMarker)
  return localVue
}

describe('Map', () => {
  const center = [46.718852, 7.097669]
  const zoom = 11
  const localVue = getLocalVue()

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
