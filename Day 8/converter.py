import requests
import datetime
import json


def getvalues():
    f = open("./currency.txt", "rt")
    value = f.readline()
    f.close()
    return json.loads(value.replace("'", '"')) 

def updatevalues():
    response = requests.get("https://currencyapi.net/api/v1/rates?key=8rWT755nh2zzX4Je8p9gnSDYTcCh9YPV8RSx&base=USD")
    data = response.json()['rates']

    f = open("./currency.txt", "wt")
    f.write(str(data))
    f.close()

    return datetime.datetime.now()

def change(n, last_update_time):
    time_dff = datetime.datetime.now() - last_update_time
    if time_dff > datetime.timedelta(seconds=600, microseconds=658665):
        last_update_time = updatevalues()
    value = n*getvalues()['INR']
    return last_update_time, value

last_update_time = updatevalues()
while(True):
    n = float(input("Enter usd to convert into INR : "))
    last_update_time, value = change(n, last_update_time)
    print(value)