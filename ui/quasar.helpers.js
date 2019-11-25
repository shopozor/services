exports.getAPI = function (isDev) {
  if (isDev) {
    return process.env.GRAPHQL_API ? JSON.stringify(process.env.GRAPHQL_API) : JSON.stringify('http://localhost:8000/graphql/')
  } else {
    if (process.env.GRAPHQL_API) {
      return JSON.stringify(process.env.GRAPHQL_API)
    }
    throw new Error('GRAPHQL_API not set')
  }
}
