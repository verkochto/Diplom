from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.chitai-gorod.ru/login" 

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.ID, "login-email").send_keys(username)
        self.driver.find_element(By.ID, "login-password").send_keys(password)
        self.driver.find_element(By.ID, "login-password").send_keys(Keys.RETURN)

    def user_icon_visible(self):
        return self.driver.find_element(By.CLASS_NAME, "user-name").is_displayed()
