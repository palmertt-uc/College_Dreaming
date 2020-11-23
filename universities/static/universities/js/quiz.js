$(document).ready(function () {
    $("#quiz").click(function () {
        $("#quizStarter").fadeOut("slow", function () {
            $("#quizStarterInterm").fadeIn(3000, function () {
                $("#quizStarterInterm").fadeOut(1000, function () {
                    $("#formStarter").fadeIn("slow");
                });
            });
        });
    });
    $("#formStarterNext").click(function () {
        $("#formStarter").fadeOut("slow", function () {
            $("#preferencesStarterInterm").fadeIn(3000, function () {
                $("#preferencesStarterInterm").fadeOut(1000, function () {
                    $("#preferencesStarter").fadeIn(2000);
                });
            });
        });
    });
    $("#preferencesStarterPrev").click(function () {
        $("#preferencesStarter").fadeOut("slow", function () {
            $("#formStarter").fadeIn(2000);
        });
    });
    $(".prefContainer").click(function () {
        if ($(this).attr("data-isPref") != "") {
        alert("if");
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
                $(this).attr("data-isPref", " ViolentCrime <= 300");
                $("#inpCrime").attr("value", " ViolentCrime <= 300");
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
    $("#preferencesStarterPrev").click(function () {
        if($("#preferencesStarter").css("display") != "none"){
            $("#preferencesStarter").fadeOut("slow", function () {
                $("#formStarter").fadeIn(2000);
            });
        }
    });
});