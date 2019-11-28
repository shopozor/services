import {
  getTokenCookie
} from './Helpers'

export default class TokenHandler {
  constructor () {
    this.TIME_DELTA_IN_MS = Cypress.env('timeDeltaInMs')
    this.TIMEOUT_IN_MS = Cypress.env('timeoutInMs')
    this.elapsedTimeInMs = 0
  }

  getToken () {
    if (this.elapsedTimeInMs > this.TIMEOUT_IN_MS) {
      return Promise.reject(new Error('Awaiting token timeout'))
    }
    return getTokenCookie().then(cookie => {
      if (cookie === null) {
        cy.wait(this.TIME_DELTA_IN_MS)
        this.elapsedTimeInMs += this.TIME_DELTA_IN_MS
        return this.getToken()
      }
      return Promise.resolve(cookie.value)
    })
  }

  getNullToken () {
    if (this.elapsedTimeInMs > this.TIMEOUT_IN_MS) {
      return Promise.reject(new Error('Awaiting token timeout'))
    }
    return getTokenCookie().then(cookie => {
      if (cookie !== null) {
        cy.wait(this.TIME_DELTA_IN_MS)
        this.elapsedTimeInMs += this.TIME_DELTA_IN_MS
        return this.getNullToken()
      }
      return Promise.resolve(true)
    })
  }
}
