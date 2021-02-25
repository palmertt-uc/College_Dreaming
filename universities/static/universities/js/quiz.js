$(document).ready(function () {
    let pages = ["#quizStarter", "#quizStarterInterm", "#formStarter", "#preferencesStarterInterm", "#preferencesStarterOne", "#preferencesStarterIntermTwo", "#preferencesStarterTwo"]
    let currentIndex = 0;

    let contGroups = {
        "costs": ["contLowCosts", "contMedCosts", "contHighCosts"],
        "selectivity": ["contLowSelectivity", "contMedSelectivity", "contHighSelectivity"],
        "special": ["contNoPrefInstitution", "contNoneInstitution", "contHBInstitution", "contNAInstitution", "contAAPIInstitution", "contMenInstitution", "contWomenInstitution"],
        "type": ["contPublic", "contPrivate", "contNoTypePref"],
        "size": ["contSmallSize", "contMediumSize", "contLargeSize", "contNoPrefSize"],
        "graduation_rate":["contNoPrefGradRate", "contAvgGradRate", "contHighGradRate"],

        "housing_costs": ["contNoPrefCosts", "contLowHousingCosts", "contMedHousingCosts"],
        "job_availability": ["contNoPrefJobs", "contEntryJobs", "contMyFieldJobs", "contBothJobs"],
        "crime": ["contNoPrefCrime", "contViolentCrime", "contPropertyCrime", "contBothCrime"],
        "community": ["contNoPrefCommunity", "contRuralCommunity", "contSuburbanCommunity", "contUrbanCommunity", "contRuralSuburbanCommunity", "contRuralUrbanCommunity", "contSuburbanUrbanCommunity"],

        "summers": ["contNoPrefSummers", "contCoolSummers", "contWarmSummers", "contHotSummers"],
        "winters": ["contNoPrefWinters", "contColdWinters", "contCoolWinters", "contWarmWinters"],
        "snowy": ["contNoPrefSnow", "contNoSnow", "contSomeSnow", "contLotsOfSnow"],

    };

    let groupAttr = {
        "contLowCosts": ["/static/universities/images/institution/low_costs.png", "low cost stock", "I'm not worried about costs"],
        "contMedCosts": ["/static/universities/images/institution/medium_costs.png", "medium cost stock", "I'm worried about costs"],
        "contHighCosts": ["/static/universities/images/institution/high_costs.png", "high cost stock", "I'm very worried about costs"],

        "contLowSelectivity": ["/static/universities/images/institution/low_selectivity.png", "not selective stock", "I want an institution with a high acceptance rate"],
        "contMedSelectivity": ["/static/universities/images/institution/medium_selectivity.png", "selective stock", "I want a selective institution"],
        "contHighSelectivity": ["/static/universities/images/institution/high_selectivity.png", "very selective stock", "I want a very selective institution"],

        "contNoPrefInstitution": ["src", "no preference stock", "I have no preference towards specialty institutions"],
        "contNoneInstitution": ["src", "no specialty stock", "I do not want a specialty institution"],
        "contHBInstitution": ["/static/universities/images/institution/black_institution.png", "historically black stock", "I want a historically black institution"],
        "contNAInstitution": ["src", "Native American institution stock", "I want a Native American institution"],
        "contAAPIInstitution": ["src", "Asian American Pacific Islander institution stock", "I want an Asian American Pacific Islander institution"],
        "contMenInstitution": ["/static/universities/images/institution/men_institution.png", "men only institution stock", "I want a men's only institution"],
        "contWomenInstitution": ["/static/universities/images/institution/women_institution.png", "women only institution stock", "I want a women's only institution"],

        "contPublic": ["/static/universities/images/institution/public_institution.png", "public school stock", "I'm interested in public schools"],
        "contPrivate": ["/static/universities/images/institution/private_institution.png", "private school stock", "I'm interested in private schools"],
        "contNoTypePref": ["src", "no preference stock", "I have no preference towards public/private schools"],

        "contSmallSize": ["/static/universities/images/institution/small_institution.ong", "small school stock", "I prefer smaller schools"],
        "contMedSize": ["/static/universities/images/institution/medium_institution.png", "average school size stock", "I prefer average size schools"],
        "contLargeSize": ["/static/universities/images/institution/large_institution.png", "large school stock", "I prefer larger schools"],
        "contNoPrefSize": ["src", "no preference stock", "I have no preference towards school size"],

        "contNoPrefGradRate": ["src", "no preference stock", "I have no preference with graduation rates"],
        "contAvgGradRate": ["/static/universities/images/institution/average_graduation.png", "average graduation rate stock", "I prefer schools with an average graduation rate"],
        "contHighGradRate": ["/static/universities/images/institution/high_graduation.png", "high graduation rate stock", "I prefer schools with a high graduation rate"],

        "contNoPrefHousingCosts": ["src", "no pref housing costs stock", "I have no preference towards housing costs"],
        "contLowHousingCosts": ["/static/universities/images/living/low_housing_costs.png", "low housing costs stock", "Low housing costs are important to me"],
        "contMedHousingCosts": ["/static/universities/images/living/medium_housing_costs.png", "average housing costs stock", "Average housing costs are okay to me"],

        "contNoPrefJobs": ["src", "no pref local job preference stock", "I have no preference towards local jobs"],
        "contEntryJobs": ["/static/universities/images/living/entry_level_jobs.png", "local entry jobs stock", "I prefer having local entry-level jobs available"],
        "contMyFieldJobs": ["/static/universities/images/living/my_field_jobs.png", "my field jobs stock", "I prefer local jobs pertaining to my field"],
        "contBothJobs": ["/static/universities/images/living/entry_and_field_jobs.png", "local entry-level and field-related jobs stock", "I want both local entry level and jobs pertaining to my field"],

        "contNoPrefCrime": ["src", "no preference crime stock", "I am not worried about crime in the area"],
        "contViolentCrime": ["src", "violent crime stock", "I am worried about violent crime in the area"],
        "contPropertyCrime": ["src", "property crime stock", "I am worried about property crime in the area"],
        "contBothCrime": ["src", "both crime stock", "I am worried about both violent and property crime in the area"],

        "contNoPrefCommunity": ["src", "no preference community stock", "I have no preference towards community type"],
        "contRuralCommunity": ["src", "rural community stock", "I prefer rural communities"],
        "contSuburbanCommunity": ["src", "suburban community stock", "I prefer suburban communities"],
        "contUrbanCommunity": ["/static/universities/images/living/urban_stock.png", "urban community stock", "I prefer urban communities"],
        "contRuralSuburbanCommunity": ["src", "rural and suburban community stock", "I prefer rural and suburban communities"],
        "contRuralUrbanCommunity": ["src", "rural and urban community stock", "I prefer rural and urban communities"],
        "contSuburbanUrbanCommunity": ["src", "suburban and urban community stock", "I prefer suburban and urban communities"],

        "contNoPrefSummers": ["src", "no preference summers stock", "I have no preference towards summer temperatures"],
        "contCoolSummers": ["/static/universities/images/climate/cool_summer.png", "cool summers stock", "I prefer cool summers"],
        "contWarmSummers": ["/static/universities/images/climate/warm_summer.png", "warm summer stock", "I prefer warm summers"],
        "contHotSummers": ["/static/universities/images/climate/hot_summer.png", "hot summers stock", "I prefer hot summers"],

        "contNoPrefWinters": ["src", "no preference winters stock", "I have no preference towards winter temperatures"],
        "contColdWinters": ["/static/universities/images/climate/cold_winter.png", "cold winters stock", "I prefer cold winters"],
        "contCoolWinters": ["/static/universities/images/climate/snowy_stock.png", "cool winters stock", "I prefer cool winters"],
        "contWarmWinters": ["/static/universities/images/climate/warm_winter.png", "warm winters stock", "I prefer warm winters"],

        "contNoPrefSnow": ["src", "no preference snow stock", "I have no preference on snow fall amounts"],
        "contNoSnow": ["/static/universities/images/climate/no_snow.png", "no snow stock", "I prefer no snow"],
        "contSomeSnow": ["/static/universities/images/climate/some_snow.png", "some snow stock", "I prefer some snow"],
        "contLotsOfSnow": ["/static/universities/images/climate/snowy_winter.png", "lots of snow stock", "I prefer lots of snow"]
    }

    $(".next").click(function() {
        $(pages[currentIndex]).fadeOut("slow", function () {
            currentIndex++;
            $(pages[currentIndex]).fadeIn(2000, function () {
                $(pages[currentIndex]).fadeOut(750, function () {
                    currentIndex++;
                    $(pages[currentIndex]).fadeIn(1500);
                });
            });
        });
    });

    /*
    For navigating to the previous quiz page
    */
    $(".prev").click(function() {
        if(currentIndex != 2){
            $(pages[currentIndex]).fadeOut("slow", function () {
                currentIndex -= 2;
                $(pages[currentIndex]).fadeIn(2000);
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
        if(contIndex == contGroups.length){
            contIndex = 0;
        }
        $(this).fadeOut("slow", function(){
            $("#img-" + contClass).attr("src", groupAttr[contGroups[contClass][contIndex]][srcIndex]);
            $(this).fadeIn("slow");
        })
    })

    $(".prefContainer").click(function () {
        if ($(this).attr("data-isPref") != "") {
            $(this).css({backgroundColor: '#6c757d'}, 250);
            let id = $(this).attr("id");
            if(id === "contCrime"){
                $(this).attr("data-isPref", "");
                $("#inpCrime").attr("value", "");
            }else if(id === "contRestaurants"){
                $(this).attr("data-isPref", "");
                $("#inpRestaurants").attr("value", "");
            }else if(id === "contOutdoors"){
                $(this).attr("data-isPref", "");
                $("#inpOutdoors").attr("value", "");
            }else if(id === "contCommute"){
                $(this).attr("data-isPref", "");
                $("#inpCommute").attr("value", "");
            }else if(id === "contState"){
                $(this).attr("data-isPref", "");
                $("#inpState").attr("value", "");
            }else if(id === "contDiversity"){
                $(this).attr("data-isPref", "");
                $("#inpDiversity").attr("value", "");
            }

        } else {
            $(this).css({backgroundColor: '#FFE066'}, 250);
            let id = $(this).attr("id");
            $("#inpSubmitted").attr("value", "true");
            if(id === "contCrime"){
                $(this).attr("data-isPref", " ViolentCrimes <= 300");
                $("#inpCrime").attr("value", " ViolentCrimes <= 300");
            }else if(id === "contRestaurants"){
                $(this).attr("data-isPref", " RestaurantRanking <= 50");
                $("#inpRestaurants").attr("value", " RestaurantRanking <= 50");
            }else if(id === "contOutdoors"){
                $(this).attr("data-isPref", " AvgTemp >= 60");
                $("#inpOutdoors").attr("value", " AvgTemp >= 60");
            }else if(id === "contCommute"){
                $(this).attr("data-isPref", "");
                $("#inpCommute").attr("value", "");
            }else if(id === "contState"){
                $(this).attr("data-isPref", "");
                $("#inpState").attr("value", "");
            }else if(id === "contDiversity"){
                $(this).attr("data-isPref", " demographics_white <= .7");
                $("#inpState").attr("value", " demographics_white <= .7");
            }
        }
    });
});