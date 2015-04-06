$(function () {

	$('.show_login_dialog').on('click', function() {
		console.log("In login.js");
		$.loadmodal({
			url: '/user/login.loginform/',
			title: 'Login',
			width: '600px',
		});

	});//click


	$('.show_join_dialog').on('click', function() {
		$.loadmodal({
			url: '/user/join.joinform/',
			title: 'Join Us!',
			width: '600px',
		});

	});//click

	$('.show_button').on('click', function() {
		console.log("In base.js");

		$.loadmodal({
			url: '/product/shopping_cart/',
			title: 'Shopping Cart',
			width: '900px',
		});

	});//click

});//ready 
