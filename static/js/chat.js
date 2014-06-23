
$(document).ready(function(){
	var pusher = new Pusher('5c4043a6d9b4d7f1da8d');
	pusher.connection.bind('connected', function() {
		alert("Aa");
	});
	pusher.connection.bind( 'error', function( err ) { 
		if( err.data.code === 4004 ) {
			log('>>> detected limit error');
		}
	});

});
