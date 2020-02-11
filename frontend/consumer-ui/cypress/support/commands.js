Cypress.Commands.add('clickFirstShopOnMap', () => {
  cy.get('img.leaflet-marker-icon')
    .first()
    .click({
      force: true
    })
})

Cypress.Commands.add('getFixtureDataForSelectedShop', () => {
  cy.get('#shop-name')
    .then(nameElement => {
      const actualName = nameElement[0].textContent.trim()
      cy.fixture('Consumer/Shops').then(fixture => {
        const shops = fixture.data.shops
        const shop = shops
          .filter(shop => shop.name === actualName)[0]
        return cy.wrap(shop)
      })
    })
})
