let ctx = document.getElementById('myTuitionChart');
let act = document.getElementById('myActChart');
let sat = document.getElementById('mySatChart');
let admission = document.getElementById('myAdmissionChart');
let demographics = document.getElementById('demographicChart');
let majors = document.getElementById('majorsChart');

let demographicChart = new Chart(demographics, {
    type: 'pie',
    data: {
        labels: ['Caucasian (' + (caucasian * 100) + '%)', 'African American (' + (africanAmerican * 100) + '%)', 'Hispanic (' + (hispanic * 100) + '%)', 'Asian (' + (asian * 100) + '%)',
            'Pacific Islander (' + (pacificIslander * 100) + '%)', 'Multi-Racial (' + (multiRacial * 100) + '%)', 'Non-Resident (' + (nonResident * 100) + '%)',
            'American Indian/Alaskan native (' + (aian * 100) + '%)'],
        datasets: [{
            label: 'Demographic Percentages (%)',
            data: [caucasian * 100, africanAmerican * 100, hispanic * 100, asian * 100, pacificIslander * 100, multiRacial * 100, nonResident * 100, aian * 100],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(176, 85, 90, 0.2)',
                'rgba(120, 45, 200, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(25, 102, 255, 1)',
                'rgba(190, 98, 78, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend : {
            position: 'left',
        },
        title: {
          display: false,
          text: 'Demographic Percentages (%)'
        },
    }
});

let myTuitionChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['In-State Tuition ($' + (parseInt(inStateTuition)).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,') + ')', 'Out-of-State Tuition ($' + (parseInt(outStateTuition)).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,') + ')'],
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
        title: {
          display: true,
          text: 'Tuition in USD ($)'
        },
        legend: {
            display: false
        },
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
        labels: ['ACT Score (' + parseInt(actScore) + ')'],
        datasets: [{
            label: 'ACT Score (out of 36)',
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
        title: {
          display: true,
          text: 'Average ACT Score (out of 36)'
        },
        legend: {
            display: false
        },
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
        labels: ['SAT Score (' + parseInt(satScore) + ')'],
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
        title: {
          display: true,
          text: 'Average SAT Score (out of 1600)'
        },
        legend: {
            display: false
        },
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