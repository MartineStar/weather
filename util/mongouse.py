from pymongo import MongoClient
import json

def conveydata(city):
    client = MongoClient('127.0.0.1',27017)
    db = client['weather']
    collection = db['total']
    airQuality = []
    humidity = []
    temperature = []
    jsondocument = {}
    cursors = collection.find({'city':city},{'id':0})
    client.close()
    for i in range(8):
        p = cursors[0]['weather'][i].values()
        for infos in p:
            airQuality.append(int(infos[0]['airQuality']))
            humidity.append(int(infos[1]['humidity'].split('%')[0]))
            temperature.append(int(infos[2]['temperature'].split('℃')[0]))
    jsondocument['air'] = airQuality
    jsondocument['temperature'] = temperature
    jsondocument['humidity'] = humidity
    return jsondocument

if __name__ == '__main__':
    data = conveydata('广州')
    print(data)
    print(data['air'])