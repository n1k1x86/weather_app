// Get the canvas element
var ctx = document.getElementById('myChart').getContext('2d');
var chart_data = {{ chart_data|safe }};
var labels = {{ labels|safe }};

var datasets = []

// Initialize a new Chart instance
var myChart = new Chart(ctx, {
    type: 'bar', // Specify the chart type
    data: {
        labels: ['Label 1', 'Label 2', 'Label 3'],
        datasets: [{
            label: 'My Dataset',
            data: [10, 20, 30],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
            ],
            borderWidth: 1,
        }],
    },
});
