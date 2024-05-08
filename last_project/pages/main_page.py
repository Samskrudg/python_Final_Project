from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Ссылки для входа нет"

    def go_to_login_form_page(self):
        link = self.browser.find_element(*MainPageLocators.login_form)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_register_form_page(self):
        link = self.browser.find_element(*MainPageLocators.register_form)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
