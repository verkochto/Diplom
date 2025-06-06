import pytest
import requests
import allure
from data import test_data

base_url = "https://web-gate.chitai-gorod.ru"
# на сайте читай-город необходимо взять токен (access-token), в разделе cookies.
token_key = " " # сюда надо встfвить токен с сайта
headers = {
    "accept": "application/json",
    "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": f"Bearer {token_key}",
    "content-type": "application/json",
    "origin": "https://www.chitai-gorod.ru",
    "priority": "u=1, i",
    "referer": "https://www.chitai-gorod.ru/",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}


@pytest.mark.api
@allure.title("API: Успешная авторизация")
def test_api_login_success():
    response = requests.post(f"{base_url}/login", json=test_data.valid_user, headers=headers)
    assert response.status_code == 200
    assert "token" in response.json()


@pytest.mark.api
@allure.title("API: Ошибка при авторизации")
def test_api_login_fail():
    response = requests.post(f"{base_url}/login", json=test_data.invalid_user, headers=headers)
    assert response.status_code == 401


@allure.title("Оформление товаров в корзине")
def test_pay_product():
    resp = requests.get(base_url + '/api/v1/orders/checkout?userType=individual&orderType=order', headers=headers)
    assert resp.status_code == 200


@allure.title("Удаление из корзины отсутствующего товара")
def test_del_cart():
    resp = requests.delete(base_url + '/api/v1/cart/product/186354025', headers=headers)
    assert resp.status_code == 404
