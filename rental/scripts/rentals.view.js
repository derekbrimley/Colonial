/**
 * Created by Administrator on 4/6/2015.
 */
$(function() {

    $('.bulk-return').change(function () {
        if (this.checked) {
            $('.actice-checkbox').prop('checked', true)
        } else {
            $('.actice-checkbox').prop('checked', false)
        }

    });
    $('.mass-return').click(function(){
        if (confirm('Are you sure you want to return all of the selected items?')) {
        var searchIDs = $('.actice-checkbox:checkbox:checked').map(function(){
            return $(this).val();
        }).get();
        //var  = $('.actice-checkbox').is('checked');
        console.log(searchIDs);
        var json_string = JSON.stringify(searchIDs);
        var userid = $(this).attr('data-userid');
        //var pathname = window.location.pathname;
        //console.log(json_string+ '  '+userid)
        $.ajax({
           url:'/rental/rentals.bulk_return/',
            data:{
                bulk: json_string,
                userid: userid
            },//data
            type: "GET",
            success: function(resp){

                $('.replace_me2').html( resp);
            }//success
        });//ajax
        } else {
            // Do nothing!
            }

    });
});