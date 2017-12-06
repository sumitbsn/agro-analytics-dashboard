

var updateDropDown1 = function(){
    $.getJSON('/pressdatapassing/', function (data_response) {
        var dropdownval = data_response.pdata;
        
        var A = dropdownval.dist;
        var B ;
        B = ["ALL"].concat(dropdownval.yr);
        // console.log(B)

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
    // console.log(dis +" "+ yr);




    // console.log('working');
    $.getJSON('/pressurechartapi/?year='+yr+'&dis='+dis, function (data_response) {
        var press_val = data_response.alldata;
        // console.log(press_val);
        var i;
        var data_list = [];
        var len = press_val.year.length;
        for (i = 0; i < len; i++){
            data_list.push({'name':press_val.year[i], 'data':press_val.value[i]})
        }

        Highcharts.chart('container1', {
            chart: {
                type: 'line'
            },
            title: {
                text: 'pressure details of various districts of Tamilnadu state'
            },
            subtitle: {
                text: 'Source: WorldClimate.com'
            },
            xAxis: {
                categories: press_val.month
            },
            yAxis: {
                title: {
                    text: 'Pressure (mb)'
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


