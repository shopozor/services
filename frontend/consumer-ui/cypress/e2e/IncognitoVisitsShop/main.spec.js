import { Given } from 'cypress-cucumber-preprocessor/steps'

Given('un utilisateur non identifié', function () {
  cy.getCookie('token').then(token => expect(token).to.be.null)
  cy.visit('/')
  cy.get('button[name="login"]').should('be.visible')
})
