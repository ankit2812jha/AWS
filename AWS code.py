#!/usr/bin/python

import json
import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform

def on_connectpub(client, userdata, flags, rc):
    print("Connected to AWS cloud broker service: " + str(rc) )
    for i in range(5):
        data_to_cloud = json.dumps({
                          "SerialNo":1,
                          "DeviceID": "007",
                          "Location": "Home",
                          "Temperature":25
                          })
        mqttcpub.publish("Temp", data_to_cloud, qos=0)
        print("msg sent: " + data_to_cloud)


if __name__=="__main__":

    #To create two client object
    mqttcpub=paho.Client()   # Publisher to AWS MQTT Broker
    
    
    mqttcpub.on_connect=on_connectpub



    # Providing AWS MQTT broker information
    awshost = "-ats.iot.us-west-2.amazonaws.com"  #AWS IoT console -> Settings
    awsport = 8883  #MQTT +TLS  ---- To ensure communication security
    clientId = "MyPi_2020"  ## Unique ID assigned by you to your device
    thingName = "MyPi_2020"
    caPath = r"/home/pi/AWS2020/root.ca.pem"
    certPath = r"/home/pi/AWS2020/MyPi_2020.cert.pem"
    keyPath = r"/home/pi/AWS2020/MyPi_2020.private.key"

    mqttcpub.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    mqttcpub.connect(awshost, awsport, keepalive=60)

    # Runing or listening mode
    mqttcpub.loop_start()
