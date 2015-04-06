$(function () {

	$( '#search_input' ).focusout(function() {
		input = $(this).val();
		console.log(input);


		$.ajax({
			url: '/product/products.search/',
			data: { 'input': input},//data
			success: function(data) {
				$('.products').html(data);
			 },//success


		});//ajax



		// $('').ajaxForm(function(data) {
		// 	$('#loginform_container').html(data);

		// });//ajaxForm





		// $.ajax({
		// 	url: "/product/products.search/" + input,
		// 	success: function(data)
		// 	{
		// 		$('contents').html(data);
		// 	},

		// });//ajax





		// $.loadmodal({
		// 	url: "/product/products.search/" + input,
		// 	title: 'Search Results for: ' + input,
		// 	width: '900px',
		// });//loadmodal

	});//focusout
});//ready