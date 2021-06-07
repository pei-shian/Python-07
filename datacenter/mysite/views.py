from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post
import json
import requests

def index(request):
	posts = Post.objects.all()
	myname = "月降雨量統計"
	data = [i for i in range(1,43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number = data[6]
	return render(request,'index.html',locals())

def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:

		
		return redirect("/")
	return render(request,"showpost.html", locals())
def weather(request, id):
    token = 'CWB-CF13E86E-3C39-4364-B74C-A79F63F31AE0'
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/C-B0025-001?Authorization=' + token + '&format=JSON&sort=dataTime&statistics=true" -H  "accept: application/json'
    Data = requests.get(url)
    DATA = json.loads(Data.text)
    DATA_2 = DATA['records']['location']
    all_local_weather = []
    key = {4:'台中', 7:'新竹'}
    for i in key:
    	if i == key:
    		local = key[i]
    		print(local)
    for item in DATA_2:
        # print(item['stationObsTimes']['stationObsTime'][-1])
        # print(item['stationObsTimes']['stationObsTime'][-1]['dataDate'])
        # print(item['stationObsTimes']['stationObsTime'][-1]['weatherElements']['precipitation'])
        # print(item['station']['stationName'])
        local_weather =  {
            "rainfall": item['stationObsTimes']['stationObsTime'][-1]['weatherElements']['precipitation'],
            'local': item['station']['stationName'],
            "time": item['stationObsTimes']['stationObsTime'][-1]['dataDate']}
        all_local_weather.append(local_weather)
    print(all_local_weather)
    return render(request,'weather.html',locals())