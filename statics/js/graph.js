function plotGraph(d) {
	//d1 = d.graph_data;

	//This is mock data         Delete below line
	d1 =[ [4, "8848.45"], [9, "8855.30"], [14, "8859.10"], [19, "8855.65"], [24, "8864.85"], [29, "8867.20"], [34, "8861.95"], [39, "8861.60"], [44, "8867.00"], [49, "8862.95"], [54, "8854.40"], [59, "8861.05"], [64, "8860.00"], [69, "8860.45"], [74, "8861.40"], [79, "8857.80"], [84, "8857.55"], [89, "8858.10"], [94, "8856.50"], [99, "8857.75"], [104, "8862.70"], [109, "8864.95"], [114, "8863.85"], [119, "8862.80"], [124, "8862.00"], [129, "8860.85"], [134, "8866.75"], [139, "8870.70"], [144, "8865.80"], [149, "8867.65"], [154, "8867.40"], [160, "8866.85"], [165, "8870.10"], [169, "8866.95"], [174, "8868.70"], [179, "8867.50"], [184, "8868.15"], [189, "8868.35"], [194, "8873.10"], [199, "8870.60"], [204, "8865.55"], [210, "8868.95"], [214, "8868.25"], [219, "8869.60"], [224, "8868.15"], [229, "8862.35"], [234, "8860.90"], [239, "8863.65"], [244, "8863.10"], [249, "8866.30"], [254, "8866.85"], [259, "8863.70"], [264, "8861.60"], [269, "8862.10"], [274, "8861.95"], [279, "8860.60"], [284, "8857.95"], [289, "8859.75"], [294, "8868.85"], [299, "8866.20"], [304, "8865.30"], [310, "8856.75"], [314, "8857.45"], [320, "8860.90"], [326, "8859.20"], [331, "8855.15"], [336, "8843.60"], [341, "8847.60"], [345, "8848.45"], [350, "8842.20"], [355, "8828.85"], [361, "8829.60"], [366, "8830.35"], [371, "8823.65"]];
  

  var g_max=0,g_min=100000000;
	
	for(e of d1)
	{
		if(e[1]<g_min)
			g_min = e[1];
		if(e[1]>g_max)
			g_max = e[1];
	}
    
    $('#graph').append( $('<h1></h1>').text("Heloooooooo") );

    if ($('#line-chart')[0]) {
        console.log("Reached here!!!!");
        $.plot('#line-chart', [ {
            data: d1,
            label: "Data",

        },],

            {
                series: {
                    lines: {
                        show: true,
                        lineWidth: 1,
                        fill: 0.25,
                    },

                    color: 'rgba(255,255,255,0.7)',
                    shadowSize: 0,
                    points: {
                        show: true,
                    }
                },

                yaxis: {
                	min: g_min,
                    max: g_max,
                    tickColor: 'rgba(255,255,255,0.15)',
                    tickDecimals: 0,
                    font :{
                        lineHeight: 13,
                        style: "normal",
                        color: "rgba(255,255,255,0.8)",
                    },
                    shadowSize: 0,
                },
                xaxis: {
                	min:0,
                    max:375,
                    tickColor: 'rgba(255,255,255,0)',
                    tickDecimals: 0,
                    font :{
                        lineHeight: 13,
                        style: "normal",
                        color: "rgba(255,255,255,0.8)",
                    }
                },
                grid: {
                    borderWidth: 1,
                    borderColor: 'rgba(255,255,255,0.25)',
                    labelMargin:10,
                    hoverable: true,
                    clickable: true,
                    mouseActiveRadius:6,
                },
                legend: {
                    show: false
                }
            });
        console.log("Reached here!!!!");
        $("#line-chart").bind("plothover", function (event, pos, item) {
            if (item) {
                var x = item.datapoint[0].toFixed(2),
                    y = item.datapoint[1].toFixed(2);
                $("#linechart-tooltip").html(item.series.label + " of " + x + " = " + y).css({top: item.pageY+5, left: item.pageX+5}).fadeIn(200);
            }
            else {
                $("#linechart-tooltip").hide();
            }
        });

        $("<div id='linechart-tooltip' class='chart-tooltip'></div>").appendTo("body");
    }

}