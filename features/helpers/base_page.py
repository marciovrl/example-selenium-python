from selenium import webdriver


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def go_url(self, url):
        self.driver.get(url)

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        self.get_element(*locator).send_keys(text)

    def click(self, *locator):
        self.get_element(*locator).click()

    def is_displayed(self, *locator):
        return self.get_element(*locator).is_displayed()

    def close(self):
        self.driver.close()
