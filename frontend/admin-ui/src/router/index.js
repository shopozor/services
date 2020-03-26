import Vue from 'vue'
import VueRouter from 'vue-router'

/* import store from '../store' */
import { generateRoutes /* checkIfUserCanAccess */ } from './Helpers'
import { links, accessRules } from './links'

const routes = generateRoutes({ links, accessRules /*, permissions: store.getters.permissions */ })

Vue.use(VueRouter)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation
 */

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ y: 0 }),
    routes,

    // Leave these as is and change from quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  // thok: do we need this?
  /*
  Router.beforeEach((to, from, next) => {
    const routeIsAccessible = checkIfUserCanAccess({ to, permissions: store.getters.permissions })
    next(routeIsAccessible)
  })
  */
  return Router
}
