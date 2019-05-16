$(document).ready(function() {
    
    //Remove the Nones from the textboxes
    $('input.capture').each(
	    function(index){  
	    	var textbox = $(this);

	    	if(textbox.val() === 'None')
	    	{
	    		textbox.val('');
	    	}
	    }
	);

	//Link in the save events on exit of textboxes
	$('input.capture').blur(function() {
		var name = $(this).attr("name");
		var count = $(this).val();
		var count_type = $(this).data('count');

		//Call the save to database method
		$.ajaxSetup({ 
		     beforeSend: function(xhr, settings) {
		         function getCookie(name) {
		             var cookieValue = null;
		             if (document.cookie && document.cookie != '') {
		                 var cookies = document.cookie.split(';');
		                 for (var i = 0; i < cookies.length; i++) {
		                     var cookie = jQuery.trim(cookies[i]);
		                     // Does this cookie string begin with the name we want?
		                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                         break;
		                     }
		                 }
		             }
		             return cookieValue;
		         }
		         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
		             // Only send the token to relative URLs i.e. locally.
		             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		         }
		     } 
		});
		if($(this).val()){
			$.ajax({
	        url : "save_data/", // the endpoint
	        type : "POST", // http method
	        data : { item_code: name, count: count, count_type: count_type}, // data sent with the post request

	        // handle a successful response
	        success : function(json) {
	        	$('#lbl' + name).text(json.result);
	        	$('#lbl' + name).addClass('text-success');
	        	$('#lbl' + name).removeClass('text-danger')
	        },

	        // handle a non-successful response
	        error : function(xhr,errmsg,err) {
	        	$('#lbl' + name).text('Error saving data');
	        	$('#lbl' + name).removeClass('text-success');
	        	$('#lbl' + name).addClass('text-danger')
	        }
	    });
		}
				
	});

	$("#searchInput").keyup(function () {
	    //split the current value of searchInput
	    var data = this.value.split(" ");

	    //create a jquery object of the rows
	    var jo = $("#fbody").find("tr");

	    if (this.value == "") {
	        jo.show();
	        return;
	    }
	    //hide all the rows
	    jo.hide();

	    //Recusively filter the jquery object to get results.
	    jo.filter(function (i, v) {
	        var $t = $(this);
	        for (var d = 0; d < data.length; ++d) {
	            if ($t.is(":contains('" + data[d].toUpperCase() + "')")) {
	                return true;
	            }
	        }
	        return false;
	    })
	    //show the rows that match.
	    .show();
	}).focus(function () {
	    this.value = "";
	    $(this).css({
	        "color": "black"
	    });
	    $(this).unbind('focus');
	}).css({
	    "color": "#C0C0C0"
	});



});

