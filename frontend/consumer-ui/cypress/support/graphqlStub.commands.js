const responseStub = result => Promise.resolve({
  json () {
    return Promise.resolve(result)
  },
  text () {
    return Promise.resolve(JSON.stringify(result))
  },
  ok: true
})

const isGraphQL = (path, method) => path.includes('/graphql/') && method === 'POST'

Cypress.Commands.add('stubGraphqlResponse', response => {
  cy.on('window:before:load', (win) => {
    const originalFunction = win.fetch

    function fetch (path, { _, method }) {
      if (isGraphQL(path, method)) {
        return responseStub(response)
      }
      return originalFunction.apply(this, arguments)
    }

    cy.stub(win, 'fetch', fetch).as('graphql')
  })
})

Cypress.Commands.add('stubServer', fixture => {
  cy.fixture(fixture)
    .then(json => {
      cy.stubGraphqlResponse(json)
    })
})
