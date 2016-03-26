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

function updateBatteryInfo() {
    $.ajax({
        url: '/batteryinfo',
        type: 'get',
        cache: false,
        error: function() {
            console.log("error on call to /batteryinfo - GET")
        },
        success: function(data) {
            control = (data['data'])["control"];
            console.log(control);
            batteries = (data['data'])["batteries"];
            for (idx in batteries) {
                temp = (batteries[idx])['temp'];
                if (temp != null) {
                    var prev_value = $('#bat' + String(parseInt(idx) + 1) + '-temp').text();
                    if (!isNaN(parseInt(prev_value))) {
                        if (parseFloat(prev_value) > parseFloat(temp)) {
                            $('#bat' + String(parseInt(idx) + 1) + '-temp').text(temp + '°C' + '\ufeff\u21e9');
                            $('#bat' + String(parseInt(idx) + 1) + '-temp').removeClass("text-success text-info").addClass( "text-danger" );
                        } else if (parseFloat(prev_value) < parseFloat(temp)) {
                            $('#bat' + String(parseInt(idx) + 1) + '-temp').text(temp + '°C' + '\ufeff\u21e7');
                            $('#bat' + String(parseInt(idx) + 1) + '-temp').removeClass("text-info text-danger").addClass( "text-success" );
                        } else {
                            $('#bat' + String(parseInt(idx) + 1) + '-temp').text(temp + '°C');
                            $('#bat' + String(parseInt(idx) + 1) + '-temp').removeClass("text-success text-danger").addClass( "text-info" );
                        }
                    } else {
                        $('#bat' + String(parseInt(idx) + 1) + '-temp').text(temp + '°C');
                    }
                }
                heaters = (batteries[idx])['heaters'];
                if (heaters != null) {
                    if (heaters) {
                        $('#bat' + String(parseInt(idx) + 1) + '-heat').text('Heaters: ON');
                        $('#bat' + String(parseInt(idx) + 1) + '-heat').removeClass("text-info text-danger").addClass( "text-success" );
                    } else {
                        $('#bat' + String(parseInt(idx) + 1) + '-heat').text('Heaters: OFF');
                        $('#bat' + String(parseInt(idx) + 1) + '-heat').removeClass("text-info text-success").addClass( "text-danger" );
                    }
                }
            }
        }
    });
}

var smoothieRamUsage =       new SmoothieChart({maxValue:100,minValue:0});
var smoothieCpuAvgLoad =     new SmoothieChart({maxValueScale:1.06});
var smoothieCpuUtilization = new SmoothieChart({maxValue:100,minValue:0});

var ramUsageLine =           new TimeSeries();
var cpuUtilizationLine =     new TimeSeries();
var cpuAvgLoadLine1mins =    new TimeSeries();
var cpuAvgLoadLine5mins =    new TimeSeries();
var cpuAvgLoadLine15mins =   new TimeSeries();

var intervalListener;

function updateRamUsageCharts() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'ramUsageCharts'},
        error: function() {},
        success: function(data) {
            $( '#ram-usage-date' ).text(data["request_time"]);
            var ram_usage_perc = data["timeseries_data"];
            ramUsageLine.append(new Date().getTime(), ram_usage_perc);
            $( '#ram-usage-used' ).text(data["free_ram"] + ' MB (' + ram_usage_perc.toFixed(1) + '%)');
            $( '#ram-usage-free' ).text(data["used_ram"] + ' MB of ' + data["total_ram"] + ' MB');
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

            cpuAvgLoadLine1mins.append(new Date().getTime(), data["timeseries_data1"]);
            $( '#avg-load-1-min' ).text(data["timeseries_data1"]);

            cpuAvgLoadLine5mins.append(new Date().getTime(), data["timeseries_data5"]);
            $( '#avg-load-5-min' ).text(data["timeseries_data5"]);

            cpuAvgLoadLine15mins.append(new Date().getTime(), data["timeseries_data15"]);
            $( '#avg-load-15-min' ).text(data["timeseries_data15"]);
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
            var cpu_util_perc = data["timeseries_data"];
            cpuUtilizationLine.append(new Date().getTime(), cpu_util_perc);
            $( '#cpu-utilization-percentage' ).text(cpu_util_perc.toFixed(2) + "%")
        }
    });
}

$( document ).ready(function() {
	$( '.dropdown-toggle' ).dropdown();

    updateDiskPartitionTable();
    updateCpuIntensiveProcesses();
    updateMemIntensiveProcesses();
    updateCpuAvgLoadCharts();
    updateRamUsageCharts();
    updateCpuUtilizationCharts();

    smoothieRamUsage.streamTo(document.getElementById("ram-usage-canvas"));
    smoothieCpuAvgLoad.streamTo(document.getElementById("cpu-avg-load-canvas"));
    smoothieCpuUtilization.streamTo(document.getElementById("cpu-util-canvas"));

    setInterval(function() {
        updateCpuAvgLoadCharts();
    }, 1500);
    setInterval(function() {
        updateRamUsageCharts();
    }, 1500);
    setInterval(function() {
        updateCpuUtilizationCharts();
    }, 1500);

    smoothieRamUsage.addTimeSeries(ramUsageLine,
        {lineWidth:2,strokeStyle:'#0000ff',fillStyle:'rgba(0,128,255,0.30)'});
    smoothieCpuUtilization.addTimeSeries(cpuUtilizationLine,
        {lineWidth:2,strokeStyle:'#0000ff',fillStyle:'rgba(0,128,255,0.30)'});
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine1mins,
        {lineWidth:2,strokeStyle:'#C7002C'});
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine5mins,
        {lineWidth:2,strokeStyle:'#08876B'});
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine15mins,
        {lineWidth:2,strokeStyle:'#147AE0'});

    $('#battery-demo-btn').click(function() {
        var battery_btn_txt = ($(this).text());
        if (battery_btn_txt == 'Start Demo') {
            $(this).text('End Demo');
            intervalListener = self.setInterval(
                function () {
                    updateBatteryInfo()
                }, 3000
            );
        } else if (battery_btn_txt == 'End Demo') {
            clearInterval(intervalListener);
            $(this).text('Start Demo');
            for (var idx = 1; idx < 5; ++idx) {
                $('#bat' + String(parseInt(idx)) + '-temp').text(' -- °C ');
                $('#bat' + String(parseInt(idx)) + '-temp').removeClass("text-danger text-success").addClass( "text-info" );
                $('#bat' + String(parseInt(idx)) + '-heat').text('Heaters: ---');
                $('#bat' + String(parseInt(idx)) + '-heat').removeClass("text-danger text-success").addClass( "text-info" );
            }
        }
    });

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

    $( '#get-logs-dialog' ).dialog({
		autoOpen: false,
	});
	$( '#get-logs-btn' ).click(function() {
		$( '#get-logs-dialog' ).dialog("open");
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
                var formInput = selectTag + '<br/><br/><center><input type="submit" value="roll back" /></center>'
                $( '#roll-back-id' ).html(formInput);
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
});
