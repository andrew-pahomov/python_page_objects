import allure
from selenium.webdriver.common.by import By

from page.BaseApp import BasePage
from page.TransferPage import TransferPage


class DashboardPage(BasePage):
    __cards_collection_locator = (By.CSS_SELECTOR, ".list__item div")

    def get_card_list(self):
        return self.find_elements(self.__cards_collection_locator)

    @allure.step('Получение балансов карт')
    def get_balances(self):
        self.make_creenshot()
        return [int(card.text.split(" ")[5]) for card in self.get_card_list()]

    @allure.step('Выбор карты для пополнения')
    def choose_card(self, card):
        card_button_locator = (By.XPATH, "//*[@data-test-id = '" + card.test_id + "']//button")
        self.make_creenshot()
        self.find_element(card_button_locator).click()
        return TransferPage(self.driver)
