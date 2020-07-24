all:
	@echo "req-install   - install requirements"
	@echo "req-update    - update requirements"
	@echo "lint    			 - lint files"

req-install:
	pip3 install pip-tools
	pip-sync

req-update:
	pip-compile -U
	pip-sync

lint:
	pycodestyle --show-source --max-line-length=120 --format='%(path)s | %(row)d | %(col)d | %(code)show' ciphers/*.py leet-code/*.py scripts/*.py maths/*.py feature-lang/*.py