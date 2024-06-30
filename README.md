# MQTT Home Assistant Hex Payload Publisher

This project contains scripts to publish HEX strings as binary payload to a given MQTT topic.

It has functionality to publish payloads and to subscribe to a given topic.

## Requirements
* `python >= 3.11.4`
* `make`

## How to test

In order to test the functionality one needs a running mqtt broker to test againts.
The project ships with a docker-compose file that sets up `mosquitto` without auth.

In order to test, first spin up the dependencies with:
`make dependencies-up`

Then start the subscriber with:
`make run-subscriber`

Then publish a message with
`make publish-message`

The subscriber will close connection after reading one message. This is subject to change later.