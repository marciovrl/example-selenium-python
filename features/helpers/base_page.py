from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def go_url(self, url):
        self.driver.get(url)

    def get_element(self, *locator):
        return WebDriverWait(self.driver, 50).until(ec.visibility_of_element_located((locator[0], locator[1])))

    def input_text(self, text, *locator):
        self.get_element(*locator).send_keys(text)

    def click(self, *locator):
        self.get_element(*locator).click()

    def is_displayed(self, *locator):
        return self.get_element(*locator).is_displayed()

    def open_tab(self):
        self.driver.execute_script('''window.open("about:blank", "_blank");''')
        self.driver.switch_to_window(self.driver.window_handles[1])

    def close_tab(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def sleep(self, time_sleep):
        time.sleep(time_sleep)

    def close(self):
        self.driver.quit()
