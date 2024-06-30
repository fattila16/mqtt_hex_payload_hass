from typing import Any

from paho.mqtt.client import CallbackOnMessage, Client, MQTTMessage

from mqtt_hass.mqtt.client import MqttClient


class MqttSubscriber:
    def __init__(self, client: MqttClient):
        self._client = client

    def subscribe(self, topic: str, callback: CallbackOnMessage) -> None:
        def callback_with_disconnect(client: Client, userdata: Any, message: MQTTMessage):
            callback(client, userdata, message)
            print('cica')
            client.loop_stop()
            client.disconnect()

        with self._client.get_connection() as client:
            client.subscribe(topic)
            client.on_message = callback_with_disconnect
            client.loop_start()
