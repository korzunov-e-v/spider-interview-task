# General
define set-default-container
	ifndef c
	c = django
	else ifeq (${c},all)
	override c=
	endif
endef

# Settings configurations
SET_SETTINGS_FOR_PROD_APPLICATION='export DJANGO_SETTINGS_MODULE=market_app.settings'

# Django commands
START_PYTEST='pytest -x api'

# General
TAIL=100



set-container:
	$(eval $(call set-default-container))

set-prod-settings: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/sh -c $(SET_SETTINGS_FOR_PROD_APPLICATION)



build:
	docker compose -f docker-compose.dev.yml build
up:
	docker compose -f docker-compose.dev.yml up -d
down:
	docker compose -f docker-compose.dev.yml down
logs: set-container
	docker compose -f docker-compose.dev.yml logs --tail=$(TAIL) -f $(c)
restart: set-container
	docker compose -f docker-compose.dev.yml restart $(c)
exec: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/sh
startup: build up


compile-reqs: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) sh -c 'pip install pip-tools && pip-compile pyproject.toml'
upgrade-reqs: set-container
	docker compose -f docker-compose.dev.yml run -rm $(c) sh -c 'pip install pip-tools && pip-compile upgrade'
migrate: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/sh -c 'python manage.py migrate'
migrations: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/sh -c 'python manage.py makemigrations'
shell: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/sh -c 'python manage.py shell'
pre-commit: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/sh -c 'pre-commit run --all-files'
execute-pytest-command: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/sh -c $(START_PYTEST)
pytest: set-container set-testing-settings execute-pytest-command set-prod-settings
