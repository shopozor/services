<template>
  <div>
    <h2 class="overview-title">
      {{ $t('budzons') }}
    </h2>
    <person-details v-for="budzon in budzons" :key="budzon.id" :person="budzon" />
  </div>
</template>

<script>
import PersonDetails from './PersonDetails'
import budzons from '~graphql/budzons'
export default {
  apollo: {
    budzons: {
      query: budzons
    }
  },
  components: {
    PersonDetails
  }
}
</script>
