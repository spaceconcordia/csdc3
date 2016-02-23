
function updateDiskPartitionTable() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'diskPart'},
        error: function() {
            $( '#error-dialog' ).dialog( "open" );
        },
        success: function(data) {
            $( '#disk-partition-table' ).html(data["jstable"]);
            $( '#disk-partition-date' ).text(data["request_time"]);
        }
    });
}

function updateMemIntensiveProcesses() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'cpuIntensProc'},
        error: function() {
            $( '#error-dialog' ).dialog( "open" );
        },
        success: function(data) {
            $( '#ram-intens-proc-table' ).html(data["jstable"]);
            $( '#ram-intens-proc-date' ).text(data["request_time"]);
        }
    });
}

function updateCpuIntensiveProcesses() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'ramIntensProc'},
        error: function() {
            $( '#error-dialog' ).dialog( "open" );
        },
        success: function(data) {
            $( '#cpu-intens-proc-table' ).html(data["jstable"]);
            $( '#cpu-intens-proc-date' ).text(data["request_time"]);
        }
    });
}

var smoothieRamUsage =       new SmoothieChart();
var smoothieCpuAvgLoad =     new SmoothieChart();
var smoothieCpuUtilization = new SmoothieChart({maxValue:100,minValue:0});

var ramUsageLine =           new TimeSeries();
var cpuUtilizationLine =     new TimeSeries();
var cpuAvgLoadLine5mins =    new TimeSeries();
var cpuAvgLoadLine10mins =   new TimeSeries();
var cpuAvgLoadLine15mins =   new TimeSeries();

function updateRamUsageCharts() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'ramUsageCharts'},
        error: function() {},
        success: function(data) {
            console.log(data["request_time"])
            $( '#ram-usage-date' ).text(data["request_time"]);
            ramUsageLine.append(new Date().getTime(), Math.random());
        }
    });
}

function updateCpuAvgLoadCharts() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'cpuAvgLoadCharts'},
        error: function() {},
        success: function(data) {
            $( '#cpu-avg-load-date' ).text(data["request_time"]);
            cpuAvgLoadLine5mins.append(new Date().getTime(), Math.random());
            cpuAvgLoadLine10mins.append(new Date().getTime(), Math.random());
            cpuAvgLoadLine15mins.append(new Date().getTime(), Math.random());
        }
    });
}

function updateCpuUtilizationCharts() {
    $.ajax({
        url: '/sysdata',
        cache: false,
        type: 'get',
        data: {'data_name': 'cpuUtilizationCharts'},
        error: function() {},
        success: function(data) {
            $( '#cpu-utilization-date' ).text(data["request_time"]);
            cpuUtilizationLine.append(new Date().getTime(), data["timeseries_data"]);
        }
    });
}

$( document ).ready(function() {
    updateDiskPartitionTable();
    updateCpuIntensiveProcesses();
    updateMemIntensiveProcesses();

    smoothieRamUsage.streamTo(document.getElementById("ram-usage-canvas"));
    smoothieCpuAvgLoad.streamTo(document.getElementById("cpu-avg-load-canvas"));
    smoothieCpuUtilization.streamTo(document.getElementById("cpu-util-canvas"));

    setInterval(function() {
        updateCpuAvgLoadCharts();
    }, 1000);
    setInterval(function() {
        updateRamUsageCharts();
    }, 1000);
    setInterval(function() { // 
        updateCpuUtilizationCharts();
    }, 1000);

    smoothieRamUsage.addTimeSeries(ramUsageLine);
    smoothieCpuUtilization.addTimeSeries(cpuUtilizationLine, {lineWidth:2,strokeStyle:'#0000ff',fillStyle:'rgba(0,128,255,0.30)'});
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine5mins);
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine10mins);
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine15mins);

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
    
    $( '#ram-intens-proc-reload' ).click(function(e) {
        e.preventDefault();
        updateMemIntensiveProcesses();
	});
    $( '#cpu-intens-proc-reload' ).click(function(e) {
        e.preventDefault();
        updateCpuIntensiveProcesses();
	});
    $( '#disk-partition-reload' ).click(function(e) {
        e.preventDefault();
        updateDiskPartitionTable();
	});
});
