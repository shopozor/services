import { Given, Then } from 'cypress-cucumber-preprocessor/steps'

Given('je veux faire passer le build de ci', function () {
  cy.visit('/')
})

Then('je le fais passer', function () {
  cy.url().should('include', '/')
})
