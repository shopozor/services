/* eslint-disable jest/expect-expect */
describe('Remove me', () => {
  it('is only there to have a spec', () => {
    cy.visit('/')
    cy.url().should('include', '/')
  })
})
