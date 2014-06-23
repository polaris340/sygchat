$(document).ready(function(){
	var pusher = new Pusher('1d81fdd2355a7d0819e3');
    var channel = pusher.subscribe('test_channel');
    
	$(document).on('keydown','#input-message',function(e){
		if(e.which == 13){
			send($(this).val());
			$(this).val('');
	
		}
	});

    $(document).on('click','button#button-send',function(){
	    send($("#input-message").val());
	    $("#input-message").val('');
	    return false;
    });
    
    channel.bind('my_event', function(data) {
      $('div#chat-list').append(
      		'<div class="panel panel-primary">'+
      			'<div class="panel-heading">'+
      				'<h3 class="panel-title">'+
      				data.username +
      				'</h3>' +
      			'</div>' +
      			'<div class="panel-body">'+
      				data.message +
      			'</div>' +
      		'</div>'
      	);
    });
});



function send(message){
	$.ajax({
		url:'/send?message='+message,
		type:'GET'
	});
}