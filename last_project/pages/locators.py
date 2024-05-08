from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    login_form = (By.ID, 'login_form')

    register_form = (By.ID, "register_form")


class ProductPageLocators:
    button_add = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')

    product_name = (By.CSS_SELECTOR, "div.product_main h1")

    product_basket = (By.CSS_SELECTOR, "div.alertinner ")

    price_product = (By.CSS_SELECTOR, "p.price_color")

    price_basket = (By.CSS_SELECTOR, ".alertinner p strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")