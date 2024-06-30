import argparse
from dataclasses import dataclass
from typing import Any

from paho.mqtt.client import Client, MQTTMessage

from mqtt_hass.mqtt.config import MqttClientConfig
from mqtt_hass.mqtt.client import MqttClient
from mqtt_hass.mqtt.publisher import MqttPublisher
from mqtt_hass.mqtt.subscriber import MqttSubscriber
from mqtt_hass.hex_codec import convert_hex_string_to_bytes

@dataclass
class Arguments:
    request_topic: str
    read_topic: str
    destination_topic: str
    data: str

def _parse_args() -> Arguments:
    parser = argparse.ArgumentParser(
        prog='distribute_sensor_data',
        description='Requests and waits for sensor data, then distributes it to the corresponding mqtt topic'
    )
    parser.add_argument('-req', '--request-topic', type=str, required=True, help='Topic to send request bytes to')
    parser.add_argument('-read', '--read-topic', type=str, required=True, help='Topic to read the requested bytes from')
    parser.add_argument('-dest', '--destination-topic', type=str, required=True, help='Destination topic to publish the parsed sensor data')
    parser.add_argument('-d', '--data', type=str, required=True, help='Request payload bytes as string')
    return Arguments(**vars(parser.parse_args()))

def on_message(_client: Client, _userdata: Any, message: MQTTMessage):
    print(f"{message.topic}: {message.payload}")

got_data = False

def main():
    args = _parse_args()
    request_data_bytes = convert_hex_string_to_bytes(args.data)
    mqtt_client = MqttClient(MqttClientConfig.from_env())
    publisher = MqttPublisher(mqtt_client)
    subscriber = MqttSubscriber(mqtt_client)
    subscriber.subscribe(args.read_topic, on_message)
    publisher.publish(args.request_topic, request_data_bytes)
    while got_data is False:
        print('Waiting for requested data')
    

if __name__ == "__main__":
    main()