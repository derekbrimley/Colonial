$(function () {

	$('.add_button').on('click', function() {
		console.log("In product.detail.js");


		//Pulls the data from the add button on products.detail.html
		var photo_id = $(this).attr('data-photo_id');
		var product_id = $(this).attr('data-product_id');
		var qty = $('select').val();

		//Print to log to affirm correct photo and product id and qty
		console.log(photo_id);
		console.log(product_id);
		console.log(qty);

		$.loadmodal({
			url: '/product/shopping_cart.add/' + photo_id + "/" + product_id + "/" + qty + "/",
			title: 'Shopping Cart',
			width: '900px',
		});

	});//click


});//ready 
