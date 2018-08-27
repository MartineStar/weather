# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WeatherItem(scrapy.Item):
    date = scrapy.Field()
    city = scrapy.Field()
    weather = scrapy.Field()
    uv = scrapy.Field()
    blood_sugar = scrapy.Field()
    dressing = scrapy.Field()
    car_cleanning = scrapy.Field()
    air_pollution = scrapy.Field()

class WeatherItem2(scrapy.Item):
    city = scrapy.Field()
    date = scrapy.Field()
    day = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    winddirection = scrapy.Field()

