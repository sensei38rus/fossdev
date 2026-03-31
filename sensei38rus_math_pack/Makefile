# Переменные
PACKAGE_NAME = sensei38rus_math_pack
PYTHON = python3
PIP = pip3

# Цели по умолчанию
.PHONY: help clean build upload test test-pypi install dev-install

help:
	@echo "Доступные команды:"
	@echo "  make clean        - очистка временных файлов"
	@echo "  make build        - сборка пакета"
	@echo "  make upload       - загрузка в TestPyPI"
	@echo "  make test-pypi    - установка из TestPyPI для проверки"
	@echo "  make install      - установка пакета в систему"
	@echo "  make dev-install  - установка в режиме разработки"
	@echo "  make test         - запуск тестов"

clean:
	@echo "Очистка временных файлов..."
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "Очистка завершена"

build: clean
	@echo "Сборка пакета..."
	$(PYTHON) setup.py sdist bdist_wheel
	@echo "Сборка завершена. Файлы в dist/:"
	@ls -la dist/

upload: build
	@echo "Загрузка в TestPyPI..."
	@echo "Введите __token__ как имя пользователя и ваш API токен как пароль"
	twine upload --repository testpypi dist/*
	@echo "Загрузка завершена!"

test-pypi:
	@echo "Установка из TestPyPI..."
	$(PIP) install --index-url https://test.pypi.org/simple/ $(PACKAGE_NAME)
	@echo "Установка завершена! Проверьте:"
	$(PYTHON) -c "import cool_math_utils; print('Версия:', cool_math_utils.__version__); print('add(2,3):', cool_math_utils.add(2,3))"

install:
	@echo "Установка пакета..."
	$(PIP) install .
	@echo "Установка завершена!"

dev-install:
	@echo "Установка в режиме разработки..."
	$(PIP) install -e .
	@echo "Установка завершена!"

test:
	@echo "Запуск тестов..."
	$(PYTHON) -m unittest discover tests
	@echo "Тесты пройдены!"