import pytest
import allure
from pages.login_page import LoginPage
from config import config


@pytest.mark.ui
@allure.title("UI: Успешная авторизация")
def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login(config.USERNAME, config.PASSWORD)
    assert page.user_icon_visible()
