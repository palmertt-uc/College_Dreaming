let ctx = document.getElementById('myTuitionChart');
let act = document.getElementById('myActChart');
let sat = document.getElementById('mySatChart');
let admission = document.getElementById('myAdmissionChart');
let demographics = document.getElementById('demographicChart');
let litLanguageSocialScience = document.getElementById('litLanguageSocialScience');
let engineeringAndTechnology = document.getElementById('engineering&Technology');
let business = document.getElementById('business');
let scienceAndMath = document.getElementById('science&Math');
let arts = document.getElementById('arts');
let social = document.getElementById('socialSciences');
Chart.defaults.global.defaultFontColor = '#fff';

const cost = JSON.parse(document.getElementById('cost').textContent);
const admissions = JSON.parse(document.getElementById('admission').textContent);
const completionRates = JSON.parse(document.getElementById('completion').textContent);
const undergraduates = JSON.parse(document.getElementById('undergrads').textContent);
const majors = JSON.parse(document.getElementById('majors').textContent);

if (undergraduates.caucasian == null || undergraduates.africanAmerican == null || undergraduates.hispanic == null
    || undergraduates.pacificIslander == null || undergraduates.multiRacial == null || undergraduates.nonResident == null
    || undergraduates.asian == null || undergraduates.aian == null) {
    undergraduates.caucasian = "0.ed.f";
    undergraduates.africanAmerican = "0.ed.f"
    undergraduates.hispanic = "0.ed.f"
    undergraduates.pacificIslander = "0.ed.f"
    undergraduates.multiRacial = "0.ed.f"
    undergraduates.nonResident = "0.ed.f"
    undergraduates.asian = "0.ed.f"
    undergraduates.aian = "0.ed.f"
}

new Chart(document.getElementById("nonResidentCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.nonResidentCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.nonResidentCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "Non-Resident Graduation Rate",
        backgroundColor: ["rgba(255, 61, 223, 0.52)", "rgba(61, 255, 81, 0.52)"],
        data: [(completionRates.nonResidentCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), 100 - (completionRates.nonResidentCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Non-Resident Graduate Rate (%)'
      }
    }
});

new Chart(document.getElementById("multiRacialCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.multiRacialCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.multiRacialCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "Multi-Racial Graduation Rate",
        backgroundColor: ["rgba(214, 0, 0, 0.52)", "rgba(28, 31, 160, 0.4)"],
        data: [(completionRates.multiRacialCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), 100 - (completionRates.multiRacialCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Multi-Racial Graduate Rate (%)'
      }
    }
});

new Chart(document.getElementById("pacificIslanderCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.pacificIslanderCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.pacificIslanderCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "Pacific Islander Graduation Rate",
        backgroundColor: ["rgba(42, 160, 28, 0.4)", "rgba(28, 86, 160, 0.4)"],
        data: [(completionRates.pacificIslanderCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), 100 - (completionRates.pacificIslanderCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Pacific Islander Graduate Rate (%)'
      }
    }
});

new Chart(document.getElementById("aianCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.aianCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.aianCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "American Indian / Alaskan Native Graduation Rate",
        backgroundColor: ["rgba(160, 116, 28, 0.5)", "rgba(160, 28, 97, 0.5)"],
        data: [(completionRates.aianCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), 100 - (completionRates.aianCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'American Indian / Alaskan Native Graduate Rate (%)'
      }
    }
});

