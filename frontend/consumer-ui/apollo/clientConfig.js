import { InMemoryCache } from 'apollo-cache-inmemory'
export default function (context) {
  return {
    httpLinkOptions: {
      uri: process.env.GRAPHQL_API,
      credentials: 'same-origin'
    },
    cache: new InMemoryCache(),
    wsEndpoint: process.env.GRAPHQL_API.replace('http', 'ws')
  }
}
