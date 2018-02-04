
var updateDropDown1 = function(){
    $.getJSON('/rainfalldatapassing/', function (data_response) {
        var dropdownval = data_response.rdata;
        
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

}

var chart1 = function(){

    var e = document.getElementById("dis1");
    var dis = e.options[e.selectedIndex].value;
    // console.log(e)
    var f = document.getElementById("year1");
    var yr = f.options[f.selectedIndex].value;
    // console.log(e);
    // console.log(dis+yr);




    // console.log('working');
    $.getJSON('/rainfallchartapi/?year='+yr+'&dis='+dis, function (data_response) {
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
                text: 'Rainfall details of various districts of Tamilnadu state'
            },
            subtitle: {
                text: 'Source: timeanddate.com'
            },
            xAxis: {
                categories: temp_val.month
            },
            yAxis: {
                title: {
                    text: 'Rainfall (mm)'
                }
            },
             credits: {
                enabled: false
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

    $.getJSON('/rainfallchartapi/?year='+yr+'&dis='+dis, function (data_response) {
        var temp_val = data_response.alldata;
        // console.log(temp_val.value);
        
        var i;
        var data_list = [];
        var len = temp_val.year.length;
        for (i = 0; i < len; i++){
            data_list.push({'name':temp_val.year[i], 'data':temp_val.value[i]})
        }
        // console.log(data_list);
        Highcharts.chart('container2', {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Rainfall details of various districts of Tamilnadu state'
            },
            subtitle: {
                text: 'Source: timeanddate.com'
            },
            xAxis: {
                categories: temp_val.month,
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
                min: 0,
                title: {
                    text: 'Rainfall (mm)'
                }
            },
            credits: {
                enabled: false
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: 'Rainfall: <b>{point.y:.1f}mm </b>'
            },
            series: data_list
        });
    });
};

updateDropDown1();


