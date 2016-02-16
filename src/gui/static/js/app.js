$( document ).ready(function() {

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

	$( '#time-dialog' ).dialog({
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
				$( '#time-dialog' ).dialog("open");
			}
		})
	});

	$( '#set-time-btn' ).click(function() {
		// Add a date picker form dialog
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
	
	$( '#update-bin-btn' ).click(function() {
		console.log( '#update-bin-btn' );
	});
	
	$( '#timetag-cmd-btn' ).click(function() {
		console.log( '#timetag-cmd-btn' );
	});
});
