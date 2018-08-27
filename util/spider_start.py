# 在项目外用脚本启动爬虫
from multiprocessing import Pool
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from util.weather.weather.items import WeatherItem,WeatherItem2
from util.weather.weather.spiders.weatherspider import WeatherspiderSpider
from util.weather.weather.spiders.weekweatherspider import WeekweatherspiderSpider
from util.weather.weather.pipelines import WeatherPipeline1,WeatherPipeline
from scrapy.settings import Settings


# 运行蜘蛛外项目必须根据需要创建一个通用设置对象并填充它(见内置设定参考手册可用的设置),而不是使用配置由get_project_settings返回。
def run_spider(spider):
    settings = Settings({
        # 蜘蛛仍然可以引用他们的名字如果SPIDER_MODULES设置模块,Scrapy应该找蜘蛛。
        # 否则,将蜘蛛CrawlerRunner类作为第一个参数。
        'BOT_NAME' : 'util.weather.weather',
        'SPIDER_MODULES': ['util.weather.weather.spiders.weatherspider', 'util.weather.weather.spiders.weekweatherspider'],
        'NEWSPIDER_MODULE' : 'util.weather.weather.spiders',
        'ROBOTSTXT_OBEY': True,

        # 设置包头
        'DEFAULT_REQUEST_HEADERS' : {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en'},

        # 启用pipelines组件
        'ITEM_PIPELINES': {
            'util.weather.weather.pipelines.WeatherPipeline1': 300,
            'util.weather.weather.pipelines.WeatherPipeline': 200,},

        # 中间件
        'DOWNLOADER_MIDDLEWARES' : {
        'util.weather.weather.middlewares.WeatherDownloaderMiddleware': 543,
        'util.weather.weather.middlewares.ChangeUseAgent': 300,},

        'CONCURRENT_REQUESTS': 16,  # 同时处理16个请求
        # 'DOWNLOAD_DELAY': 1 ,       # 每下载一个页面延迟一秒钟

        # 日志文件
        'LOG_FILE' : 'weather.log',
        'LOG_LEVEL' : 'DEBUG',
    })
    runner = CrawlerRunner(settings)
    d = runner.crawl(spider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    # print('Spider Over')
    return 0


def main(spiders):
    p = Pool(processes = 2)
    for spider in spiders:
        p.apply_async(func=run_spider, args=(spider,))
    p.close()
    p.join()


def start_spider():
    # 爬虫启动的调用
    spiders = ['weekweatherspider', 'weatherspider']
    # spiders = ['weekweatherspider']
    main(spiders)

if __name__ == '__main__':
    start_spider()