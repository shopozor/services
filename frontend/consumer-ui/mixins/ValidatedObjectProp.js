export default function ValidatedObjectProp (propName, keys) {
  return {
    props: {
      [propName]: {
        type: Object,
        required: true,
        validator: value => keys.every(key => key in value)
      }
    }
  }
}
