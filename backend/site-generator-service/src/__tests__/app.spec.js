const request = require('supertest')
const app = require('../app')

describe('Test the root path', () => {
  it('should return 200 upon browsing /', async () => {
    const response = await request(app).get('/')
    expect(response.statusCode).toBe(200)
  })
})
