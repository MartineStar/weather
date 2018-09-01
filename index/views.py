import datetime
import json
import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from util import noteSend, myaip, mongouse

# Create your views here.
def indexViews(request):
    # if request.method == 'GET':
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    theDate = str(month) + '月' + str(day) + '日'
    city = '广州'
    info = SevenDayWeather.objects.get(city=city,date=theDate)
    t1 = info.temperature.split('/')[1]
    t2 = info.temperature.split('/')[0] + '℃'
    # print(t1, t2)
    temperature = (int(t1.split('℃')[0]) + int(t2.split('℃')[0])) // 2
    windDireaction = info.winddirection
    weather = info.weather
    oneday = mongouse.conveydata(city)
    air = str(oneday['air'][4])
    humidity = str(oneday['humidity'][4]) + '%'
    return render(request, 'index.html', locals())


def registerViews(request):
    if request.method == 'POST':
        typ = request.POST.get('type', None)
        # print(typ,'ooooooooooooo')
        if typ == 'check':
            # print(111)
            user = request.POST.get('username', None)
            userInfo = User.objects.filter(user=user)
            if userInfo:
                status = 'Fail'
                return HttpResponse(json.dumps({"msg": status}, ensure_ascii=False))
            else:
                status = 'OK'
                return HttpResponse(json.dumps({"msg": status}, ensure_ascii=False))
        elif typ == 'notesend':
            mobile = request.POST.get('username', None)
            if mobile:
                if re.findall(r'[0-9]{11}', mobile):
                    vcode = noteSend.noteSend(mobile)
                    # print(vcode, mobile)
                    status = 'OK'
                    dic = {
                        'user': mobile,
                        'vertificationCode':vcode
                    }
                    obj = SaveCode(**dic)
                    obj.save()
                    return HttpResponse(json.dumps({"msg": status}, ensure_ascii=False))
            status = 'NO'
            return HttpResponse(json.dumps({"msg": status}, ensure_ascii=False))
        elif typ == "rg":
            #  {"user": user, 'upwd': upwd, 'type': 'register', 'note': note}
            user = request.POST['user']
            upwd = request.POST['upwd']
            note = request.POST['note']
            if SaveCode.objects.filter(user=user, vertificationCode=note):
                if User.objects.filter(user=user):
                    print('亲，有提示噢！')
                    return HttpResponse(json.dumps({"msg": 'FAIL'}, ensure_ascii=False))
                else:
                    print('chenggong')
                    dic = {
                        'user': user,
                        'upwd': upwd,
                    }
                    obj = User(**dic)
                    obj.save()
                    print('账号添加成功')
                    return HttpResponse(json.dumps({"msg": 'OK'}, ensure_ascii=False))
            else:
                print('false')
                return HttpResponse(json.dumps({"msg": 'FAIL'}, ensure_ascii=False))
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def loginViews(request):
    if request.method == 'POST':
        user = request.POST['user']
        upwd = request.POST['upwd']
        userInfo = User.objects.filter(user=user, upwd=upwd)
        if userInfo:
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def feedbackViews(request):
    typ = request.POST.get('type', None)
    if request.method == 'POST':
        if typ == 'message':
            print(request.POST)
            accountName = request.POST.get('name', '佚名')
            email = request.POST['email']
            message = request.POST.get('message', '没有填写意见')
            dic = {
                'accountName': accountName,
                'email': email,
                'suggestion': message
            }
            obj = Feedback(**dic)
            obj.save()
            return HttpResponse(json.dumps({"msg": 'OK'}, ensure_ascii=False))
    else:
        return HttpResponseRedirect('/#contact/message')


def voiceViews(request):
    # print(request.POST)
    try:
        city = myaip.startaip()
        print(city)
        infos = []
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        theDate = str(month) + '月' + str(day) + '日'
        datas = SevenDayWeather.objects.filter(city=city).order_by('date')
        theDateInfo = SevenDayWeather.objects.get(city=city, date=theDate)
        windDireaction = theDateInfo.winddirection
        weather = theDateInfo.weather
        # print(windDireaction)
        for data in datas:
            if int(data.date.split('月')[1].split('日')[0]) < 10:
                info = '0' + data.date.split('月')[1].split('日')[0] + data.temperature
            else:
                info = data.date.split('月')[1].split('日')[0] + data.temperature
            infos.append(info)
        infos = sorted(infos)
        array = []
        temperature_lower = []
        temperature_higher = []
        for info in infos:
            array.append(int(info[0:2]))
            all = info[2:].split('/')
            lower = all[1].split('℃')[0]
            high = all[0].split('℃')[0]
            temperature_lower.append(int(lower))
            temperature_higher.append(int(high))
        # print(infos)
        oneday = mongouse.conveydata(city)
        # print(oneday)


        dataAll = {'array': array, 'temperature_lower': temperature_lower, 'temperature_higher': temperature_higher,
                   'air': oneday['air'], 'humidity': oneday['humidity'], 'temperature': oneday['temperature'],
                   'windDireaction': windDireaction, 'weather': weather, 'city':city}
        # print(dataAll)
        return HttpResponse(json.dumps(dataAll, ensure_ascii=False))
    except Exception as e:
        print(e)
        return HttpResponse({'city':'NO'})


def dataViews(request):
    print(request.POST)
    infos = []
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    theDate = str(month) + '月' + str(day) + '日'
    city = request.POST.get('cityName', None)
    if city:
        datas = SevenDayWeather.objects.filter(city=city).order_by('date')
        theDateInfo = SevenDayWeather.objects.get(city=city,date=theDate)
        windDireaction = theDateInfo.winddirection
        weather = theDateInfo.weather
        # print(windDireaction)
        for data in datas:
            if int(data.date.split('月')[1].split('日')[0])<10:
                info = '0' + data.date.split('月')[1].split('日')[0] + data.temperature
            else:
                info = data.date.split('月')[1].split('日')[0] + data.temperature
            infos.append(info)
        infos = sorted(infos)
        array = []
        temperature_lower = []
        temperature_higher = []
        for info in infos:
            array.append(int(info[0:2]))
            all = info[2:].split('/')
            lower = all[1].split('℃')[0]
            high = all[0].split('℃')[0]
            temperature_lower.append(int(lower))
            temperature_higher.append(int(high))
        # print(infos)
        oneday = mongouse.conveydata(city)
        # print(oneday)
    dataAll = {'array':array,'temperature_lower':temperature_lower,'temperature_higher':temperature_higher,
               'air':oneday['air'],'humidity':oneday['humidity'],'temperature':oneday['temperature'],
               'windDireaction':windDireaction, 'weather':weather}
    # print(dataAll)
    return HttpResponse(json.dumps(dataAll, ensure_ascii=False))


