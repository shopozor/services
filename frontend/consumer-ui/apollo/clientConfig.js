import { InMemoryCache } from 'apollo-cache-inmemory'
export default function (context) {
  return {
    httpLinkOptions: {
      uri: context.env.GRAPHQL_API,
      credentials: 'same-origin'
    },
    cache: new InMemoryCache(),
    wsEndpoint: context.env.GRAPHQL_API.replace('http', 'ws')
  }
}
