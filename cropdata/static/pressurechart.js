var updateDropDown1 = function(){
    $.getJSON('/pressdatapassing/', function (data_response) {
        var dropdownval = data_response.pdata;
        
        var A = dropdownval.dist;
        
        var B = ["ALL"].concat(dropdownval.yr);
        var C = dropdownval.yr;
        // console.log(B)

        var val1 = ""
        var val2 = ""
        var val3 = ""
        
        for (dval in A) {
            val1 += "<option>" + A[dval]+ "</option>";
        }
        document.getElementById("dis1").innerHTML = val1;
        document.getElementById("dis2").innerHTML = val1;
        for (yval in B){
            val2 += "<option>" + B[yval]+ "</option>";
        }
        for (yval2 in C){
            val3 += "<option>" + C[yval2]+ "</option>";
        }

        document.getElementById("year1").innerHTML = val2;
        document.getElementById("year2").innerHTML = val3;
        
        chart1();
        chart2();

    });

};

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
        // console.log(data_list);
        Highcharts.chart('container3', {
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

var chart2 = function(){
    var e = document.getElementById("dis2");
    var dis = e.options[e.selectedIndex].value;
    // console.log(e)
    var f = document.getElementById("year2");
    var yr = f.options[f.selectedIndex].value;
    // console.log(e);
    // console.log(dis+yr);

    $.getJSON('/pressurechartapi/?year='+yr+'&dis='+dis, function (data_response) {
        var press_val = data_response.alldata;
        // console.log(temp_val.value);
        
        var i;
        var data_list = [];
        var len = press_val.year.length;
        for (i = 0; i < len; i++){
            data_list.push({'name':press_val.year[i], 'data':press_val.value[i]})
        }
        // console.log(data_list);
        Highcharts.chart('container4', {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Temperature details of various districts of Tamilnadu state'
            },
            subtitle: {
                text: 'Source: timeanddate.com'
            },
            xAxis: {
                categories: press_val.month,
                type: 'category',
                labels: {
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 1000,
                title: {
                    text: 'Pressure (mb)'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: 'Pressure: <b>{point.y:.1f}mb </b>'
            },
            series: data_list
        });
        // console.log(data_list);
    });

};

updateDropDown1();

