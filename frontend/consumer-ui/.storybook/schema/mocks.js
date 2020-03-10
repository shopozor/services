import ShopsData from '~fixtures/Consumer/Shops'

export default {
  Query: () => {
    return {
      // the first argument available here is in the () [if we provided some] is the query name
      // the second argument is the where clauses and stuff
      shops: () => {
        return ShopsData.data.shops
      }
    }
  }
}