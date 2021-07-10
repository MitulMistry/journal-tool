document.addEventListener('DOMContentLoaded', function() {
   
    // Make API GET request
    fetch(`/userdata`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        loadChart(result);
    });

});

function loadChart(data) {
    mood_data = data['mood_totals'];
    console.log(mood_data);
    
    var ctx = document.getElementById('mood-chart');  
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(mood_data),
            datasets: [{
                label: 'Entries',
                data: Object.values(mood_data),
                backgroundColor: [
                    'rgba(245, 59, 49, 0.3)',
                    'rgba(179, 92, 196, 0.3)',
                    'rgba(47, 152, 250, 0.3)',
                    'rgba(51, 199, 222, 0.3)',
                    'rgba(23, 230, 178, 0.3)'
                ],
                borderColor: [
                    'rgba(245, 59, 49, 1)',
                    'rgba(179, 92, 196, 1)',
                    'rgba(47, 152, 250, 1)',
                    'rgba(51, 199, 222, 1)',
                    'rgba(23, 230, 178, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        // precision, if defined and stepSize is not specified, 
                        // the step size will be rounded to this many decimal places.
                        precision: 0
                    }
                }
            }
        }
    });
}