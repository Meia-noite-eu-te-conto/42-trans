VOLUMES :=		~/goinfre/storage/game-data \
				~/goinfre/storage/user-data

all: mkdir run-compose

run-compose:
	docker compose up --build

venv:
	cd src
	python3 -m venv core
	source core/bin/activate
	pip install django

clean:
	docker compose down
	docker volume prune -a -f
	sudo rm -rf $(STORAGE_GAME) $(STORAGE_USER)

mkdir:
	sudo mkdir -p $(VOLUMES)

fclean:
	docker compose down
	docker volume prune -a -f
	sudo rm -rf $(VOLUMES)

build: mkdir
	docker compose up --build

re: fclean build