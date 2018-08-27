// 基于准备好的dom，初始化echarts实例
//温度
var temperature = [20, 18, 17, 20, 22, 28, 30, 35];
//湿度
var humidity = [78, 80, 82, 88, 84, 70, 56, 50];
//空气质量
var air = [50, 78, 56, 45, 34, 65, 78, 43];

var myChart = echarts.init(document.getElementById('one-day-echart'));
var option = {
    title:{
        show:true,
        text:"今日天气走势",
        textStyle:{
            color: '#ccc',
            fontSize:30,
        }
    },
    toolbox: {
        show: true,
        x: "right",
        orient: "horizontal",
        feature: {
            dataView: {show: true},
            magicType: {type:['bar','line']},
            restore: {},
            saveAsImage: {
                type:'png',
            },
        },
        iconStyle:{
            color:"#ccc",
        }
    },
    grid:{
        show:false
    },
    tooltip: {
        show: true,
        trigger: 'axis',

    },
    legend: {
        data: ["温度", "湿度","空气质量"],
        x:"center",
        y:20,
        textStyle:{
            color:"#b4b4b4",
            fontSize:16,
        },
        selected: {"温度": true, "湿度": true, "空气质量": true}
    },
    xAxis:[{
        type:"category",
        name: "时间(/hour)",
        nameTextStyle:{
            fontSize:14,
            color: "#ccc",
        },
        axisLine:{
            lineStyle:{
                color: "#ccc",
            },
        },
        splitLine:{
            show:false
        },
        axisLabel : {
                    textStyle: {
                        color: '#b4b4b4'
                    }
        },
        data:["0","3","6","9","12","15","18","21"]
        }
    ],
    yAxis:[{
        type:"value",
        splitLine:{
            show:false
        },
        axisLine:{
            lineStyle:{
                color: "#ccc",
            },
        },
        axisLabel : {
                    textStyle: {
                        color: '#b4b4b4'
                    }
        },
        }
    ],
    series : [
        {
            "name":"温度",
            "type":"bar",
            "data":temperature,//要修改的内容
            color: "#ca8622",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
            markLine: {
                color:"#ccc",
                silent: true,
                data: [{
                    yAxis: 10
                }, {
                    yAxis: 20
                }, {
                    yAxis: 30
                },]
            },
        },
        {
            "name": "湿度",
            "type": "bar",
            "data": humidity, //要修改的内容
            color: "#749f83",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
        },
        {
            "name": "空气质量",
            "type": "bar",
            "data": air, //要修改的内容
            color: "#d48265",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
        }
    ]
};
// ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3']
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);

function oneday(air, humidity, temperature) {
    var myChart = echarts.init(document.getElementById('one-day-echart'));
var option = {
    title:{
        show:true,
        text:"今日天气走势",
        textStyle:{
            color: '#ccc',
            fontSize:30,
        }
    },
    toolbox: {
        show: true,
        x: "right",
        orient: "horizontal",
        feature: {
            dataView: {show: true},
            magicType: {type:['bar','line']},
            restore: {},
            saveAsImage: {
                type:'png',
            },
        },
        iconStyle:{
            color:"#ccc",
        }
    },
    grid:{
        show:false
    },
    tooltip: {
        show: true,
        trigger: 'axis',

    },
    legend: {
        data: ["温度", "湿度","空气质量"],
        x:"center",
        y:20,
        textStyle:{
            color:"#b4b4b4",
            fontSize:16,
        },
        selected: {"温度": true, "湿度": true, "空气质量": true}
    },
    xAxis:[{
        type:"category",
        name: "时间(/hour)",
        nameTextStyle:{
            fontSize:14,
            color: "#ccc",
        },
        axisLine:{
            lineStyle:{
                color: "#ccc",
            },
        },
        splitLine:{
            show:false
        },
        axisLabel : {
                    textStyle: {
                        color: '#b4b4b4'
                    }
        },
        data:["0","3","6","9","12","15","18","21"]
        }
    ],
    yAxis:[{
        type:"value",
        splitLine:{
            show:false
        },
        axisLine:{
            lineStyle:{
                color: "#ccc",
            },
        },
        axisLabel : {
                    textStyle: {
                        color: '#b4b4b4'
                    }
        },
        }
    ],
    series : [
        {
            "name":"温度",
            "type":"bar",
            "data":temperature,//要修改的内容
            color: "#ca8622",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
            markLine: {
                color:"#ccc",
                silent: true,
                data: [{
                    yAxis: 10
                }, {
                    yAxis: 20
                }, {
                    yAxis: 30
                },]
            },
        },
        {
            "name": "湿度",
            "type": "bar",
            "data": humidity, //要修改的内容
            color: "#749f83",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
        },
        {
            "name": "空气质量",
            "type": "bar",
            "data": air, //要修改的内容
            color: "#d48265",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
        }
    ]
};
// ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3']
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
}