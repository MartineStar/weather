from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ['user', 'userCreateDate', 'userUpdateDate']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['accountName', 'email', 'suggestion']
    list_display_links = ['accountName', 'email']
    search_fields = ['accountName', 'email']
    date_hierarchy = 'dateTime'

class SevenDayWeatherAdmin(admin.ModelAdmin):
    list_display = ['city', 'temperature', 'weather', 'winddirection', 'date']
    list_display_links = ['city']
    search_fields = ['city', 'date']
    list_filter = ['city']

admin.site.register(User, UserAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(SevenDayWeather, SevenDayWeatherAdmin)

