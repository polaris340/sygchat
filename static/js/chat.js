$(document).ready(function(){
	var pusher = new Pusher('1d81fdd2355a7d0819e3');
    var channel = pusher.subscribe('test_channel');
    channel.bind('my_event', function(data) {
      alert(data.message);
    });
    
    channel.trigger('my_event',{message:"message"})
});



function send(message){
	$.ajax({
		url:'/send?message='+message,
		type:'GET'
	});
}