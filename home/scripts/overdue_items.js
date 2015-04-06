$(function () {

	$( '#30' ).click(function() {
		console.log("Overdue30");


		$.ajax({
			url: '/home/overdue_items.batch_30/',
			success: function(data) {
				$('.overdue_report').html(data);
			 },//success


		});//ajax


	});//click


	$( '#60' ).click(function() {
		console.log("Overdue60");


		$.ajax({
			url: '/home/overdue_items.batch_60/',
			success: function(data) {
				$('.overdue_report').html(data);
			 },//success


		});//ajax


	});//click


	$( '#90' ).click(function() {
		console.log("Overdue90");


		$.ajax({
			url: '/home/overdue_items.batch_90/',
			success: function(data) {
				$('.overdue_report').html(data);
			 },//success


		});//ajax


	});//click


	$( '#email' ).click(function() {
		console.log("Email");


		$.ajax({
			url: '/home/overdue_items.overdue_email/',
			success: function(data) {
				$('.overdue_report').html(data);
			 },//success


		});//ajax


	});//click

});//ready