import urljoin from 'url-join'

export default {
  methods: {
    assetUrl (assetBasename) {
      return urljoin(process.env.ASSETS_API, assetBasename)
    }
  }
}
