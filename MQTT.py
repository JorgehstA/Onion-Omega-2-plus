import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):  #Log Callback (it's not necessary)
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):   #Connect Callback
    if (rc==0):
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0): #Disconnect callback
    print("Disconnected result code "+str(rc))

def on_message(client, userdata, msg):  #Shows the message
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8", "ignore"))
    print("message receiver: ", m_decode)

broker="test.mosquitto.org"  #Chosen broker
#broker="broker.hivemq.com"
#broker="iot.eclipse.org"
#broker="192.168.1.206"

client = mqtt.Client("python9")  #Client name

client.on_connect=on_connect 
client.on_disconnect=on_disconnect
#client.on_log=on_log
client.on_message=on_message

print("Connecting to broker: ", broker)
client.connect(broker)
client.loop_start()
client.subscribe("house/sensor1")
client.publish("house/sensor1", "It works")
time.sleep(4)

client.loop_stop()
client.disconnect() 