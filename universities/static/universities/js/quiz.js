$(document).ready(function() {
	$("#quiz").click(function(){
		$("#quizStarter").fadeOut("slow", function(){
			$("#quizStarterInterm").fadeIn(3000, function(){
				$("#quizStarterInterm").fadeOut(1000, function(){
					$("#formStarter").fadeIn("slow");
				});
			});
		});
	});
	$("#formStarterNext").click(function(){
		$("#formStarter").fadeOut("slow", function(){
			$("#preferencesStarterInterm").fadeIn(3000, function(){
				$("#preferencesStarterInterm").fadeOut(1000, function(){
					$("#preferencesStarter").fadeIn(2000);
				});
			});
		});
	});
	$(".prefContainer").click(function() {
		if($(this).attr("data-isPref") === "true"){
			$(this).css({backgroundColor: '#6c757d'}, 250);
			$(this).attr("data-isPref", "false");
		}else{
			$(this).css({backgroundColor: '#FFE066'}, 250);
			$(this).attr("data-isPref", "true");
		}
	});
});