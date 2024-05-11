from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Логин должен находиться по текущему URL"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.login_form), "Нет формы для логина"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.register_form), "Нет формы для регистрации"

    def register_new_user(self, email, password):
        email_input=self.browser.find_element(*LoginPageLocators.EMAIL)
        password1_input=self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password2_input=self.browser.find_element(*LoginPageLocators.PASSWORD2)
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        button_submit=self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        button_submit.click()