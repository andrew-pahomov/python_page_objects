import allure
from pytest_check import check

from data.DataHelper import Helper
from data.DataHelper import get_valid_amount
from page.LoginPage import LoginPage


@allure.suite('Перевод средств между своими картами')
@allure.story('Перевод случайной валидной сумму со второй карты на первую')
def test_transfer_from2to1(driver):
    login_page = LoginPage(driver, 'http://localhost:9999/')
    user = Helper.get_user()
    verification_page = login_page.valid_login(user.login, user.password)
    code = Helper.get_verification_code()
    dashboard_page = verification_page.valid_verify(code)
    cards_balances_before = dashboard_page.get_balances()
    transfer_page = dashboard_page.choose_card(Helper.get_cards()[0])
    amount = get_valid_amount(cards_balances_before[1])
    transfer_page.transfer(amount, Helper.get_cards()[1].number)
    cards_balances_after = dashboard_page.get_balances()
    with check:
        assert cards_balances_before[0] + amount == cards_balances_after[0]
    with check:
        assert cards_balances_before[1] - amount == cards_balances_after[1]
