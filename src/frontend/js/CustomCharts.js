function PieChart(data,canvaId){
  
  var newCanvas =document.getElementById(canvaId)
  var myPieChart = new Chart(newCanvas, {
    type: "doughnut",
    data: {
      labels: data['data']["labels"],
      datasets: [
        {
          data: data['data']["values"],
          backgroundColor: ["#CD8CF2", "#ebdc87","#4e73df","#ffa36c", "#4CAF50","#6200EA","#F57F17","#FF9E80","#DCEDC8","#607D8B","#4CAF50", "#1cc88a", "#FFEBEE", "#36b9cc","#e1ef0c","#d54062","#799351","#5eaaa8","#d49a89"],
          //hoverBackgroundColor: ["#2e59d9", "#17a673", "#2c9faf"],
          hoverBorderColor: "rgba(234, 236, 244, 1)",
        },
      ],
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        borderColor: "#dddfeb",
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        caretPadding: 10,
      },
      legend: {
        display: true,
      },
      cutoutPercentage: 80,
    },
  });
  
  return(myPieChart)
}

function HexToRGB(hex_color,trnsprnc){

  var myRegexp = /#+([a-zA-Z0-9]{2})+([a-zA-Z0-9]{2})+([a-zA-Z0-9]{2})/gm;
  var m = myRegexp.exec(hex_color);
  var r = parseInt(m[1],16);
  var g = parseInt(m[2],16);
  var b = parseInt(m[3],16);
  
  return("rgb("+r+","+ g+","+b+","+trnsprnc+")")

}


function AreaChart(data_json,canva,color) {
  // Area Chart Example
  
  var ctx = document.getElementById(canva);
    var myLineChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: [],

      datasets: [
        {
          label: "value",
          lineTension: 0.5,
          backgroundColor: HexToRGB(color,0.1), //Area
          borderColor: color, //line
          borderWidth: 2.5,
          pointRadius: 0,
          pointBackgroundColor: color, //Point
          pointBorderColor: color,
          pointHoverRadius: 3,
          pointHoverBackgroundColor: color,
          pointHoverBorderColor: color,
          pointHitRadius: 10,
         
          data: [],
        },
      ],
    },
    options: {
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 10,
          right: 25,
          top: 25,
          bottom: 0,
        },
      },
      scales: {
        xAxes: [
          {
            time: {
              unit: "date",
            },
            gridLines: {
              display: false,
              drawBorder: false,
            },
            ticks: {
              maxTicksLimit: 4,
              //autoSkip: false,
              maxRotation: 0,
              minRotation: 0,

              callback: function(value, index, values) {
            return value.substring(0,value.length-3);
          }
            },
          },
        ],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 1,
          
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
      },
      legend: {
        display: true,
      },
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        titleMarginBottom: 10,
        titleFontColor: "#6e707e",
        titleFontSize: 14,
        borderColor: "#dddfeb",
        borderWidth: 1/2,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        intersect: false,
        mode: "index",
        caretPadding: 10,
        callbacks: {
          label: function (tooltipItem, chart) {
            var datasetLabel =
              chart.datasets[tooltipItem.datasetIndex].label || "";
            return datasetLabel + ": " + number_format(tooltipItem.yLabel);
          },
        },
      },
    },
  });

    return(myLineChart)
}



function BarChart(data_json,canva,color){
  
var ctx = document.getElementById(canva);
var myBarChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [],
    
    datasets: [{
      
      backgroundColor: HexToRGB(color,0.5),
      hoverBackgroundColor: HexToRGB(color,0.5),
      borderColor: HexToRGB(color,0.5),
      data: [],
      maxBarThickness: 25,
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: data_json['labels'].length
        },
        
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: Math.max(...data_json['values']),
          maxTicksLimit: 4,
          padding: 10,
          
          
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      
    },
  }
});
    return(myBarChart)
}


function RadarChart(data_json,canva,color){
  var ctx = document.getElementById(canva);
  var myRadarChart = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: [],
      datasets: 
          [{ data: [],
          backgroundColor: HexToRGB(color,0.3),
          borderColor: color,
          }]
          },
    options: {
      maintainAspectRatio: false, 
      legend: {
      display: false
    },
      
      }
    
  });

  return(myRadarChart)
}

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}


