$(document).ready(function(){
    //for tabs
    var selected='#track';
    var selected_view="#graph";
    $('#track').click(function(){
	$(selected).parent().attr('class','');
	selected="#track";
	$(selected).parent().attr('class','active');
	$(selected_view).attr('class','ent');
	selected_view="#graph";
	$(selected_view).attr('class','ent show');
    });
    $('#allocate').click(function(){
	$(selected).parent().attr('class','');
	selected="#allocate";
	$(selected).parent().attr('class','active');
	$(selected_view).attr('class','ent');
	selected_view="#m_allocate";
	$(selected_view).attr('class','ent show');
    });
    $('#approve').click(function(){
	$(selected).parent().attr('class','');
	selected="#approve";
	$(selected).parent().attr('class','active');
	$(selected_view).attr('class','ent');
	selected_view="#m_approve";
	$(selected_view).attr('class','ent show');
    });
    $('#report').click(function(){
	$(selected).parent().attr('class','');
	selected="#report";
	$(selected).parent().attr('class','active');
	$(selected_view).attr('class','ent');
	selected_view="#m_report";
	$(selected_view).attr('class','ent show');
	$.ajax({
	    type: 'POST',
	    url : '/ration-office/issues',
	    data: {'username':'ashwink'},
	    success: populateData
	});
    });


    //for submitting ration id
    $('#approve_shop').click(function(e){
	alert($('#shop_id').val());
	$.ajax({
	    url:'/ration-office/approve',
	    data:{'shop_id': $('#shop_id').val()},
	    success: dispStats
	});
    });

    //allocate grain
    $('#allocate_grain').click(function(){
	$.ajax({
	    type: 'POST',
	    url: '/ration-shop/allocate',
	    data: {'username': 'ashwink'},
	    success: allocateMessage
	});
    });
});

function allocateMessage(data){
    if(data.status)
	$('#allocate_area').html('Allocation Successful');
    else
	$('#allocate_area').html('Allocation failed');
}

function dispStats(data){
    if(data.status)
	$('#json_res').html('Approved!');
    else
	$('#json_res').html('Shop not registered');
}

function populateData(data){
    if(data.status){
	var table_header='<table class="table customtb"><thead><tr><th>#</th><th>Name</th><th>Location</th><th>Shop Keeper</th><th>Complaint</th></tr></thead><tbody>';
	var table_text = table_header;
	var i=1;
	for (complaint of data.complaints){
	    table_text+='<tr><td>'+(i++)+'</td><td>'+complaint.name+'</td><td>'+complaint.location+'</td><td>'+complaint.shopkeeper+'</td><td class="complaint">'+complaint.description+'</td></tr>';
	}
	table_text+='</tbody></table>';
	$('#m_report').html(table_text);
    }
    else{
	$('#m_report').html('No issues reported today');
    }
}
