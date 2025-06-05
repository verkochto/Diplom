# 🧪 Автоматизация тестирования сайта «Читай-город»

## 📌 Описание проекта

Этот проект содержит автотесты для сайта [Читай-город](https://www.chitai-gorod.ru) — онлайн-магазина книг, учебников, канцелярии и сопутствующих товаров.  
Автотесты реализованы на Python с использованием `pytest`, `selenium`, `requests` и `allure`.  
Цель проекта — автоматизировать ключевые сценарии пользовательского взаимодействия (UI) и API, на основе тест-кейсов из финального проекта по ручному тестированию.

## 🗂 Структура проекта


├── config/             
│   └── config.py  
├── data/               
│   └── test_data.py  
├── pages/               
│   └── login_page.py  
├── tests/              
│   ├── test_ui.py  
│   └── test_api.py  
├── conftest.py         
├── requirements.txt    
├── pytest.ini         
├── .gitignore         
└── README.md           

## 🚀 Как запустить автотесты

1. Клонировать репозиторий  

2. Создать виртуальное окружение  
python -m venv venv  
source venv/bin/activate  (Linux/macOS)  
venv\Scripts\activate     (Windows)  

3. Установить зависимости  
pip install -r requirements.txt  

4. Запуск тестов  
pytest -m ui        # Только UI тесты  
pytest -m api       # Только API тесты  
pytest              # Все тесты  

## 📊 Генерация Allure-отчета


pytest --alluredir=allure-results  
  

## 🧪 Покрытие автотестами

UI-тесты (Selenium + PageObject):  
вторизация с валидными данными  
Авторизация с невалидными данными  
Поиск книги (можно добавить)  
Добавление в корзину (можно добавить)  

API-тесты (requests):  
Успешная авторизация  
Ошибка при неверных данных  
Поиск книг по API (если доступно — можно добавить)  
Получение карточки товара (можно добавить)  

## ⚙️ Используемые технологии

- Python 3.10+  
- Pytest  
- Selenium  
- Requests  
- Allure Pytest  
- WebDriverManager  



## 💬 Комментарии

- Все чувствительные данные вынесены в `config.py`  
- Проект не содержит лишних файлов: `chromedriver.exe`, `.vscode`, `__pycache__` и т.д.  
- Код оформлен по стандарту PEP8  
- Используется маркировка тестов `@pytest.mark.ui` и `@pytest.mark.api` для выборочного запуска


