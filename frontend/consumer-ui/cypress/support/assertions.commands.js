Cypress.Commands.add('assertShopDescriptionMatchesFixture', (selectedShop) => {
  cy.get('#shop-description')
    .should(descrElement => {
      const actualDescr = descrElement[0].textContent.trim()
      const expectedDescr = selectedShop.description
      expect(actualDescr).to.equal(expectedDescr)
    })
})
