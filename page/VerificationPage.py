from page.BaseApp import BasePage
from selenium.webdriver.common.by import By


class VerificationPage(BasePage):
    __verification_code_field_locator = (By.CSS_SELECTOR, "[data-test-id=code] input")
    __verify_button_locator = (By.CSS_SELECTOR, "[data-test-id=action-verify]")

    def valid_verify(self, verification_code):
        self.find_element(self.__verification_code_field_locator).send_keys(verification_code.code)
        self.find_element(self.__verify_button_locator).click()