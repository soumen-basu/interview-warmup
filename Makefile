.PHONY: help install build serve test docker-dev docker-preview docker-down clean sync-config

help:
	@echo "Available commands:"
	@echo "  make install        - Initialize submodule and install Quartz dependencies"
	@echo "  make build          - Build static HTML to quartz/public"
	@echo "  make serve          - Run local dev server with hot reload (http://localhost:8080)"
	@echo "  make test           - Run automated site integrity and link validation tests"
	@echo "  make docker-dev     - Run dev server inside Docker (http://localhost:8080)"
	@echo "  make docker-preview - Build & serve production Nginx preview (http://localhost:8081)"
	@echo "  make docker-down    - Stop running Docker services"
	@echo "  make clean          - Remove built artifacts and cache"

sync-config:
	cp -f quartz.config.yaml quartz/quartz.config.yaml

install: sync-config
	git submodule update --init --recursive
	cd quartz && npm install

build: sync-config
	npm --prefix quartz run quartz -- build -d ../wiki

serve: sync-config
	npm --prefix quartz run quartz -- build --serve -d ../wiki

test:
	python3 -m unittest discover tests -v

docker-dev: sync-config
	docker compose up --build wiki-dev

docker-preview: sync-config
	docker compose up --build wiki-preview

docker-down:
	docker compose down

clean:
	rm -rf quartz/public quartz/.quartz-cache