new Chart(document.getElementById("asianCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.asianCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.asianCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "Asian Graduation Rate",
        backgroundColor: ["rgba(28, 160, 42, 0.79)", "rgba(160, 28, 28, 0.64)"],
        data: [(completionRates.asianCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), (100 - (completionRates.asianCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Asian Graduate Rate (%)'
      }
    }
});

new Chart(document.getElementById("hispanicCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.hispanicCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.hispanicCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "Hispanic Graduation Rate",
        backgroundColor: ["rgba(103, 228, 184, 0.79)", "rgba(226, 228, 103, 0.79)"],
        data: [(completionRates.hispanicCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), 100 - (completionRates.hispanicCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Hispanic Graduate Rate (%)'
      }
    }
});

new Chart(document.getElementById("whiteCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.whiteCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.whiteCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "Caucasian Graduation Rate",
        backgroundColor: ["rgba(100, 114, 196, 0.79)", "rgba(196, 100, 100, 0.79)"],
        data: [(completionRates.whiteCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), 100 - (completionRates.whiteCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Caucasian Graduate Rate (%)'
      }
    }
});

new Chart(document.getElementById("blackCompletionRate"), {
    type: 'pie',
    data: {
      labels: ["Graduated (" + (completionRates.blackCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + "%)", "Not Graduated (" + (100 - (completionRates.blackCompletionRate.replace(/[^0-9$.,]/g, '') * 100)).toFixed(2) + "%)"],
      datasets: [{
        label: "African American Graduation Rate",
        backgroundColor: ["rgba(196, 170, 100, 0.79)", "rgba(159, 100, 196, 0.79)"],
        data: [(completionRates.blackCompletionRate.replace(/[^0-9$.,]/g, '') * 100).toFixed(2), 100 - (completionRates.blackCompletionRate .replace(/[^0-9$.,]/g, '')* 100).toFixed(2)]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'African American Graduate Rate (%)'
      }
    }
});

let socialSciencesChart = new Chart(social, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Social Science (' + (majors.socialScience.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.socialScience.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(51, 0, 235, 0.53)']
        },
        {
            label: 'Public Administration (' + (majors.publicAdministration.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.publicAdministration.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Ethnic Cultural/Gender Studies (' + (majors.ethnicCulturalGender.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.ethnicCulturalGender.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(117, 11, 11, 0.79)']
        },
        {
            label: 'Psychology (' + (majors.psychology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.psychology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 223, 0, 0.53)']
        },
        {
            label: 'Education (' + (majors.education.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.education.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(117, 11, 111, 0.79)']
        },
        {
            label: 'Legal (' + (majors.legal.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.legal.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(166, 149, 245, 0.79)']
        },
        {
            label: 'Humanities (' + (majors.humanities.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.humanities.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(231, 107, 24, 0.79)']
        },
        {
            label: 'Security & Law Enforcement (' + (majors.securityLawEnforcement.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.securityLawEnforcement.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(28, 24, 231, 0.79)']
        },
        ]
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                title: () => {}
            },
        },
        title: {
          display: true,
          text: 'Social Sciences (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
            xAxes: [{
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
        }
    }
});

let artsChart = new Chart(arts, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Architecture (' + (majors.architecture.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.architecture.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
             backgroundColor: ['rgba(182, 84, 84, 0.79)']
        },
        {
            label: 'Visual Performing (' + (majors.visualPerforming.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.visualPerforming.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Personal Culinary (' + (majors.personalCulinary.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.personalCulinary.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Multi Discipline (' + (majors.multiDiscipline.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.multiDiscipline.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(27, 17, 166, 0.79)']
        },
        {
            label: 'Military (' + (majors.military.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.military.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(166, 17, 146, 0.79)']
        },
        {
            label: 'Parks & Recreation & Fitness (' + (majors.parksRecreationFitness.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.parksRecreationFitness.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(166, 149, 17, 0.79)']
        },
        ]
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                title: () => {}
            },
        },
        title: {
          display: true,
          text: 'Arts & Other (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
            xAxes: [{
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
        }
    }
});

let scienceAndMathChart = new Chart(scienceAndMath, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Health (' + (majors.health.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.health.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
             backgroundColor: ['rgba(182, 84, 84, 0.79)']
        },
        {
            label: 'Mathematics (' + (majors.mathematics.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.mathematics.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Biology (' + (majors.biological.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.biological.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Family Consumer Science (' + (majors.familyConsumerScience.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.familyConsumerScience.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(28, 24, 231, 0.79)']
        },
        {
            label: 'Physical Science (' + (majors.physicalScience.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.physicalScience.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(0, 235, 51, 0.53)']
        },
        {
            label: 'Agriculture (' + (majors.agriculture.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.agriculture.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(17, 166, 129, 0.79)']
        },
        ]
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                title: () => {}
            },
        },
        title: {
          display: true,
          text: 'Science & Math (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
            xAxes: [{
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
        }
    }
});

let businessChart = new Chart(business, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Business Marketing (' + (majors.businessMarketing.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.businessMarketing.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
             backgroundColor: ['rgba(90, 182, 84, 0.79)']
        },
        {
            label: 'Resources (' + (majors.resources.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.resources.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Transportation (' + (majors.transportation.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.transportation.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Construction Management (' + (majors.construction.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.construction.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(28, 24, 231, 0.79)']
        },
        ]
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                title: () => {}
            },
        },
        title: {
          display: true,
          text: 'Business-Related (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
            xAxes: [{
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
        }
    }
});

let engineeringTechChart = new Chart(engineeringAndTechnology, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Engineering (' + (majors.engineering.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.engineering.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
             backgroundColor: ['rgba(51, 0, 235, 0.53)']
        },
        {
            label: 'Engineering Technology (' + (majors.engineeringTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.engineeringTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Communications Technology (' + (majors.communicationsTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.communicationsTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Mechanic Repair Technology (' + (majors.mechanicRepairTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.mechanicRepairTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(0, 235, 51, 0.53)']
        },
        {
            label: 'Science Technology (' + (majors.scienceTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.scienceTechnology.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 223, 0, 0.53)']
        },
        {
            label: 'Computer Science (' + (majors.computer.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.computer.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 141, 0, 0.65)']
        },
        {
            label: 'Precision Production (' + (majors.precisionProduction.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.precisionProduction.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(11, 20, 117, 0.79)']
        },
        ]
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                title: () => {}
            },
        },
        title: {
          display: true,
          text: 'Engineering & Technology (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
            xAxes: [{
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
        }
    }
});

let litLanguageChart = new Chart(litLanguageSocialScience, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [
        {
            label: 'Religious Philosophy (' + (majors.philosophyReligious.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.philosophyReligious.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Theology Religious Vocation (' + (majors.theologyReligiousVocation.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.theologyReligiousVocation.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(0, 235, 51, 0.53)']
        },
        {
            label: 'Library (' + (majors.library.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.library.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 141, 0, 0.65)']
        },
        {
            label: 'History (' + (majors.history.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.history.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(11, 20, 117, 0.79)']
        },
        {
            label: 'English (' + (majors.english.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.english.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(69, 117, 11, 0.79)']
        },
        {
            label: 'Communication (' + (majors.communication.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.communication.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(11, 117, 110, 0.79)']
        },
        {
            label: 'Language (' + (majors.language.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(majors.language.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(150, 117, 200, 0.79)']
        },
        ]
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                title: () => {}
            },
        },
        title: {
          display: true,
          text: 'Literature & Language (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
            xAxes: [{
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
        }
    }
});

function otherDemographic() {
    let total = (undergraduates.caucasian.replace(/[^0-9$.,]/g, '') * 100)
        + (undergraduates.africanAmerican.replace(/[^0-9$.,]/g, '') * 100)
        + (undergraduates.hispanic.replace(/[^0-9$.,]/g, '') * 100) + (undergraduates.asian.replace(/[^0-9$.,]/g, '') * 100)
        + (undergraduates.pacificIslander.replace(/[^0-9$.,]/g, '') * 100) + (undergraduates.multiRacial.replace(/[^0-9$.,]/g, '') * 100)
        + (undergraduates.nonResident.replace(/[^0-9$.,]/g, '') * 100) + (undergraduates.aian.replace(/[^0-9$.,]/g, '') * 100);
    if ((100 - total).toFixed(2) < 0) {
        return 0;
    }else {
        return (100 - total).toFixed(2);
    }
}

let demographicChart = new Chart(demographics, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Caucasian (' + (undergraduates.caucasian.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.caucasian.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(255, 99, 132, 0.5)',]
        },
        {
            label: 'African American (' + (undergraduates.africanAmerican.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.africanAmerican.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(54, 162, 235, 0.5)']
        },
        {
            label: 'Hispanic (' + (undergraduates.hispanic.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.hispanic.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(255, 206, 86, 0.5)']
        },
        {
            label: 'Asian (' + (undergraduates.asian.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.asian.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(75, 192, 192, 0.5)']
        },
        {
            label: 'Pacific Islander (' + (undergraduates.pacificIslander.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.pacificIslander.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(153, 102, 255, 0.5)']
        },
        {
            label: 'Multi-Racial (' + (undergraduates.multiRacial.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.multiRacial.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(255, 159, 64, 0.5)']
        },
        {
            label: 'Non-Resident (' + (undergraduates.nonResident.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.nonResident.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(176, 85, 90, 0.5)']
        },
        {
            label: 'American Indian/Alaskan native (' + (undergraduates.aian.replace(/[^0-9$.,]/g, '') * 100).toFixed(2) + '%)',
            data: [(undergraduates.aian.replace(/[^0-9$.,]/g, '') * 100).toFixed(2)],
            backgroundColor: ['rgba(46, 120, 20, 0.5)']
        },
            {
            label: 'Other (' + otherDemographic() + '%)',
            data: [otherDemographic()],
            backgroundColor: ['rgba(0, 27, 204, 0.5)']
        },
        ]
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                title: () => {}
            },
        },
        title: {
          display: false,
          text: 'Demographic Percentages (%)'
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    max: 100,
                },
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
            xAxes: [{
                stacked: true,
                gridLines: {
                color: '#383838'
            }
            }],
        }
    }
});

let myTuitionChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['In-State ($' + (parseInt(cost.inStateTuition)).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,') + ')', 'Out-of-State ($' + (parseInt(cost.outStateTuition)).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,') + ')'],
        datasets: [{
            label: 'Tuition in USD ($)',
            data: [parseInt(cost.inStateTuition), parseInt(cost.outStateTuition)],
            backgroundColor: [
                'rgba(255, 99, 132, .5)',
                'rgba(54, 162, 235, .5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
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
                },
                gridLines: {
                color: '#383838'
            }
            }],
        },
    }
});

let myActChart = new Chart(act, {
    type: 'bar',
    data: {
        labels: ['ACT Score (' + parseInt(admissions.actScore) + ')'],
        datasets: [{
            label: 'ACT Score (out of 36)',
            data: [parseInt(admissions.actScore)],
            backgroundColor: [
                'rgba(255, 206, 86, .5)'
            ],
            borderColor: [
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
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
                },
                gridLines: {
                color: '#383838'
            }
            }]
        }
    }
});

let mySatChart = new Chart(sat, {
    type: 'bar',
    data: {
        labels: ['SAT Score (' + parseInt(admissions.satScore) + ')'],
        datasets: [{
            label: 'SAT Score (out of 1600)',
            data: [parseInt(admissions.satScore)],
            backgroundColor: [
                'rgba(75, 192, 192, .5)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
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
                },
                gridLines: {
                color: '#383838'
            }
            }]
        }
    }
});