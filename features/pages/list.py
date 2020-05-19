from selenium.webdriver.common.by import By
from features.helpers.base_page import BasePage


class ListPageLocator(object):
    LABEL_RESULT = (
        By.CSS_SELECTOR,
        'div .breadcrumb > h1'
    )

    LABEL_RESULT_PAGE = (
        By.CSS_SELECTOR,
        'h1'
    )


class ListPage(BasePage):
    def is_item_searched_displayed(self):
        return self.get_text(*ListPageLocator.LABEL_RESULT)

    def is_page_the_selected(self):
        return self.get_text(*ListPageLocator.LABEL_RESULT_PAGE)
