import { storiesOf } from '@storybook/vue'
import Map from '../Map'
import ShopCard from '../ShopCard'
import ShopsData from '~fixtures/Consumer/Shops'

const components = {
  ShopCard,
  'shops-map': Map
}

const center = [46.718852, 7.097669]
const shop = ShopsData.data.shops[0]
const zoom = 11

storiesOf('Map', module)
  .add('OpenStreetMap Carto with some customizations', () => {
    return {
      components,
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
      template: '<shop-card :shop="shop"/>',
      data: () => ({
        shop
      })
    }
  })
