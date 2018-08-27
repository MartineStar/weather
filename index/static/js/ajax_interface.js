
function ajax_interface(elem_class) {
    var c_name = $(elem_class).val();
    var city = $('#city');
    var cTemperature = $('#temperature');
    var cHumidity = $('#humidity');
    var cWind = $('#windDirection');
    var cAir = $('#airQuailty');
    var cWeather = $('.weather22');
    var cLowTemperature = $('#night');
    var cHighTemperature = $('#sunshine');
    console.log(c_name);
    $.ajax({
        url: "/getdata/",
        type:"POST",
        dataType:'json',
        data:{'cityName':c_name},
        success:function(data) {
            console.log(data);
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
            city.text(c_name);
            cTemperature.text(temperature[4] + '℃');
            cHumidity.text(humidity[4] + '%');
            cWind.text(windDireaction);
            cAir.text(air[4]);
            cWeather.text(weather);
            cHighTemperature.text(temperature_higher[0] + '℃');
            cLowTemperature.text(temperature_lower[0] + '℃')
            // temperature_avg = data['temperature_avg'];
            // humidity_avg = data['humidity_avg'];
            // air_avg = data['air_avg'];
            // console.log('tq6666')
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
    })
}

function get(elem_class) {
        ajax_interface(elem_class);
    }