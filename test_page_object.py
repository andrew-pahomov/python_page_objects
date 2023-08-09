from page.LoginPage import LoginPage
from page.VerificationPage import VerificationPage
from data.DataHelper import Helper


def test_transfer_from1to2(driver):
    login_page = LoginPage(driver, 'http://localhost:9999/')
    user = Helper.get_user()
    login_page.valid_login(user.login, user.password)
    verification_page = VerificationPage(driver)
    code = Helper.get_verification_code()
    verification_page.valid_verify(code)
