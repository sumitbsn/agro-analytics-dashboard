

var updateDropDown1 = function(){
    $.getJSON('/tempdatapassing/', function (data_response) {
        var dropdownval = data_response.tdata;
        
        var A = dropdownval.dist;
        var B ;
        B = ["ALL"].concat(dropdownval.yr);
        console.log(B)

        var val1 = ""
        var val2 = ""
        
        for (dval in A) {
            val1 += "<option>" + A[dval]+ "</option>";
        }
        document.getElementById("dis1").innerHTML = val1;

        for (yval in B){
            val2 += "<option>" + B[yval]+ "</option>";
        }

        document.getElementById("year1").innerHTML = val2;

        chart1();

    });

}

var chart1 = function(){

    var e = document.getElementById("dis1");
    var dis = e.options[e.selectedIndex].value;
    // console.log(e)
    var f = document.getElementById("year1");
    var yr = f.options[f.selectedIndex].value;
    // console.log(e);
    console.log(dis+yr);




    // console.log('working');
    $.getJSON('/temperaturechartapi/?year='+yr+'&dis='+dis, function (data_response) {
        var temp_val = data_response.alldata;
        // console.log(temp_val);
        var i;
        var data_list = [];
        var len = temp_val.year.length;
        for (i = 0; i < len; i++){
            data_list.push({'name':temp_val.year[i], 'data':temp_val.value[i]})
        }

        Highcharts.chart('container1', {
            chart: {
                type: 'line'
            },
            title: {
                text: 'Temperature details of various districts of Tamilnadu state'
            },
            subtitle: {
                text: 'Source: WorldClimate.com'
            },
            xAxis: {
                categories: temp_val.month
            },
            yAxis: {
                title: {
                    text: 'Temperature (°C)'
                }
            },
            plotOptions: {
                line: {
                    dataLabels: {
                        enabled: true
                    },
                    enableMouseTracking: false
                }
            },

            series: data_list 

           
        });
    });
};

updateDropDown1();


