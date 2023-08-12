from page.BaseApp import BasePage
from selenium.webdriver.common.by import By
from page.VerificationPage import VerificationPage


class LoginPage(BasePage):
    __header_locator = (By.CSS_SELECTOR, "h2")
    __login_field_locator = (By.CSS_SELECTOR, "[data-test-id='login'] input")
    __password_field_locator = (By.XPATH, "//*[@data-test-id='password']//input")
    __button_locator = (By.CSS_SELECTOR, "[data-test-id='action-login']")

    def __init__(self, driver, url):
        super().__init__(driver)
        super().go_to_site(url)

    def valid_login(self, user_login, user_password):
        self.find_element(self.__login_field_locator).send_keys(user_login)
        self.find_element(self.__password_field_locator).send_keys(user_password)
        self.find_element(self.__button_locator).click()
        return VerificationPage(self.driver)