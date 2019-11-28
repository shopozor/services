import types from '../../../src/types'

// import store from '../../../../src/store/index'

export function getTokenCookie () {
  return cy.getCookie(types.cookies.TOKEN)
}

export function login (email, password) {
  // TODO: the following code needs to be replaced with a programmatic login
  // i.e. a direct call to store.dispatch('login', { email, password, stayLoggedIn }):
  cy.visit('/login')
  connectWithUserCredentialsViaGui(email, password)
  // TODO: instead of the above code, we need something like
  // // TODO: I will probably need to import the action directly and provide it with the commit method
  // let stayLoggedIn = true
  // // // TODO: use the const defined in /types/links.js
  // email = user.email
  // password = user.password
  // store.dispatch('login', { email, password, stayLoggedIn })

  cy.get('@graphql').then(() => {
    getTokenCookie().then(token => {
      expect(token).to.not.be.null
    })
  })
}

export function connectWithUserCredentialsViaGui (email, password) {
  cy.get('input[type=email]').clear().type(email)
  cy.get('input[type=password]').clear().type(password)
  cy.get('button[id="loginButton"]')
    .click()
}

function openSideDrawer () {
  cy.get('[id=sideDrawer]').then(drawer => {
    const transform = drawer.children()[0].style.transform
    const sideDrawerIsVisible = transform.includes('translateX(0px)')
    if (!sideDrawerIsVisible) {
      cy.get('.burger-menu').click()
    }
  })
}

function getPageLink (label) {
  return cy.get(`[id="pageLink->${label}"]`)
}

function clickOnPageLink (label) {
  getPageLink(label).click()
}

export function navigateTo (label) {
  openSideDrawer()
  clickOnPageLink(label)
}

export function checkIfLinkIsActive (label) {
  openSideDrawer()

  getPageLink(label)
    .first()
    .should('have.class', 'isActive')
}
