import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class MqttClientConfig:
    broker: str
    port: int
    username: Optional[str]
    password: Optional[str]

    @staticmethod
    def from_env():
        return MqttClientConfig(
            broker=os.getenv("MQTT_BROKER"),
            port=int(os.getenv("MQTT_PORT")),
            username=os.getenv("MQTT_USERNAME"),
            password=os.getenv("MQTT_PASSWORD"),
        )
