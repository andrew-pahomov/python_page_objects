import allure
from selenium.webdriver.common.by import By

from page.BaseApp import BasePage
from page.DashBoardPage import DashboardPage


class VerificationPage(BasePage):
    __verification_code_field_locator = (By.CSS_SELECTOR, "[data-test-id=code] input")
    __verify_button_locator = (By.CSS_SELECTOR, "[data-test-id=action-verify]")

    @allure.step('Верификация')
    def valid_verify(self, verification_code):
        self.find_element(self.__verification_code_field_locator).send_keys(verification_code.code)
        self.make_creenshot()
        self.find_element(self.__verify_button_locator).click()
        return DashboardPage(self.driver)
