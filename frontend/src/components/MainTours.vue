<template>
<h1>Все экскурсии</h1>
</template>

<script>

export default {
  name: 'MainTours',
  data: function() {
    return {
      tours: [],
    }
  },
  created: function (){
    const vm = this;
    axios.get('/api/tours/')
      .then(function(response){ console.log(response.data) })
  }

}
</script>

<style scoped>

</style>
