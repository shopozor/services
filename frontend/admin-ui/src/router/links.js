import types from '../types'

// thok: currently only imported the home

export const links = [
  types.links.HOME
]

export const orderedLinks = {
  navigation: [
    types.links.HOME
  ]
}

export const accessRules = {
  [types.permissions.NOT_CONNECTED]: {
    [types.links.HOME]: true
  },
  [types.permissions.CONSUMER]: {
    [types.links.HOME]: true
  },
  [types.permissions.MANAGE_PRODUCTS]: {
    [types.links.HOME]: true
  },
  [types.permissions.MANAGE_PRODUCERS]: {
    [types.links.HOME]: true
  },
  [types.permissions.MANAGE_MANAGERS]: {
    [types.links.HOME]: true
  },
  [types.permissions.MANAGE_STAFF]: {
    [types.links.HOME]: true
  },
  [types.permissions.MANAGE_USERS]: {
    [types.links.HOME]: true
  },
  [types.permissions.MANAGE_REX]: {
    [types.links.HOME]: true
  }
}
