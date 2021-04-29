$(function() {
    $( "#slider-range" ).slider({
          range: true,
          min: 0,
          max: 500,
          step: 10,
          values: [ 75, 300 ],
          slide: function( event, ui ) {
              $("#min").html($( "#slider-range" ).slider( "values", 0));
              $("#max").html($( "#slider-range" ).slider( "values", 1));
          }
    });
} );