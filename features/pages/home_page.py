from selenium.webdriver.common.by import By
from features.helpers.base_page import BasePage

class HomePageLocator(object):
    INPUT_ITEM = (By.NAME, 'as_word')
    BUTTON_INPUT = (By.XPATH, "//button[@class='nav-search-btn']")
    LABEL_ITEM_SEARCH = (By.XPATH, "//h1[@class='breadcrumb__title'][text()='golf']")

class HomePage(BasePage):
    def navigate_to(self):
        self.go_url('https://mercadolivre.com.br/')
    
    def search_item(self, item):
        self.input_text(item, *HomePageLocator.INPUT_ITEM)
        self.click(*HomePageLocator.BUTTON_INPUT)

    def is_item_searched_displayed(self):
        return self.is_displayed(*HomePageLocator.LABEL_ITEM_SEARCH)