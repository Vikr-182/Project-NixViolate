
    var selected =  ""; 
    google.charts.load('current', {
        'packages':['geochart'],
        // Note: you will need to get a mapsApiKey for your project.
        // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
        'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
      });
      var chart;
      google.charts.setOnLoadCallback(drawRegionsMap);
      var array = new Array(0);
      var gh;
      var total = new Array(0);
      array.push(['Country','Popularity']);
      console.log(array);
      var fb = {
          'United States of America' : 'United States',
          'United Kingdom of Great Britain and Northern Ireland' : 'United Kingdom',
          'Russian Federation' : 'RU',
          'Korea, Republic of' : 'South Korea'
      }
      var reverse_fb = {
        'United States' : 'United States of America',
        'United Kingdom' : 'United Kingdom of Great Britain and Northern Ireland',
        'RU' : 'Russian Federation',
        'South Korea' : 'Korea, Republic of'

      }
      for(gg in count){
         if (fb[data[gg]["name"]] != undefined){
            data[gg]["name"] = fb[data[gg]["name"]];
         }
      }
      gh = 0;   
      for(gh in count){
        console.log(gh);
        array.push([data[gh]["name"],parseInt(count[gh]["number"])]);
        total.push([data[gh],count[gh]["number"]]);
    }
    // alert($(".m-portlet__head").width());
    var mapwidth=$(".m-portlet__head").width(),mapheight=200;
    var piewidth=347,pieheight=556;
    console.log(array)
      function drawRegionsMap() {

        // for map
        var data = google.visualization.arrayToDataTable(array);

        var options = {
            colorAxis:{
                colors : ['#00c1cf','#000280'],
                minValue: 0,
                maxValue: 1000,
            },
            width : $(".m-portlet__head").width(),
            height: $(window).height()*0.5

        };

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        function show(){
          // alert("HI");
          // alert(array[chart.getSelection()[0].row+1])
          console.log(chart.getSelection());
          selected = array[chart.getSelection()[0].row+1][0]
          if( reverse_fb[selected] != undefined){
            selected = reverse_fb[selected];
          }
          document.getElementById("country").innerHTML = "\t" + selected;
          populateTable();
          pie();
        }
  

        google.visualization.events.addListener(chart, 'select', show);       
        chart.draw(data, options);

      }
    

