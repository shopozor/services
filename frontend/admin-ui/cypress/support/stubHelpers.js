export const responseStub = result => Promise.resolve({
  json () {
    return Promise.resolve(result)
  },
  text () {
    return Promise.resolve(JSON.stringify(result))
  },
  ok: true
})
