
// 基于准备好的dom，初始化echarts实例
//温度
var temperature_lower = [20, 18, 17, 20, 22, 28, 30, 35,20, 18, 17, 20, 22, 28, 30];
//湿度
var temperature_higher = [78, 80, 82, 88, 84, 70, 56, 50,78, 80, 82, 88, 84, 70, 56];
//天数
var array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
var myChart = echarts.init(document.getElementById('half-month-echart'));
var option = {
    title:{
        show:true,
        text:"近15日天气走势",
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
            dataZoom:{show:true},
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
        data: ["最低温", "最高温",],
        x:"center",
        y:20,
        textStyle:{
            color:"#b4b4b4",
            fontSize:16,
        },
        selected: {"最低温": true, "最高温": true}
    },
    xAxis:[{
        type:"category",
        name: "时间(/day)",
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
        data: array,
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
            "name":"最低温",
            "type":"line",
            "data":temperature_lower,//要修改的内容
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
            "name": "最高温",
            "type": "line",
            "data": temperature_higher, //要修改的内容
            color: "#749f83",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
            markLine: {
                color:"#ccc",
                silent: true,
            },
        },
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);


function halfMonth(array, temperature_lower, temperature_higher) {
    var myChart = echarts.init(document.getElementById('half-month-echart'));
var option = {
    title:{
        show:true,
        text:"近15日天气走势",
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
            dataZoom:{show:true},
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
        data: ["最低温", "最高温",],
        x:"center",
        y:20,
        textStyle:{
            color:"#b4b4b4",
            fontSize:16,
        },
        selected: {"最低温": true, "最高温": true}
    },
    xAxis:[{
        type:"category",
        name: "时间(/day)",
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
        data: array,
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
            "name":"最低温",
            "type":"line",
            "data":temperature_lower,//要修改的内容
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
            "name": "最高温",
            "type": "line",
            "data": temperature_higher, //要修改的内容
            color: "#749f83",
            markPoint: {
                data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'},
                ]
            },
            markLine: {
                color:"#ccc",
                silent: true,
            },
        },
    ]
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
}


