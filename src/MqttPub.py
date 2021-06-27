import paho.mqtt.client as mqtt 

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.publish("BQMS/new_ticket", "99")