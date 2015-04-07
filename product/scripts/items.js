$(function () {
	
	$('#non-rentable').on('click',function(){
		console.log("clicked");
		$.ajax({
			url:'/product/items.non_rentable/',
			success: function(data){
				$('#items_container').html(data);
			},//success
		})
		
	})
	
	$('#rentable').on('click',function(){
		console.log("clicked");
		$.ajax({
			url:'/product/items.rentable/',
			success: function(data){
				$('#items_container').html(data);
			},//success
		})
		
	})
	
	$('#wardrobe').on('click',function(){
		console.log("clicked");
		$.ajax({
			url:'/product/items.wardrobe/',
			success: function(data){
				$('#items_container').html(data);
			},//success
		})
		
	})
	
});//ready