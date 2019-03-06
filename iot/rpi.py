#!/usr/bin/python3

import Adafruit_DHT
import json
import requests
import os
import time

#hellou

def readSensors():
    pin = os.environ["GPIO"]

    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    sensors = {
        "message": "Humidity: " + str(humidity) + " Temperature: " + str(temperature)
        
    }

    return sensors 

if __name__ == "__main__":
    url = os.environ["ENDPOINT"]
    print(url)

    sensorsJson = json.dumps(readSensors(), sort_keys=True, indent=2)

    print("------")
    print(sensorsJson)

    headers = {'content-type': 'application/json'}
    requests.post(url, data=sensorsJson, headers=headers)
