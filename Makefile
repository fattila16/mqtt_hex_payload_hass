DOCKER_COMPOSE_FILE := ./config/docker/docker-compose.yaml
PROJECT_NAME := mqtt-hass

##------------------------------------------------------------------------
##                      Run Commands
##------------------------------------------------------------------------
run-subscriber:
	poetry run python -m mqtt_hass.subscribe_to_hex_payload -t topic
publish-message:
	poetry run python -m mqtt_hass.publish_hex_payload -t topic	-d "01 03 00 1E 00 03 65 C9"
##------------------------------------------------------------------------
##                      Docker Related Commands
##------------------------------------------------------------------------
dependencies-up:
	docker compose --file $(DOCKER_COMPOSE_FILE) --project-name $(PROJECT_NAME)  up -d

dependencies-down:
	docker compose --file $(DOCKER_COMPOSE_FILE) --project-name $(PROJECT_NAME) down