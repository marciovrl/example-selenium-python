from selenium.webdriver.common.by import By
from features.helpers.base_page import BasePage


class HomePageLocator(object):
    INPUT_ITEM = (
        By.NAME,
        'as_word'
    )

    BUTTON_INPUT = (
        By.CSS_SELECTOR,
        'button .nav-icon-search'
    )

    LIST_MENU = (
        By.CLASS_NAME,
        'nav-menu-item-link'
    )


class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def navigate_to(self, url):
        self.go_url(url)

    def search_item(self, item):
        self.input_text(item, *HomePageLocator.INPUT_ITEM)
        self.click(*HomePageLocator.BUTTON_INPUT)

    def go_to_menu_item(self, menu_option):
        menu_list = self.get_elements(*HomePageLocator.LIST_MENU)

        for option in menu_list:
            if option.text == menu_option:
                option.click()
                break
