import { Before, Given, When, Then } from 'cypress-cucumber-preprocessor/steps'

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

// Here it's difficult to check in more details that the data represented on the map really are those coming from the database
// One thing that makes it hard is that we should find out how the GPS coordinates are transformed into pixels on the map
Then('il voit la carte des Shops', function () {
  // TODO: We also need to make a snapshot image test here to ensure that we really see a map
  // That will most probably need an upgrade to corejs@3; the snapshot libs we tried did not work with corejs@2
  cy.fixture('Consumer/Shops').then(fixture => {
    const nbShops = fixture.data.shops.length
    cy.get('img.leaflet-marker-icon').should('have.length', nbShops)
  })
})

When('il clique sur un Shop', function () {
  cy.clickFirstShopOnMap()
    .getFixtureDataForSelectedShop()
    .as('selectedShop')
})

Then('il voit les caractéristiques de ce Shop', function () {
  cy.assertShopDescriptionMatchesFixture(this.selectedShop)
    .assertShopImageMatchesFixture(this.selectedShop)
})
