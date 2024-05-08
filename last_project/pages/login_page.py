from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators


def should_be_login_url():
    assert True


class LoginPage(BasePage):
    def should_be_login_page(self):
        should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.login_form), "Нет формы для логина"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.register_form), "Нет формы для регистрации"


class ProductPage(BasePage):
    def should_be_add_basket_page(self):
        self.should_be_button_add()

    def should_be_button_add(self):
        assert self.is_element_present(*ProductPageLocators.button_add), "Нет кнопки добавить"
