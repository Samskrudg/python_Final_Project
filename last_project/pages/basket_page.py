from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "В списке не должно быть элементов"

    def text_basket_is_empty_should_be_present(self):
        expected_alert = 'basket is empty'
        alert = self.browser.find_element(*BasketPageLocators.ALERT).text
        assert expected_alert in alert, "Текст «Корзина пуста» должен присутствовать."