import pytest
import requests
import allure
from config import config
from data import test_data

@pytest.mark.api
@allure.title("API: Успешная авторизация")
def test_api_login_success():
    response = requests.post(f"{config.API_URL}/login", json=test_data.valid_user)
    assert response.status_code == 200
    assert "token" in response.json()

@pytest.mark.api
@allure.title("API: Ошибка при авторизации")
def test_api_login_fail():
    response = requests.post(f"{config.API_URL}/login", json=test_data.invalid_user)
    assert response.status_code == 401
