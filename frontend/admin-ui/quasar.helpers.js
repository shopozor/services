exports.getAPI = function (isDev) {
  if (isDev) {
    return JSON.stringify(process.env.GRAPHQL_API || 'http://localhost:8080/v1/graphql/')
  } else {
    if (process.env.GRAPHQL_API) {
      return JSON.stringify(process.env.GRAPHQL_API)
    }
    throw new Error('GRAPHQL_API not set')
  }
}
