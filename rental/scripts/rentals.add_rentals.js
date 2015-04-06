$(function () {

	$('.add_rental').on('click', function() {
		console.log("In rentals.add.js");


		//Pulls the data from the add button on products.detail.html
		var photo_id = $(this).attr('data-photo_id');
		var product_id = $(this).attr('data-product_id');
		var item_id = $(this).attr('data-item_id');
		var customer_id = $(this).attr('data-customer_id');
		var qty = $('select').val();

		//Print to log to affirm correct photo and product id and qty
		console.log(photo_id);
		console.log(product_id);
		console.log(item_id);
		console.log(customer_id);
		console.log(qty);

		$.loadmodal({
			url: '/rental/rentals.add_rental_into_cart/' + photo_id + "/" + product_id + "/" + item_id + "/" + customer_id + "/" + qty + "/",
			title: 'Rental Cart',
			width: '900px',
		});

	});//click

	$('.show_rentalcart').on('click', function() {
		console.log("In rentals.add.js");

		$.loadmodal({
			url: '/rental/rentals.show_rentalcart/',
			title: 'Rental Cart',
			width: '900px',
		});

	});//click


});//ready 
