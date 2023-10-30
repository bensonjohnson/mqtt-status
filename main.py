import paho.mqtt.client as mqtt
import time
import os

# Callback when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Read environment variables for MQTT configuration
MQTT_BROKER = os.environ.get("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 1883))
MQTT_USERNAME = os.environ.get("MQTT_USERNAME", None)
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD", None)
MQTT_SLEEP = int(os.environ.get("MQTT_SLEEP", 120))

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = on_connect

# Set username and password if provided
if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 15)

# Loop to keep the connection alive
client.loop_start()

try:
    while True:
        # Publish the message to the topic
        client.publish("/control/status", "up")
        print("Message published: up")
        time.sleep(MQTT_SLEEP)
except KeyboardInterrupt:
    print("Disconnected")
    client.loop_stop()
    client.disconnect()
