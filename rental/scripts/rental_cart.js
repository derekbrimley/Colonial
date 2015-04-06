$(function () {

	$('.delete_button').click(function() {
		console.log("In rental_cart.js");


		$.ajax({

			url: "/rental/rentals.rentalcart_delete/" + $(this).attr('data-product_id') + "/",
			success: function(data){
				$('.modal-body').html(data);
			},
		});//ajax

	});//click


	$('.show_login_dialog').on('click', function() {
		console.log("In rental_cart.js");
		$.loadmodal({
			url: '/user/login.loginform/',
			title: 'Login',
			width: '600px',
		});

	});//click


});//ready 
