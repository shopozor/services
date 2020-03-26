export const wait = timeInMs => {
  const start = Date.now()
  const end = start + timeInMs
  while (Date.now() < end) {
    console.log(`waiting ${timeInMs}ms...`)
  }
}

export const atLeastOneMatch = (array1, array2) => {
  return array1.some(el1 => {
    return array2.some(el2 => {
      return el1 === el2
    })
  })
}

export const firstUpperCase = (string) => string.charAt(0).toUpperCase() + string.slice(1)

export const getValueFromObject = ({ object, path }) => {
  return path.split('.').reduce((prev, curr) => {
    return prev ? prev[curr] : null
  }, object)
}

export const setValueOfObject = ({ object, path, value }) => {
  const pathArray = path.split('.')
  const last = pathArray.length - 1
  const mutatedProp = pathArray[last]
  const accessArray = pathArray.slice(0, last)

  const superProp = accessArray.reduce((prev, curr) => {
    return prev ? prev[curr] : null
  }, object)

  superProp[mutatedProp] = value
}
