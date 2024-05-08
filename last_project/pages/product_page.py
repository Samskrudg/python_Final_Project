from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add(self):
        button = self.browser.find_element(*ProductPageLocators.button_add)
        button.click()

    def should_be_add_button_link(self):
        assert self.is_element_present(*ProductPageLocators.button_add), "Нет кнопки добавить в корзину"

    def compare_price_product(self):
        product_price_check = self.browser.find_element(*ProductPageLocators.price_product).text
        basket_price_check = self.browser.find_element(*ProductPageLocators.price_basket).text
        assert product_price_check == basket_price_check, "Цена на сайте и в корзине не совпадают"

    def compare_name_product(self):
        product_name_check = self.browser.find_element(*ProductPageLocators.product_name).text
        basket_name_check = self.browser.find_element(*ProductPageLocators.product_basket).text
        assert f"{product_name_check} has been added to your basket." == basket_name_check, ("Название товара на сайте "
                                                                                             "и в корзине не совпадают")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе представлено, но не должно быть"

    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Элемент не исчез"