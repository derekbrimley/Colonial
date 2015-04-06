$(function () {

	$('.add_rental').on('click', function() {
		console.log("In rentals.add.js");


		//Pulls the data from the add button on products.detail.html
		var photo_id = $(this).attr('data-photo_id');
		var product_id = $(this).attr('data-product_id');
		var item_id = $(this).attr('data-item_id');

		//Print to log to affirm correct photo and product id and qty
		console.log(photo_id);
		console.log(product_id);
		console.log(item_id);

		$.loadmodal({
			url: '/rental/rentals.rentalcart_add/' + photo_id + "/" + product_id + "/" + item_id + "/",
			title: 'Rental Cart',
			width: '900px',
		});

	});//click


});//ready 
