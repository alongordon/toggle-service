$(document).ready(function () {

    //Remove the Nones from the textboxes
    $('input.capture').each(
        function (index) {
            var textbox = $(this);

            if (textbox.val() === 'None') {
                textbox.val('');
            }
        }
    );

    $('input.change_count_summary').blur(function(){
        var pk = $(this).data('pk');
        var changed_val = $(this).val();

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
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

        if ($(this).val()) {
            $.ajax({
                url: "save_count_summary/", // the endpoint
                type: "POST", // http method
                data: {pk: pk, value: changed_val}, // data sent with the post request

                // handle a successful response
                success: function (json) {
                    $('#lbl_' + pk).text(json.result);
                    $('#lbl_' + pk).addClass('text-success');
                    $('#lbl_' + pk).removeClass('text-danger')
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    $('#lbl_' + pk).text('Error saving data');
                    $('#lbl_' + pk).removeClass('text-success');
                    $('#lbl_' + pk).addClass('text-danger')
                }
            });
        }


    });

    //Link in the save events on exit of textboxes
    $('input.capture').blur(function () {
        var pk = $(this).attr("name");
        var count = $(this).val();
        var count_type = $(this).data('count');

        //Call the save to database method
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
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
        if ($(this).val()) {
            $.ajax({
                url: "save_data/", // the endpoint
                type: "POST", // http method
                data: {pk: pk, count: count, count_type: count_type}, // data sent with the post request

                // handle a successful response
                success: function (json) {
                    $('#lbl' + pk).text(json.result);
                    $('#lbl' + pk).addClass('text-success');
                    $('#lbl' + pk).removeClass('text-danger')
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    $('#lbl' + pk).text('Error saving data');
                    $('#lbl' + pk).removeClass('text-success');
                    $('#lbl' + pk).addClass('text-danger')
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

