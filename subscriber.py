"""This script is an example of subscriber to CloudMQTT Broker"""

from urllib.parse import urlparse
import os
import paho.mqtt.client as mqtt

# Define event callbacks
def on_connect(mosq, obj, rc):
    print('Reconnect: {}'.format(str(rc)))

def on_message(mosq, obj, msg):
    # message = str(msg.payload)
    print('Topic: {}/{}'.format(msg.topic, msg.payload.decode('utf-8')))


def on_subscribe(mosq, obj, mid, granted_qos):
    print('Subscribed: {}, QoS: {}'.format(str(mid), str(granted_qos)))

def on_log(mosq, obj, level, string):
    print(string)

#username = 'ketawadewa'
#password = '1234'
host_url = 'mqtt.eclipse.org'
host_port = 1883 # do not type string, but change to integer

mqttc = mqtt.Mosquitto()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', host_url)
url = urlparse(url_str)

# Connect
#username = 'ketawadewa'
#password = '1234'
#mqttc.username_pw_set(username, password)
mqttc.connect(url.hostname, url.port)

# Subscribe to a topic
mqttc.subscribe('python/170010169/I Gede Febri Purnama Putra')

# Continue the network loop, exit when an error occurs

client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('mqtt.eclipse.org', 1883)

client.subscribe('myhome/+/kitchen')
rc = 0
while rc == 0:
    rc = mqttc.loop()
print('Reconnect: ' + str(rc))