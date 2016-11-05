$(document).ready(function(){
    $('#check_status').click(function(){
	$.ajax({
	    type: 'GET',
	    data : {ration_id : $('#ration_id').val()},
	    url: '/depot/status',
	    success: populateData
	});
    });
});

function populateData(data){
    if(data.status)
	$('#result_post').html(data.text);
    else
	$('#result_post').html('unexpected error!');
}
