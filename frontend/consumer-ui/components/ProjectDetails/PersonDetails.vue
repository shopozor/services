<template>
  <div class="bg-white p-6 md:flex md:items-center">
    <img class="w-32 rounded-full mx-auto md:mx-0 md:w-48 md:mr-6" :src="assetUrl(person.image.url)" :alt="person.image.alt">
    <div>
      <h3 class="text-lg font-bold text-center md:text-justify">
        <!-- TODO: use the full_name!!! https://docs.hasura.io/1.0/graphql/manual/schema/computed-fields.html -->
        {{ person.first_name }} {{ person.last_name }}
      </h3>
      <span class="text-justify" v-html="person.description" />
    </div>
  </div>
</template>

<script>
import AssetUrl from '~/mixins/AssetUrl'
import ValidatedObjectProp from '~/mixins/ValidatedObjectProp'

export default {
  mixins: [
    AssetUrl,
    ValidatedObjectProp('person',
      ['description', 'first_name', 'last_name', 'image'])
  ],
  props: {
    person: {
      type: Object,
      required: true
    }
  }
}
</script>
