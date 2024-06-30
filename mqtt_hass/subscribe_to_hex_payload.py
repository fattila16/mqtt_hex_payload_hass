import argparse
from dataclasses import dataclass
from typing import Any

from paho.mqtt.client import Client, MQTTMessage

from mqtt_hass.mqtt.client import MqttClient
from mqtt_hass.mqtt.config import MqttClientConfig
from mqtt_hass.mqtt.subscriber import MqttSubscriber


@dataclass
class Arguments:
    topic: str


def _parse_args() -> Arguments:
    parser = argparse.ArgumentParser(
        prog="publish_hex_payload",
        description="Publishes a given string as bytes to a given MQTT topic.",
    )
    parser.add_argument(
        "-t", "--topic", type=str, required=True, help="The MQTT topic to publish to."
    )
    return Arguments(**vars(parser.parse_args()))

def on_message(_client: Client, _userdata: Any, message: MQTTMessage):
    print(f"{message.topic}: {message.payload}")


def main():
    args = _parse_args()
    mqtt_client = MqttClient(MqttClientConfig.from_env())
    mqtt_subscriber = MqttSubscriber(mqtt_client)
    mqtt_subscriber.subscribe(topic=args.topic, callback=on_message)


if __name__ == "__main__":
    main()
