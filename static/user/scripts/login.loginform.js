$(function () {

// // Form
// 	$('#loginform').ajaxForm(function(data) {
// 		$('#loginform_container').html(data);

// 	});//ajaxForm

// //Modal
// 	$('#loginform').ajaxForm(function(data) {
// 		$('#login_dialog').find('.modal-body').html(data);

// 	});//ajaxForm


//LoadModal
	$('#loginform').ajaxForm(function(data) {
		$('#jquery-loadmodal-js-body').html(data);

	});//ajaxForm
    

});//ready 
