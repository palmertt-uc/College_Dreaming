$(document).ready(function () {
    let pages = ["#quizStarter", "#quizStarterInterm", "#formStarter", "#quizACTInterm","#testStarter", "#quizMajorInterm", "#majorStarter", "#preferencesStarterInterm", "#preferencesStarterOne", "#preferencesStarterIntermTwo", "#preferencesStarterTwo",
     "#preferencesStarterIntermThree", "#preferencesStarterThree"]
    let currentIndex = 0;

    let contGroups = {
        "costs": ["contLowCosts", "contMedCosts", "contHighCosts"],
        "selectivity": ["contLowSelectivity", "contMedSelectivity", "contHighSelectivity"],
        "special": ["contNoPrefInstitution", "contNoneInstitution", "contHBInstitution", "contNAInstitution", "contAAPIInstitution", "contMenInstitution", "contWomenInstitution",
                    "contReligiousInstitution", "contHispanicInstitution", "contTribalInstitution"],
        "type": ["contPublic", "contPrivate", "contNoTypePref"],
        "size": ["contSmallSize", "contMedSize", "contLargeSize", "contNoPrefSize"],
        "graduation_rate":["contNoPrefGradRate", "contAvgGradRate", "contHighGradRate"],

        "housing_costs": ["contNoPrefHousingCosts", "contLowHousingCosts", "contMedHousingCosts"],
        "earnings": ["contNoPrefEarnings", "contEarnings"],
        "crime": ["contNoPrefCrime", "contViolentCrime", "contPropertyCrime", "contBothCrime"],
        "community": ["contNoPrefCommunity", "contRuralCommunity", "contSuburbanCommunity", "contUrbanCommunity", "contRuralSuburbanCommunity", "contRuralUrbanCommunity", "contSuburbanUrbanCommunity"],

        "summers": ["contNoPrefSummers", "contCoolSummers", "contWarmSummers", "contHotSummers"],
        "winters": ["contNoPrefWinters", "contColdWinters", "contCoolWinters", "contWarmWinters"],
        "snowy": ["contNoPrefSnow", "contNoSnow", "contSomeSnow", "contLotsOfSnow"],
        "sunny": ["contNoPrefSunny", "contSunny"]
    };

    let groupAttr = {
        "contLowCosts": ["/static/universities/images/institution/low_costs.png", "low cost stock", "I'm not worried about costs"],
        "contMedCosts": ["/static/universities/images/institution/medium_costs.png", "medium cost stock", "I'm worried about costs"],
        "contHighCosts": ["/static/universities/images/institution/high_costs.png", "high cost stock", "I'm very worried about costs"],

        "contLowSelectivity": ["/static/universities/images/institution/low_selectivity.png", "not selective stock", "I prefer a high acceptance rate"],
        "contMedSelectivity": ["/static/universities/images/institution/medium_selectivity.png", "selective stock", "I want a selective institution"],
        "contHighSelectivity": ["/static/universities/images/institution/high_selectivity.png", "very selective stock", "I want a very selective institution"],

        "contNoPrefInstitution": ["src", "no preference stock", "I have no preference towards specialty institutions"],
        "contNoneInstitution": ["src", "no specialty stock", "I do not want a specialty institution"],
        "contHBInstitution": ["/static/universities/images/institution/black_institution.png", "historically black stock", "I want a historically black institution"],
        "contNAInstitution": ["src", "Native American institution stock", "I want a Native American institution"],
        "contAAPIInstitution": ["/static/universities/images/institution/aapi_institution.png", "Asian American Pacific Islander institution stock", "I want an Asian American Pacific Islander institution"],
        "contMenInstitution": ["/static/universities/images/institution/men_institution.png", "men only institution stock", "I want a men's only institution"],
        "contWomenInstitution": ["/static/universities/images/institution/women_institution.png", "women only institution stock", "I want a women's only institution"],
        "contReligiousInstitution": ["src", "Religious Affiliation Stock", "I want a religious affiliated institution"],
        "contHispanicInstitution": ["src", 'Hispanic Serving Stock', "I want a Hispanic Serving institution"],
        "contTribalInstitution": ["src", "Tribal Colleges and Universities", "I want a Tribal institution"],

        "contPublic": ["/static/universities/images/institution/public_institution.png", "public school stock", "I'm interested in public schools"],
        "contPrivate": ["/static/universities/images/institution/private_institution.png", "private school stock", "I'm interested in private schools"],
        "contNoTypePref": ["/static/universities/images/institution/public_private.png", "no preference stock", "I have no preference towards public/private schools"],

        "contSmallSize": ["/static/universities/images/institution/small_institution.png", "small school stock", "I prefer smaller schools"],
        "contMedSize": ["/static/universities/images/institution/medium_institution.png", "average school size stock", "I prefer average size schools"],
        "contLargeSize": ["/static/universities/images/institution/large_institution.png", "large school stock", "I prefer larger schools"],
        "contNoPrefSize": ["/static/universities/images/institution/size_no_pref.png", "no preference stock", "I have no preference towards school size"],

        "contNoPrefGradRate": ["/static/universities/images/institution/graduation_no_pref.png", "no preference stock", "I have no preference with graduation rates"],
        "contAvgGradRate": ["/static/universities/images/institution/average_graduation.png", "average graduation rate stock", "I prefer schools with an average graduation rate"],
        "contHighGradRate": ["/static/universities/images/institution/high_graduation.png", "high graduation rate stock", "I prefer schools with a high graduation rate"],

        "contNoPrefHousingCosts": ["/static/universities/images/living/costs_no_pref.png", "no pref housing costs stock", "I have no preference towards housing costs"],
        "contLowHousingCosts": ["/static/universities/images/living/low_housing_costs.png", "low housing costs stock", "Low housing costs are important to me"],
        "contMedHousingCosts": ["/static/universities/images/living/medium_housing_costs.png", "average housing costs stock", "Average housing costs are okay to me"],

        "contNoPrefEarnings": ["/static/universities/images/living/entry_and_field_jobs.png", "no preference earnings", "I have no preference towards earnings"],
        "contEarnings": ["/static/universities/images/living/my_field_jobs.png", "higher earnings stock", "I want higher than average earnings after graduation"],

        "contNoPrefCrime": ["/static/universities/images/living/crime_both.png", "no preference crime stock", "I am not worried about crime in the area"],
        "contViolentCrime": ["/static/universities/images/living/property_crime.png", "violent crime stock", "I am worried about violent crime in the area"],
        "contPropertyCrime": ["/static/universities/images/living/violent_crime.png", "property crime stock", "I am worried about property crime in the area"],
        "contBothCrime": ["/static/universities/images/living/crime_both.png", "both crime stock", "I am worried about both violent and property crime in the area"],

        "contNoPrefCommunity": ["/static/universities/images/living/community_no_pref.png", "no preference community stock", "I have no preference towards community type"],
        "contRuralCommunity": ["/static/universities/images/living/rural_living.png", "rural community stock", "I prefer rural communities"],
        "contSuburbanCommunity": ["/static/universities/images/living/suburban_living.png", "suburban community stock", "I prefer suburban communities"],
        "contUrbanCommunity": ["/static/universities/images/living/urban_living.png", "urban community stock", "I prefer urban communities"],
        "contRuralSuburbanCommunity": ["/static/universities/images/living/rural_suburb.png", "rural and suburban community stock", "I prefer rural and suburban communities"],
        "contRuralUrbanCommunity": ["/static/universities/images/living/rural_urban.png", "rural and urban community stock", "I prefer rural and urban communities"],
        "contSuburbanUrbanCommunity": ["/static/universities/images/living/suburban_urban.png", "suburban and urban community stock", "I prefer suburban and urban communities"],

        "contNoPrefSummers": ["/static/universities/images/climate/summer_no_pref.png", "no preference summers stock", "I have no preference towards summer temperatures"],
        "contCoolSummers": ["/static/universities/images/climate/cool_summer.png", "cool summers stock", "I prefer cool summers"],
        "contWarmSummers": ["/static/universities/images/climate/warm_summer.png", "warm summer stock", "I prefer warm summers"],
        "contHotSummers": ["/static/universities/images/climate/hot_summer.png", "hot summers stock", "I prefer hot summers"],

        "contNoPrefWinters": ["/static/universities/images/climate/winter_no_pref.png", "no preference winters stock", "I have no preference towards winter temperatures"],
        "contColdWinters": ["/static/universities/images/climate/cold_winter.png", "cold winters stock", "I prefer cold winters"],
        "contCoolWinters": ["/static/universities/images/climate/cool_winter.png", "cool winters stock", "I prefer cool winters"],
        "contWarmWinters": ["/static/universities/images/climate/warm_winter.png", "warm winters stock", "I prefer warm winters"],

        "contNoPrefSnow": ["/static/universities/images/climate/snow_no_pref.png", "no preference snow stock", "I have no preference on snow fall amounts"],
        "contNoSnow": ["/static/universities/images/climate/no_snow.png", "no snow stock", "I prefer no snow"],
        "contSomeSnow": ["/static/universities/images/climate/some_snow.png", "some snow stock", "I prefer some snow"],
        "contLotsOfSnow": ["/static/universities/images/climate/snowy_winter.png", "lots of snow stock", "I prefer lots of snow"],

        "contNoPrefSunny": ["/static/universities/images/climate/cloudy.png", "no preference sunny stock", "I have no preference towards sunny weather"],
        "contSunny": ["/static/universities/images/climate/sunny_weather.png", "sunny stock", "I prefer sunny weather"]
    }

    $(".next").click(function() {
        $(this).css("pointer-events", "none")
        $(pages[currentIndex]).fadeOut("slow", function () {
            currentIndex++;
            $(pages[currentIndex]).fadeIn(2000, function () {
                $(pages[currentIndex]).fadeOut(750, function () {
                    currentIndex++;
                    $(pages[currentIndex]).fadeIn(1500);
                    $(this).css("pointer-events", "auto")
                });
            });
        });
    });

    /*
    For navigating to the previous quiz page
    */
    $(".prev").click(function() {
        $(this).css("pointer-events", "none")
        if(currentIndex != 2){
            $(pages[currentIndex]).fadeOut("slow", function () {
                currentIndex -= 2;
                $(pages[currentIndex]).fadeIn(2000);
                $(this).css("pointer-events", "auto")
            });
        }

    });

    $(".prefContainer").click(function(){
        let srcIndex = 0;
        let altIndex = 1;
        let descIndex = 2;
        let contClass = $(this).attr("class").split(" ")[1];
        let contId = $(this).attr("id");
        let contIndex = contGroups[contClass].indexOf(contId) + 1;
        if(contIndex == contGroups[contClass].length){
            contIndex = 0;
        }
        $(this).fadeOut("slow", function(){
            $("#img-" + contClass).attr("src", groupAttr[contGroups[contClass][contIndex]][srcIndex]);
            $("#img-" + contClass).attr("alt", groupAttr[contGroups[contClass][contIndex]][altIndex]);
            $("#div-" + contClass).text(groupAttr[contGroups[contClass][contIndex]][descIndex]);
            $("#inp-" + contClass).attr("value", contGroups[contClass][contIndex]);
            $(this).attr("id", contGroups[contClass][contIndex]);
            $(this).fadeIn("slow");
        })
    })

    $("#buttonSubmit").click(function(){
        $("input").each(function(){
            if($(this).attr("value") == ""){
                $(this).attr("value", $(this).parent().attr("id"));
            }
        });
    });

    $(".tests").on('input', function() {
    let text = $(this).val()
    if(text != ""){
        let newChar = text.charAt(text.length-1);
        let isNum = newChar >= '0' && newChar <= '9';
        if(!isNum){
            $(this).val(text.substring(0, text.length-1));
        }
    }
});
});



// New Design Code
let open = document.getElementById('hamburger');
let mainContent = document.querySelector('.quiz-form-content');
let changeIcon = true;
let windowSize = window.innerWidth

open.addEventListener("click", function () {

    let overlay = document.querySelector('.overlay');
    let nav = document.querySelector('nav');
    let icon = document.querySelector('.menu-toggle i');

    overlay.classList.toggle("menu-open");
    nav.classList.toggle("menu-open");
    mainContent.classList.add("d-none");

    if (windowSize > 800) {
        mainContent.classList.remove("d-none");
    }

    if (changeIcon) {
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-times");

        changeIcon = false;
    } else {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
        mainContent.classList.remove("d-none");
        changeIcon = true;
    }

    $('select').selectpicker();
});