import allure
from selenium.webdriver.common.by import By

from page.BaseApp import BasePage


class TransferPage(BasePage):
    __amount_field_locator = (By.CSS_SELECTOR, "[data-test-id='amount'] input")
    __card_number_field_locator = (By.CSS_SELECTOR, "[data-test-id='from'] input")
    __transfer_button_locator = (By.CSS_SELECTOR, "[data-test-id='action-transfer']")

    @allure.step('Перевод')
    def transfer(self, amount, card_number):
        self.find_element(self.__amount_field_locator).send_keys(amount)
        self.find_element(self.__card_number_field_locator).send_keys(card_number)
        self.make_creenshot()
        self.find_element(self.__transfer_button_locator).click()
