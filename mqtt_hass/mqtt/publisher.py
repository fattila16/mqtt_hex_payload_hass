from mqtt_hass.mqtt.client import MqttClient
from typing import Union


class MqttPublisher:
    def __init__(self, client: MqttClient):
        self._client = client

    def publish(self,topic: str, message: Union[str, bytes]) -> None:
        with self._client.get_connection() as connection:
            connection.publish(topic, message)
            print(f'Published to topic {topic}: {message}')