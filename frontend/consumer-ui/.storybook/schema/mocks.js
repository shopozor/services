import ShopsData from '~fixtures/Consumer/Shops'
import Budzons from '~fixtures/Budzons'
import ProjectOverview from '~fixtures/ProjectOverview'

export default {
  Query: () => {
    return {
      shops: () => {
        return ShopsData.data.shops
      },
      // the first argument available here is in the () [if we provided some] is the query name
      // the second argument is the where clauses and stuff
      users: () => {
        return Budzons.data.users
      },
      sites: () => {
        return ProjectOverview.data.sites
      }
    }
  }
}