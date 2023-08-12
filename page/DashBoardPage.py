from page.BaseApp import BasePage
from page.TransferPage import TransferPage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    __cards_collection_locator = (By.CSS_SELECTOR, ".list__item div")

    def get_card_list(self):
        return self.find_elements(self.__cards_collection_locator)

    def get_balances(self):
        return [int(card.text.split(" ")[5]) for card in self.get_card_list()]

    def choose_card(self, card):
        card_button_locator = (By.XPATH, "//*[@data-test-id = '" + card.test_id + "']//button")
        self.find_element(card_button_locator).click()
        return TransferPage(self.driver)