from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=20, verbose_name='用户')
    upwd = models.CharField(max_length=20, verbose_name='密码')
    userCreateDate = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    userUpdateDate = models.DateTimeField(default=timezone.now, verbose_name='修改时间')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class Feedback(models.Model):
    accountName = models.CharField(max_length=100,verbose_name='用户名')
    email = models.EmailField(verbose_name='用户邮箱')
    suggestion = models.TextField(verbose_name='用户反馈意见')
    dateTime = models.DateTimeField(default=timezone.now, verbose_name='反馈时间')

    def __str__(self):
        return self.accountName

    class Meta:
        db_table = 'feedback'
        verbose_name = '用户意见反馈'
        verbose_name_plural = verbose_name

class SevenDayWeather(models.Model):
    city  = models.CharField(max_length=20, verbose_name='城市')
    date = models.CharField(max_length=40, verbose_name='日期')
    day = models.CharField(max_length=20, verbose_name='日子')
    temperature = models.CharField(max_length=30, verbose_name='温度')
    weather = models.CharField(max_length=60, verbose_name='天气情况')
    winddirection = models.CharField(max_length=60, verbose_name='风向')

    def __str__(self):
        return self.city

    class Meta:
        db_table = 'weather'
        verbose_name = '7天气温情况'
        verbose_name_plural = verbose_name

class SaveCode(models.Model):
    user = models.CharField(max_length=100,verbose_name='用户名')
    vertificationCode = models.CharField(max_length=100,verbose_name='验证码')
    dateTime = models.DateTimeField(default=timezone.now, verbose_name='反馈时间')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'verticode'
        verbose_name = '验证码信息存储'
        verbose_name_plural = verbose_name
