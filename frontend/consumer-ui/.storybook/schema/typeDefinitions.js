export default `
  type Shop {
    id: Int
    latitude: Float
    longitude: Float
    name: String
    description: String
  }

  type Query {
    shops: [Shop]
  }

  schema {
    query: Query
  }
`
