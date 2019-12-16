<template>
  <div>
    <h3>Authors</h3>
    <my-map />
  </div>
</template>

<script>
import Map from '~/components/Map'

export default {
  components: {
    'my-map': Map
  },
  head: {
    title: 'Authors of Blog'
  }
}
</script>

<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  line-height: 1.6;
}
a {
  text-decoration: none;
  color: #3498DB;
}
a:hover {
  border-bottom: 1px solid;
}
</style>
