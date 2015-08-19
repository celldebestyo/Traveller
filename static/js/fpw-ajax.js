$(function() {
	var $first_form = $("email_form");
	var $second_form = $("verif_form");

	$first_form.submit(function() {
		$.ajax({
			url: "",
			type: "POST",
			data: $first_form.serialize(),
			success: function(response) {
				if (response.indexOf("error") == -1) {
					$(".wrapper.first").fadeOut(400);
					$(".wrapper.second").fadeIn(400);
				} else {
					// show error in popup! <right center>
				}
			},
			error: function() {
				alert("Error");
			}
		});
		return false;
	});

	$second_form.submit(function() {
		$.ajax({
			url: "",
			type: "POST",
			data: $second_form.serialize(),
			success: function(response) {
				if (response.indexOf("error") == -1) {
					// redirect to sign in page
				} else {
					// show error in popup! <right/left center>
				}
			},
			error: function() {
				alert("Error");
			}
		});
		return false;
	});
});