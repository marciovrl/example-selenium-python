from selenium.webdriver.common.by import By
from features.helpers.base_page import BasePage

class HomePageLocator(object):
    INPUT_ITEM = (By.NAME, 'as_word')
    BUTTON_INPUT = (By.XPATH, "//button[@class='nav-search-btn']")
    LABEL_ITEM_SEARCH = (By.XPATH, "//h1[@class='breadcrumb__title'][text()='golf']")

class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def navigate_to(self, url):
        self.go_url(url)
    
    def search_item(self, item):
        self.input_text(item, *HomePageLocator.INPUT_ITEM)
        self.click(*HomePageLocator.BUTTON_INPUT)

    def go_to_menu_item(self, option):
        MENU_ITEM = (By.XPATH, "//a[@class='nav-menu-item-link'][text()='" + option + "']")
        self.click(*MENU_ITEM)