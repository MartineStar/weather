from scrapy import cmdline
# from subprocess import Popen
# import sched
# import time
# import os

def spiderstart():
    cmdline.execute("scrapy crawl weatherspider".split())
    cmdline.execute("scrapy crawl weekweatherspider".split())
# print("===========================")
# time.sleep(6)


# 利用模块
# Popen('scrapy crawlall')
# print("===========================")
# time.sleep(3)


# #初始化sched模块的scheduler类
# #第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
# schedule = sched.scheduler(time.time, time.sleep)
# #被周期性调度触发的函数
# def func():
#     os.system("scrapy crawl weatherspider")
#     os.system("scrapy crawl weekweatherspider")
#     print("==============================")
# def perform1(inc):
#     schedule.enter(inc,0,perform1,(inc,))
#     func()    # 需要周期执行的函数
# def mymain():
#     schedule.enter(0,0,perform1,(60,))
#
if __name__ == "__main__":
    spiderstart()
#     schedule.run()  # 开始运行，直到计划时间队列变成空为止




