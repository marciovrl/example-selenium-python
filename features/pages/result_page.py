from selenium.webdriver.common.by import By
from features.helpers.base_page import BasePage


class ResultPageLocator(object):
    pass


class ResultPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def is_item_searched_displayed(self, item):
        LABEL_ITEM = (
            By.XPATH, "//h1[@class='breadcrumb__title'][text()='" + item + "']")
        return self.is_displayed(*LABEL_ITEM)

    def is_page_the_selected(self, option):
        LABEL_PAGE = (
            By.XPATH, "//h1[@class='breadcrumb__title'][text()='" + option + "']")
        return self.is_displayed(*LABEL_PAGE)
