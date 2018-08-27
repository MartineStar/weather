# -*- coding: utf-8 -*-
import scrapy
from util.weather.weather.items import WeatherItem
import re
import time

class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherspider'
    allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/textFC/hb.shtml#']
    l = []
    select_time = ""
    custom_settings = {
        'ITEM_PIPELINES': {
            'weather.weather.pipelines.WeatherPipeline1': 300,
        }
    }

    def parse(self, response):
        """爬取首页，获取各省各直辖市的链接"""
        city_list = response.xpath('//div[@class="lqcontentBoxheader"]//li/a/@href').extract()
        if city_list:
            for i in city_list:
                url = "http://www.weather.com.cn" + i
                # print(url)
                yield scrapy.Request(url=url, callback=self.cityHandler)
            # url = "http://www.weather.com.cn/textFC/beijing.shtml"
            # yield scrapy.Request(url=url, callback=self.cityHandler)
        else:
            print("首页各城市链接获取失败")

    def cityHandler(self, response):
        """获取进入各省会城市和直辖市的链接"""
        detail_link = response.xpath("//div[@class='conMidtab3'][1]/table/tr/td[2]/a/@href").extract()[0]
        if detail_link:
            # self.city_name= response.xpath("//div[@class='conMidtab3'][1]/table/tr/td[2]/a/text()").extract()[0]
            self.select_time = response.xpath('//li[@class="selected"]/text()').extract()[0]
            self.select_time = self.select_time[5:9]
            # print(detail_link)
            yield scrapy.Request(url=detail_link, callback=self.msgHandler)
        else:
            print("各城市详情链接获取失败")

    def msgHandler(self,response):
        """爬取页面详细部分的内容"""
        item = WeatherItem()
        # 获取响应的文本字符串
        result = response.text
        # eachday_1 = re.findall("<div.*?biggt.*?winl.*?script>.*?hour3data=(.*?)</script>",result,re.S)[0]
        # eachday_1 = eval(eachday_1)["1d"]
        # 正则表达式获取响应中的script标签内容，包含24个小时的爬取信息
        eachday_2 = re.findall(r'<div.*?biggt.*?winl.*?observe24h_data.*?"od2".*?\[(.*?)\].*?</script>',result,re.S)[0]
        # 将元组类型的字符串转化元组
        eachday_2 = eval(eachday_2)
        # 获取各页面的省会城市/直辖市
        city_1 = response.xpath('//div[@class="crumbs fl"]/a[1]/text()').extract()
        city_2 = response.xpath('//div[@class="crumbs fl"]/a[2]/text()').extract()
        # 获取页面的生活指数类型的列表
        life_index = response.xpath('//div[@class="hide show"]/ul[@class="clearfix"]//em/text()').extract()
        # 获取页面生活指数值的列表
        index_strength = response.xpath('//div[@class="hide show"]/ul[@class="clearfix"]//span/text()').extract()
        # 获取类型对应方法的的列表
        life_method = response.xpath('//div[@class="hide show"]/ul[@class="clearfix"]//p/text()').extract()
        # 列表处理，剔除不需要的数据
        life_method.pop(1)
        life_index.pop(1)
        index_strength.pop(1)
        index_strength.pop(1)
        item["uv"] = [life_index[0],index_strength[0],life_method[0]]
        item["blood_sugar"] = [life_index[1],index_strength[1],life_method[1]]
        item["dressing"] = [life_index[2],index_strength[2],life_method[2]]
        item["car_cleanning"] = [life_index[3],index_strength[3],life_method[3]]
        item["air_pollution"] = [life_index[4],index_strength[4],life_method[4]]
        # 加判断，统一存入数据库的值
        for i in eachday_2:
            if i["od25"] is "null" or i["od25"] == "":
                a = "null"
            else:
                a = i['od24'] + i["od25"] + "级"
            if i["od22"] is "null" or i["od22"] == "":
                b = "null"
            else:
                b = i["od22"] + "℃"
            if i["od27"] is "null" or i["od27"] == "":
                c = "null"
            else:
                c = i["od27"] + "%"
            if i["od28"] == "":
                d = "null"
            else:
                d = i["od28"]
            self.l.append({i["od21"]:[{'airQuality':d},{'humidity':c},{'temperature':b},{'windDirection':a}]})
        item["weather"] = self.l[1:25][-1::-1]
        # 对存入数据库的值加判断
        if city_1[0] in ["香港", "北京", "重庆", "上海", "天津", "澳门"]:
            item["city"] = city_1[0]
        else:
            item["city"] = city_2[0]
        item["date"] = self.select_time
        self.l = []
        print(item)
        return item















