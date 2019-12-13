import ShopsData from '../../../../shared/fixtures/graphql/responses/Consumer/Shops'

export default {
  Query: () => {
    return {
      shops: () => {
        return ShopsData.data.shops
      }
    }
  }
}
