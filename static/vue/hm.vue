<tempale>

</tempale>

<script>
  export default {
    data: {
        example: "yesss",
        tours: []
    },
    created: function (){
        console.log("Ауф");
        const vm = this;
        axios.get('/api/tours/')
            .then(function (response){
                console.log(response.data);
                vm.tours = response.data
            })
    }
  }
</script>