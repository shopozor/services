import { Before, Given, Then } from 'cypress-cucumber-preprocessor/steps'

Before(() => {
  cy.visit('/')
  cy.get('div[id="close-preview"').click()
})

Given('un utilisateur non identifié', function () {
  cy.location('pathname').should('eq', '/')
  cy.getCookie('token').then(token => expect(token).to.be.null)
  cy.get('button[name="login"]').should('be.visible')
})

Given('Incognito se trouve sur la page d\'accueil', function () {
  cy.location('pathname').should('eq', '/')
})

Then('il voit la carte des Shops', function () {
  // We also need to make a snapshot image test here to ensure that we really see a map
  cy.fixture('Consumer/Shops').then(fixture => {
    const nbShops = fixture.data.shops.length
    cy.get('img.leaflet-marker-icon').should('have.length', nbShops)
  })
})
