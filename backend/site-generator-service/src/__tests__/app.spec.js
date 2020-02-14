const request = require('supertest')
const app = require('../app')

describe('Test root path', () => {
  it('should return 204 upon browsing /', async () => {
    const response = await request(app).get('/')
    expect(response.statusCode).toBe(204)
  })
})

// TODO: to test this, we need to mock the generator, otherwise jest will fail and we also generate a website, which is not what we want
/* describe('Test generate path', () => {
  it('should return 200 upon browsing /generate', async () => {
    const response = await request(app).get('/generate')
    expect(response.statusCode).toBe(200)
  })
}) */
