import paho.mqtt.client as mqtt

# Define callback functions for handling connection and message events
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # Subscribe to the desired topic
        client.subscribe("BotPatrol")
    else:
        print("Failed to connect, return code: ", rc)

def on_message(client, userdata, msg):
    # Print received message topic and payload
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode())
    # Process the received data here according to your requirements
    client.disconnect()
    client.loop_stop()


# Create an MQTT client instance
client = mqtt.Client()

# Set event callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
broker_address = "192.168.0.101"
broker_port = 1883

client.connect(broker_address, broker_port)

# Start infinite loop to receive messages
client.loop_forever()