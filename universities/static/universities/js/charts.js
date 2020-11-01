let ctx = document.getElementById('myTuitionChart');
let act = document.getElementById('myActChart');
let sat = document.getElementById('mySatChart');

let myTuitionChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            label: 'Tuition in USD ($)',
            data: [parseInt(inStateTuition), parseInt(outStateTuition)],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});