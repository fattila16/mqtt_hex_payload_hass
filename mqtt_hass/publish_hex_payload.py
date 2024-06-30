import argparse
from dataclasses import dataclass

from mqtt_hass.mqtt.client import MqttClient
from mqtt_hass.mqtt.config import MqttClientConfig
from mqtt_hass.mqtt.publisher import MqttPublisher
from mqtt_hass.hex_codec import convert_hex_string_to_bytes


@dataclass
class Arguments:
    topic: str
    data: str

def _parse_args() -> Arguments:
    parser = argparse.ArgumentParser(
        prog='publish_hex_payload',
        description='Publishes a given string as bytes to a given MQTT topic.'
    )
    parser.add_argument('-t', '--topic', type=str, required=True, help='The MQTT topic to publish to.')
    parser.add_argument('-d', '--data', type=str, required=True, help='The payload to send.')
    return Arguments(**vars(parser.parse_args()))

def main():
    args = _parse_args()
    payload_as_bytes = convert_hex_string_to_bytes(args.data)
    mqtt_client = MqttClient(MqttClientConfig.from_env())
    publisher = MqttPublisher(mqtt_client)
    publisher.publish(args.topic, payload_as_bytes)

if __name__ == '__main__':
    main()