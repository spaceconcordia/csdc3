$( document ).ready(function() {

    var sourceSwap = function () {
        var $this = $(this);
        var newSource = $this.data('alt-src');
        $this.data('alt-src', $this.attr('src'));
        $this.attr('src', newSource);
    }

    $('img.reload').hover(sourceSwap, sourceSwap);

	$( '#error-dialog' ).dialog({
		autoOpen: false
	});

	$( '#job-success-dialog' ).dialog({
		autoOpen: false,
		resizable: false,
		modal: true,
		buttons: {
			"Ok": function () {
				$(this).dialog('close');
			}
		}
	});

	$( '#deploy-antenna-dialog' ).dialog({
		autoOpen: false,
		resizable: false,
		modal: true,
		buttons: {
			"Yes": function () {
				$.ajax({
					url: '/deploy-antenna',
					type: 'put',
					error: function() {
						$( '#error-dialog' ).dialog( "open" )
					},
					success: function(data) {
						$( '#job-success-text' ).text("The antenna deployment was started successfully");
						$( '#job-success-dialog' ).dialog( "open" )
					}
				});
				$(this).dialog('close');
			},
			"Cancel": function () {
				$(this).dialog('close');
			}
		}
	});
	$( '#deploy-antenna-btn' ).click(function() {
		$( '#deploy-antenna-dialog' ).dialog( "open" )
	});

	$( '#start-payload-dialog' ).dialog({
		autoOpen: false,
		resizable: false,
		modal: true,
		buttons: {
			"Yes": function () {
				$.ajax({
					url: '/start-payload',
					type: 'put',
					error: function() {
						$( '#error-dialog' ).dialog( "open" )
					},
					success: function(data) {
						$( '#job-success-text' ).text("The payload experiment was started successfully");
						$( '#job-success-dialog' ).dialog( "open" )
					}
				});
				$(this).dialog('close');
			},
			"Cancel": function () {
				$(this).dialog('close');
			}
		}
	});
	$( '#start-payload-btn' ).click(function() {
		$( '#start-payload-dialog' ).dialog( "open" )
	});

	$( '#get-time-dialog' ).dialog({
		autoOpen: false,
		buttons: {
			"Ok": function () {
				$(this).dialog('close');
			}
		}
	});
	$( '#get-time-btn' ).click(function() {
		$.ajax({
			url: '/time',
			type: 'GET',
			error: function() {
				$( '#error-dialog' ).dialog( "open" )
			},
			success: function(data) {
				var time = data["time"];
				$( '#time-text' ).text(time);
				$( '#get-time-dialog' ).dialog("open");
			}
		})
	});

	$( '#time-picker' ).datetimepicker();
	$( '#set-time-dialog' ).dialog({
		autoOpen: false,
		buttons: {
			"Set": function () {
				var timeread = $( '#time-picker' ).datetimepicker().val();
				$.ajax({
					url: '/time',
					type: 'POST',
					data: { sys_time: timeread },
					error: function() {
						$( '#error-dialog' ).dialog( "open" )
					},
					success: function(data) {
						if (data["status_code"] == 400) {
                            $( '#error-dialog' ).dialog( "open" )
                        } else if (data["status_code"] == 200) {
                        	var time = data["time"];
                            $( '#time-text' ).text("system time was set to: " + data["time-set"]);
                            $( '#get-time-dialog' ).dialog("open");
                        }
					}
				});
				$(this).dialog('close');
			}
		}
	});
	$( '#set-time-btn' ).click(function() {
		$( '#set-time-dialog' ).dialog("open");
	});
	
	$( '#get-logs-btn' ).click(function() {
		console.log( '#get-logs-btn' );
	});

	$( '#delete-logs-dialog' ).dialog({
		autoOpen: false,
		resizable: false,
		modal: true,
		buttons: {
			"Yes": function () {
				$.ajax({
					url: '/logs',
					type: 'delete',
					error: function() {
						$( '#error-dialog' ).dialog( "open" )
					},
					success: function(data) {
						$( '#job-success-text' ).text("All copies of the logs were deleted successfully.");
						$( '#job-success-dialog' ).dialog( "open" )
					}
				});
				$(this).dialog('close');
			},
			"Cancel": function () {
				$(this).dialog('close');
			}
		}
	});
	$( '#del-logs-btn' ).click(function() {
		$( '#delete-logs-dialog' ).dialog("open");
	});

	$( '#update-binaries-dialog' ).dialog({
		autoOpen: false
	});
	$( '#update-bin-btn' ).click(function() {
		$( '#update-binaries-dialog' ).dialog("open");
	});

	$( '#roll-back-dialog' ).dialog({
		autoOpen: false
	});
    $( '#roll-back-btn' ).click(function() {
		$.ajax({
			url: '/updatebin',
			type: 'GET',
			error: function() {
				$( '#error-dialog' ).dialog( "open" );
			},
			success: function(data) {
                var backup_list = data["backup_list"];
                var selectTag = '<select name=\'backup_file\'>'
                for(index in backup_list) {
                    var optionTag = '<option value=\"' + backup_list[index] + '\">' + backup_list[index] + '</option>'
                    selectTag = selectTag.concat(optionTag);
                }
                selectTag = selectTag.concat('</select>');
                console.log(selectTag)

                $( '#roll-back-id' ).append(selectTag);
                $( '#roll-back-id' ).append('<br/><br/><center><input type="submit" value="roll back" /></center>');
                $( '#roll-back-dialog' ).dialog("open");
			}
        });
    });

	$( '#time-picker-cmd' ).datetimepicker();
	$( '#timetag-cmd-dialog' ).dialog({
		autoOpen: false
	});
	$( '#timetag-cmd-btn' ).click(function() {
		$( '#timetag-cmd-dialog' ).dialog("open");
	});
});
