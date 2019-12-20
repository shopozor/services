import { storiesOf } from '@storybook/vue'
import VueI18n from 'vue-i18n'
import Map from '../Map'
import ShopCard from '../ShopCard'
import ShopsData from '~fixtures/Consumer/Shops'

const components = {
  ShopCard,
  'shops-map': Map
}

const center = [46.718852, 7.097669]
const i18n = new VueI18n({
  locale: 'fr',
  messages: {
    fr: {
      gestureHandling: {
        touch: 'Utiliser 2 doigts pour bouger la carte',
        scroll: 'CTRL + scroll pour zoomer',
        scrollMac: '\u2318 + scroll pour zoomer'
      }
    }
  }
})
const shop = ShopsData.data.shops[0]
const zoom = 11

storiesOf('Map', module)
  .add('OpenStreetMap Carto with some customizations', () => {
    return {
      components,
      i18n,
      template: '<shops-map :center="center" :zoom="zoom" :tilesUrl="tilesUrl"/>',
      data: () => ({
        center,
        zoom,
        tilesUrl: 'https://tile.osm.ch/switzerland/{z}/{x}/{y}.png'
      })
    }
  })
  .add('Swiss lv03 projection (epsg:21781)', () => {
    return {
      components,
      i18n,
      template: '<shops-map :center="center" :zoom="zoom" :tilesUrl="tilesUrl"/>',
      data: () => ({
        center,
        zoom,
        tilesUrl: 'https://tile.osm.ch/21781/{z}/{x}/{y}.png'
      })
    }
  })
  .add('Swiss lv95 projection (epsg:2056)', () => {
    return {
      components,
      i18n,
      template: '<shops-map :center="center" :zoom="zoom" :tilesUrl="tilesUrl"/>',
      data: () => ({
        center,
        zoom,
        tilesUrl: 'https://tile.osm.ch/2056/{z}/{x}/{y}.png'
      })
    }
  })
  .add('Swiss Style from xyztobixyz', () => {
    return {
      components,
      i18n,
      template: '<shops-map :center="center" :zoom="zoom" :tilesUrl="tilesUrl"/>',
      data: () => ({
        center,
        zoom,
        tilesUrl: 'https://tile.osm.ch/osm-swiss-style/{z}/{x}/{y}.png'
      })
    }
  })
  .add('French language map', () => {
    return {
      components,
      i18n,
      template: '<shops-map :center="center" :zoom="zoom" :tilesUrl="tilesUrl"/>',
      data: () => ({
        center,
        zoom,
        tilesUrl: 'https://tile.osm.ch/name-fr/{z}/{x}/{y}.png'
      })
    }
  })
  .add('Transparent layer of contour lines', () => {
    return {
      components,
      i18n,
      template: '<shops-map :center="center" :zoom="zoom" :tilesUrl="tilesUrl"/>',
      data: () => ({
        center,
        zoom,
        tilesUrl: 'https://tile.osm.ch/switzerland/{z}/{x}/{y}.png'
      })
    }
  })
  .add('Shop description', () => {
    return {
      components,
      i18n,
      template: '<shop-card :shop="shop"/>',
      data: () => ({
        shop
      })
    }
  })
