.PHONY: setup build-local deploy


setup:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

build-local:
	venv/bin/python3 build.py

deploy:
	venv/bin/python3 build.py --config config.json
	./deploy.sh
