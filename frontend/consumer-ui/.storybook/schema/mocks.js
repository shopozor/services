import ShopsData from '~fixtures/Consumer/Shops'

export default {
  Query: () => {
    return {
      shops: () => {
        return ShopsData.data.shops
      }
    }
  }
}
