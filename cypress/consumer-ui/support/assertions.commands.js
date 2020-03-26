Cypress.Commands.add('assertShopDescriptionMatchesFixture', (selectedShop) => {
  cy.get('#shop-description')
    .should(htmlElement => {
      const actualDescr = htmlElement[0].textContent.trim()
      const expectedDescr = selectedShop.description
      expect(actualDescr).to.equal(expectedDescr)
    })
})

Cypress.Commands.add('assertShopImageMatchesFixture', (selectedShop) => {
  cy.get('#shop-img')
    .should(htmlElement => {
      const actualImg = htmlElement[0].style.backgroundImage
      const expectedImg = selectedShop.image.url
      expect(actualImg).to.contain(expectedImg)

      const actualAlt = htmlElement[0].title
      const expectedAlt = selectedShop.image.alt
      expect(actualAlt).to.eq(expectedAlt)
    })
})
