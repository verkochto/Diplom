import pytest
import allure
from pages.main_page import MainPage


@allure.epic("UI Проверка поиска")
@allure.feature("Функциональность строкового поиска")
class TestSearchFunctionality:

    @allure.title("Поиск по ключевому слову: заголовок книги")
    @allure.description("Убедиться, что поиск по слову 'капитанская' возвращает релевантные результаты.")
    @pytest.mark.ui
    def test_search_by_title_keyword(self, driver):
        page = MainPage(driver)
        page.open()
        page.search_book("капитанская")
        results = page.get_search_results_text()
        assert "запросу «капитанская», найдено" in results

    @allure.title("Поиск по фамилии писателя")
    @allure.description("Проверка поиска по имени автора: пушкин.")
    @pytest.mark.ui
    def test_search_by_author_name(self, driver):
        page = MainPage(driver)
        page.open()
        page.search_book("пушкин")
        results = page.get_search_results_text()
        assert "запросу «пушкин», найдено" in results

    @allure.title("Поиск по английскому названию")
    @allure.description("Тестирование поиска по англоязычному слову 'house'.")
    @pytest.mark.ui
    def test_search_english_term(self, driver):
        page = MainPage(driver)
        page.open()
        page.search_book("house")
        results = page.get_search_results_text()
        assert "запросу «house», найдено" in results

    @allure.title("Поиск по спецсимволам")
    @allure.description("Проверка реакции на ввод несуществующего слова из символов.")
    @pytest.mark.ui
    def test_search_with_symbols(self, driver):
        page = MainPage(driver)
        page.open()
        page.search_book("@!?*")
        results = page.get_search_results_text()
        assert "не принёс результатов" in results

    @allure.title("Поиск по тексту на тайском языке")
    @allure.description("Убедиться, что ввод текста на тайском не даёт результатов.")
    @pytest.mark.ui
    def test_search_with_thai_language(self, driver):
        page = MainPage(driver)
        page.open()
        page.search_book("เกาะมหาสมบัต")
        results = page.get_search_results_text()
        assert "не принёс результатов" in results
