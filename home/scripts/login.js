$(function () {

	$('.show_login_dialog').on('click', function() {
		console.log("In login.js");
		$.loadmodal({
			url: '/user/login.loginform/',
			title: 'Login',
			width: '600px',
		});

	});//click

});//ready 
