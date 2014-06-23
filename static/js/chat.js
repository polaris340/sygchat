$(document).ready(function(){
	var pusher = new Pusher('1d81fdd2355a7d0819e3');
    var channel = pusher.subscribe('test_channel');
    
	$(document).on('keydown','input#input-message',function(e){
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
      $('ul#chat-list').append('<li>'+data.username+': '+data.message+'</li>');
    });
    
    
    
    
});



function send(message){
	$.ajax({
		url:'/send?message='+message,
		type:'GET'
	});
}