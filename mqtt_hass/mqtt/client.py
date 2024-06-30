from contextlib import contextmanager
from typing import Iterator

from paho.mqtt.client import Client, MQTTv5
from paho.mqtt.enums import CallbackAPIVersion

from mqtt_hass.mqtt.config import MqttClientConfig


class MqttClient:
    def __init__(self, config: MqttClientConfig):
        self._config = config
        self._client = Client(callback_api_version=CallbackAPIVersion.VERSION2 ,protocol=MQTTv5)
        if (config.username is not None) and (config.password is not None):
            self._client.username_pw_set(config.username, config.password)

    @contextmanager
    def get_connection(self) -> Iterator[Client]:
        try:
            self._client.connect(self._config.broker, self._config.port)
            yield self._client
        finally:
            self._client.disconnect()
