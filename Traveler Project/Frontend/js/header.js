$(function() {
	
	var $bottom_icon = $("#bot-icon");
	
	function active(element) {
		var $temp = $(element).attr("data-dd");
		var el = "#" + $temp;
		
		$(".dropdown").each(function() {
			$(this).fadeOut(400);
			$(this).removeClass("dd-active");
			$(this).addClass("dd-deactive");

			var $tempo = $("#main").find("#text i");

			if ($tempo.hasClass("fa-sort-asc")) {
				$bottom_icon.hide();
				$tempo.removeClass("fa-sort-asc");
				$tempo.addClass("fa-sort-desc");
				$bottom_icon.fadeIn();
			}
		});
		
		$(el).fadeIn(400);
		$(el).addClass("dd-active");
		
		if ($(element).attr("id") == "text") {
			$bottom_icon.hide();
			$($bottom_icon).addClass("fa-sort-asc");
			$($bottom_icon).removeClass("fa-sort-desc");
			$bottom_icon.fadeIn();
		}

		$(el).removeClass("dd-deactive");
	}
	
	$(".dd").on("click", function() {
		
		var $temp = $(this).attr("data-dd");
		var el = "#" + $temp;
		
		if (!$(el).hasClass("dd-active"))
			active($(this));
		else {
			$(el).removeClass("dd-active");
			$(el).addClass("dd-deactive");
			
			if ($(this).attr("id") == "text") {
				$bottom_icon.hide();
				$($bottom_icon).removeClass("fa-sort-asc");
				$($bottom_icon).addClass("fa-sort-desc");
				$bottom_icon.fadeIn();
			}
			
			$(el).fadeOut(400);
		}
			
	});
	
	$(".tab").on("click", function() {
		if ($(this).hasClass("ff")) {
			$(".tab.ff").each(function() {
				$(this).removeClass("current");
			});
			
			$(this).addClass("current");
			var content = $(this).attr("data-content");
			
			$("#ff-dropdown .sub-content").each(function() {
				if ($(this).attr("id") !== content.replace("#", ""))
					$(this).fadeOut(400);
			});
			
			$(content).fadeIn(400);
		} else if ($(this).hasClass("feeds")) {
			$(".tab.feeds").each(function() {
				$(this).removeClass("current");
			});
			
			$(this).addClass("current");
			// var content = $(this).attr("data-content");
			// 
			// $("#feeds-dropdown .sub-content").each(function() {
			// 	if ($(this).attr("id") !== content.replace("#", ""))
			// 		$(this).fadeOut(400);
			// });
			// 
			// $(content).fadeIn(400);
		}
	});
	
});