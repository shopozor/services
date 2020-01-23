<template>
  <div class="bg-white p-6 md:flex md:items-center">
    <img class="w-32 rounded-full mx-auto md:mx-0 md:w-48 md:mr-6" :src="imageUrl" :alt="person.image.alt">
    <div class="text-center md:text-justify">
      <h3 class="text-lg font-bold">
        <!-- TODO: use the full_name!!! https://docs.hasura.io/1.0/graphql/manual/schema/computed-fields.html -->
        {{ person.first_name }} {{ person.last_name }}
      </h3>
      <span v-html="person.description" />
    </div>
  </div>
</template>

<script>
// import ValidatedObjectProp from '~/mixins/ValidatedObjectProp'
import urljoin from 'url-join'
export default {
  // mixins: [
  //   ValidatedObjectProp('person',
  //     ['description', 'full_name', 'img'])
  // ]
  // TODO: put more validation here!
  props: {
    person: {
      type: Object,
      required: true
    }
  },
  computed: {
    imageUrl () {
      // TODO: refactor this: there must be a helper method taking the image url, that's it
      console.log('ASSETS_API = ', process.env.ASSETS_API)
      return urljoin(process.env.ASSETS_API, this.person.image.url)
    }
  }
}
</script>
