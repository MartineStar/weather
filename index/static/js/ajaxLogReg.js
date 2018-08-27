/**
 * Created by Administrator on 2018/7/6.
 */

$(function () {
    var inputusername = $('#i1');
    var upwd = $('#i2').val();
    var cpwd = $('#i3').val();
    var note = $('#i4').val();
    var spanusername = $('#notice');
    inputusername.blur(function () {
        var name = inputusername.val();
		if (name.length!=0) {
			if(name.length!=0 && cpwd.length!=0 && note.length!=0 && inputusername.length!=0){
				console.log('不需要提交')
			}
			else{
				$.ajax({
				url: "/register/",
				data: {"username": name, 'type': 'check'},
				type: 'post',
				datatype: "json",
				success: function (data) {
					data = JSON.parse(data);
					if (data['msg'] == 'Fail') {
						console.log('fail');
						spanusername.text('用户已被占用');
						spanusername.css({'color': 'red'})
					}
					else {
						console.log('success');
						spanusername.text('用户可以使用');
						spanusername.css({'color': 'green'})
					}
				},
				error: function (err) {
					console.log(err);
				}
			});
			}
		}
    })
})

function test() {
	var inputusername = $('#i1');
	var name = inputusername.val();
    $.ajax({
        url: "/register/",
        data: {"username": name, 'type':'notesend'},
        type: 'post',
        datatype: "json",
		success: function(data) {
			console.log(data);}
        })
}

function messagesubmit() {
	var name = $('#mes-name').val()
	var email = $('#mes-email').val()
	var message = $('#mes-text').val()
	 $.ajax({
        url: "/message/",
        data: {"name": name, 'email':email, 'message':message, 'type':'message'},
        type: 'post',
        datatype: "json",
		success: function() {
			alert('提交成功，我们会尽快处理')}
        })
}

function regist() {
    var user = $('#i1').val();
    var upwd = $('#i2').val();
    var cpwd = $('#i3').val();
    var note = $('#i4').val();
    console.log(1111)
    var spanusername = $('#notice').text();
    if (user.length === 0 || upwd.length === 0 || cpwd.length === 0 || note.length === 0) {
        return false;
    }
    if (upwd != cpwd) {
        return false
    }
    console.log(666);
    //
    // if(spanusername != '用户已被占用') {
    $.ajax({
        async: false,
        url: "/register/",
        data: {"user": user, 'upwd': upwd, 'note': note, 'type': 'rg'},
        type: 'post',
        datatype: "json",
        success: function (data) {
            data = JSON.parse(data);
            if (data['msg'] == 'Fail') {
                console.log('fail');
                spanusername.text('注册失败，验证码输入有误！');
                spanusername.css({'color': 'red'})
            }
            else {
                window.location.href = "//127.0.0.1:8000/login/";
                spanusername.text('注册成功！');
                spanusername.css({'color': 'green'})
            }
        }
    })
}

function voice() {
    $('#ttt1').css('color', 'red');
    var city = $('#city');
    var cTemperature = $('#temperature');
    var cHumidity = $('#humidity');
    var cWind = $('#windDirection');
    var cAir = $('#airQuailty');
    var cWeather = $('.weather22');
    var cLowTemperature = $('#night');
    var cHighTemperature = $('#sunshine');
	 $.ajax({
        url: "/voice/",
        data: {"name": 'voice'},
        type: 'post',
        datatype: "json",
		success: function(data1) {
			// alert('请稍等');
            $('#ttt1').css('color', 'white');
            // var data = data1
            if(data1['city'] != 'NO'){
                var data = JSON.parse(data1)
                $('#ttt1').css('color', 'white');
                // var data = data1;
                console.log(data['city']);
                console.log(data.city);
                var temperature_lower = data['temperature_lower'];
                var temperature_higher = data['temperature_higher'];
                var windDireaction = data['windDireaction']
                var array = data['array'];
                halfMonth(array, temperature_lower, temperature_higher);
                var temperature = data["temperature"];
                var humidity = data["humidity"];
                var air = data["air"];
                var weather = data['weather']
                oneday(air, humidity, temperature);

                city.text(data['city']);
                cTemperature.text(temperature[4] + '℃');
                cHumidity.text(humidity[4] + '%');
                cWind.text(windDireaction);
                cAir.text(air[4]);
                cWeather.text(weather);
                cHighTemperature.text(temperature_higher[0] + '℃');
                cLowTemperature.text(temperature_lower[0] + '℃')
                var value = $('.weather22').text();
                if (value.indexOf('雷') != -1){
                    var v1 = 'lei.png';
                }
                else if (value.indexOf('雨') != -1){
                    var v1 = 'yu.png';
                }
                else if (value.indexOf('晴') != -1){
                    var v1 = 'qing.png';
                }
                else if (value.indexOf('雪') != -1){
                    var v1 = 'xue.png';
                }
                else if (value.indexOf('阴') != -1){
                    var v1 = 'yin.png';
                }

                $('#morning-img').attr('src','/static/img/tq/'+v1);
                $('#night-img').attr('src','/static/img/tq/'+v1);
            }
            else{
                alert('清不清楚，请重新说');
            }

        }
        })
}


