$(document).ready(function () {
    let pages = ["#quizStarter", "#quizStarterInterm", "#formStarter", "#preferencesStarterInterm", "#preferencesStarterOne", "#preferencesStarterIntermTwo", "#preferencesStarterTwo"]
    let currentIndex = 0;

    let contGroups = {
        "costs": ["contLowCosts", "contMedCosts", "contHighCosts"],
        "selectivity": ["contLowSelectivity", "contMedSelectivity", "contHighSelectivity"],
        "special": ["contNoPrefInstitution", "contNoneInstitution", "contHBInstitution", "contNAInstitution"],
        "type": ["contPublic", "contPrivate", "contNoTypePref"],
        "size": ["contSmallSize", "contMediumSize", "contLargeSize", "contNoPrefSize"],
        "graduation_rate":["contNoPrefGradRate", "contAvgGradRate", "contHighGradRate"],

        "housing_costs": ["contLowHousingCosts", "contMedHousingCosts", "contHighHousingCosts"],
        "job_availability": ["contNoPrefJobs", "contEntryJobs", "contMyFieldJobs"],
        "crime": ["contNoPrefCrime", "contViolentCrime", "contPropertyCrime", "contBothCrime"],
        "community": ["contNoPrefCommunity", "contRuralCommunity", "contSuburbanCommunity", "contUrbanCommunity", "contRuralSuburbanCommunity", "contRuralUrbanCommunity", "contSuburbanUrbanCommunity"],

        "summers": ["contNoPrefSummers", "contCoolSummers", "contWarmSummers", "contHotSummers"],
        "winters": ["contNoPrefWinters", "contColdWinters", "contCoolWinters", "contWarmWinters"],
        "snowy": ["contNoPrefSnow", "contNoSnow", "contSomeSnow", "contLotsOfSnow"],

    };

    let groupAttr = {
        "contLowCosts": ["src", "low cost stock", "I'm not worried about costs"],
        "contMedCosts": ["/static/universities/images/snowy_stock.png", "medium cost stock", "I'm worried about costs"],
        "contHighCosts": ["src", "high cost stock", "I'm very worried about costs"],

        "contLowSelectivity": ["src", "not selective stock", "I want an institution with a high acceptance rate"],
        "contMedSelectivity": ["src", "selective stock", "I want a selective institution"],
        "contHighSelectivity": ["src", "very selective stock", "I want a very selective institution"],

        "contNoPrefInstitution": ["src", "no preference stock", "I have no preference towards specialty institutions"],
        "contNoneInstitution": ["src", "no specialty stock", "I do not want a specialty institution"],
        "contHBInstitution": ["src", "historically black stock", "I want a historically black institution"],
        "contNAInstitution": ["src", "Native American institution stock", "I want a Native American institution"],

        "contPublic": ["src", "public school stock", "I'm interested in public schools"],
        "contPrivate": ["src", "private school stock", "I'm interested in private schools"],
        "contNoTypePref": ["src", "no preference stock", "I have no preference towards public/private schools"],

        "contSmallSize": ["src", "small school stock", "I prefer smaller schools"],
        "contMedSize": ["src", "average school size stock", "I prefer average size schools"],
        "contLargeSize": ["src", "large school stock", "I prefer larger schools"],
        "contNoPrefSize": ["src", "no preference stock", "I have no preference towards school size"],

        "contNoPrefGradRate": ["src", "no preference stock", "I have no preference with graduation rates"],
        "contAvgGradRate": ["src", "average graduation rate stock", "I prefer schools with an average graduation rate"],
        "contHighGradRate": ["src", "high graduation rate stock", "I prefer schools with a high graduation rate"],


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