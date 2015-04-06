$(function () {

	//This is used to check if the username is unique
	alert('Use this form to update the account');
	var current_username = $('#id_username').val();
	console.log(current_username);

	$('#id_username').on('change', function() {
		var username = $('#id_username').val();

		$.ajax({
			url: '/user/user.check_username/',

			data: {
				username: username,
				current_username: current_username,
			},//data

			type: "POST",

			success: function(resp) {
				if (resp == '1') {
					$('.is_username_message').text('Valid Username');
				}else{
					$('.is_username_message').text('Invalid Username');

				console.log("Response = " + resp);

				}//if
			},//success

		});//ajax

	});//change

});//ready