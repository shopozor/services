export default {
  Query: () => {
    return {
      shops: () => {
        return [{
          id: 1,
          latitude: 46.775406,
          longitude: 7.037900,
          name: 'Budzonnerie d\'Onnens',
          description: 'blablabli blablabla'
        }, {
          id: 2,
          latitude: 46.7789,
          longitude: 7.0371,
          name: 'Budzonnerie du coin perdu',
          description: 'hihihihihihiiiiiiiiiiiii'
        }]
      }
    }
  }
}
