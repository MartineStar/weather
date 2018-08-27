# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from weather.items import WeatherItem2

import pymongo
import pymysql
from util.weather.weather import settings
from util.weather.weather.items import WeatherItem,WeatherItem2
from datetime import datetime

class WeatherPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        if isinstance(item, WeatherItem2):
            month = datetime.now().month
            temp = str(month) + '月'
            item = dict(item)
            # print(settings.MONGO_DB)
            client = pymysql.connect(host=settings.MYSQL_HOST, port=settings.MYSQL_PORT, user=settings.MYSQL_USER, db=settings.MONGO_DB, password=settings.MYSQL_PASSWORD,charset="utf8")
            cursor = client.cursor()
            # print(cursor)
            # print(666666666666666)
            for i in range(7):
                sql = "INSERT INTO weather(date,day,temperature,weather,winddirection,city) VALUES('{}','{}','{}','{}','{}','{}')".format(temp + item["date"][i],item["day"][i],item["temperature"][i],item["weather"][i],item["winddirection"][i],item["city"][0])
                cursor.execute(sql)
                client.commit()
            cursor.close()
            client.close()
            return item


class WeatherPipeline1(object):
    def process_item(self, item, spider):
        # print(item)
        if isinstance(item, WeatherItem):
            # print(22222222222222)
            client = pymongo.MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
            db = client[settings.MONGO_DB]
            collection = db[settings.MONGO_SHEET]
            # print(len(item))
            collection.insert(dict(item))
            # print("==============================")
            # print(item)
            return item






