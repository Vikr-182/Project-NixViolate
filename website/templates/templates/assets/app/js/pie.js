
function populateTable(){
    console.log(Kilo[Country_to_code[selected]['alpha-3']]);
    count = 0;
    var bi = Kilo[Country_to_code[selected]['alpha-3']]
    var string;
    $(".anna").remove();
    for(ki in bi){
        count = count + 1;
        string = '<tr class="anna"><td>' + count.toString() + '</td><td><span class="m-widget11__title">' + bi[ki]["company"] + '</span> <span class="m-widget11__sub"></span></td><td>' + bi[ki]["primary_offense"] + '</td><td><div class="m-widget11__chart" style="height:50px; width: 100px">' + bi[ki]["agency"] + '   </div></td><td>' + bi[ki]["penalty_year"] + '</td><td class="m--align-right m--font-brand">' + bi[ki]["penalty_amount"] + '</td> <\/tr>'
        $("#booty").append(string);
    }
}

function pie(){
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    var arr = new Array(0);
    arr.push(['Company', 'Total Violation']);
    var bi = Kilo[Country_to_code[selected]['alpha-3']]
    for( ki in bi){
        arr.push([bi[ki]["company"],bi[ki]["penalty_amount"]])
    }
    piewidth = ($(".m-portlet__head").width()/2.3)
    console.log(arr);
    function drawChart() {
      var data = google.visualization.arrayToDataTable(arr);

      var options = {
        title: 'Top 10 Violators',
        is3D: true,
        width: piewidth
      };

	    
      var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
      chart.draw(data, options);
    } 
}
function showdb(){
    window.location.href = "http://127.0.0.1:5000/"
}
