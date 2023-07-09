function setCharts(chartID){

  // Set new default font family and font color to mimic Bootstrap's default styling
  Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
  Chart.defaults.global.defaultFontColor = '#858796';

  // Pie Chart Example
  var ctx = document.getElementById(chartID);

  var myPieChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
          labels: ctx.dataset.label.replace(/[\[\]']/g, "").split(", "), // Valores de dinámicos desde la DB
          datasets: [{
              data: JSON.parse(ctx.dataset.value), // Valores de dinámicos desde la DB
              backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#858796', '#0060df', '#ae5b02'],
              hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf','#cea233', '#676975','#003eaa','#8e4a01'],
              hoverBorderColor: "rgba(234, 236, 244, 1)",
          }],
      },
      options: {
          maintainAspectRatio: false,
          tooltips: {
              backgroundColor: "rgb(255,255,255)",
              bodyFontColor: "#858796",
              borderColor: '#dddfeb',
              borderWidth: 1,
              xPadding: 15,
              yPadding: 15,
              displayColors: false,
              caretPadding: 10,
          },
          legend: {
              display: false
          },
          cutoutPercentage: 80,
      },
  });
}

