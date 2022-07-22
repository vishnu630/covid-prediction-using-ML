// Global parameters:
// do not resize the chart canvas when its container does (keep at 600x400px)
Chart.defaults.global.responsive = false;
// define the chart data
var chartData = {
  labels: JSON.parse(jinjaLabels),
  
  datasets: [{
    data: JSON.parse(jinjaValues),
    label: jinjaLegend,
    backgroundColor: "#50164F63",
    pointHoverRadius: 5,
    pointHoverBackgroundColor: "#164F63",
    pointRadius: 1,
    pointHitRadius: 10
    }]
}
console.log(jinjaLabels);
console.log(jinjaValues);


var chartData1 = {
  labels: JSON.parse(jinjaLabels1),

  datasets: [{
    data: JSON.parse(jinjaValues1),
    label: jinjaLegend,
    backgroundColor: "#50164F63",
    pointHoverRadius: 5,
    pointHoverBackgroundColor: "#164F63",
    pointRadius: 1,
    pointHitRadius: 10
    }]
}
console.log(jinjaLabels1);
console.log(jinjaValues1);

var chartData2 = {
  labels: JSON.parse(jinjaLabels2),

  datasets: [{
    data: JSON.parse(jinjaValues2),
    label: jinjaLegend,
    backgroundColor: "#50164F63",
    pointHoverRadius: 5,
    pointHoverBackgroundColor: "#164F63",
    pointRadius: 1,
    pointHitRadius: 10
    }]
}
console.log(jinjaLabels2);
console.log(jinjaValues2);
// get chart canvas
var ctx = document.getElementById("myChart").getContext("2d");

// create the chart using the chart canvas
var myChart = new Chart(ctx, {
  type: 'line',
  data: chartData,
});

var ctx = document.getElementById("con").getContext("2d");

// create the chart using the chart canvas
var con = new Chart(ctx, {
  type: 'line',
  data: chartData1,
});


var ctx = document.getElementById("det").getContext("2d");

// create the chart using the chart canvas
var det = new Chart(ctx, {
  type: 'line',
  data: chartData2,
});