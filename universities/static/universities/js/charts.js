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

let myActChart = new Chart(act, {
    type: 'bar',
    data: {
        labels: ['Yellow'],
        datasets: [{
            label: 'Average ACT Score (out of 36)',
            data: [parseInt(actScore)],
            backgroundColor: [
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    max : 40,
                    min : 0
                }
            }]
        }
    }
});

let mySatChart = new Chart(sat, {
    type: 'bar',
    data: {
        labels: ['Green'],
        datasets: [{
            label: 'SAT Score (out of 1600)',
            data: [parseInt(satScore)],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    max : 1600,
                    min : 0
                }
            }]
        }
    }
});