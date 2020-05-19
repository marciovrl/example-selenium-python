from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class BasePage(object):
    __TIMEOUT = 50

    def __init__(self, driver):
        super(BasePage, self).__init__()
        self._driver_wait = WebDriverWait(driver, BasePage.__TIMEOUT)
        self._driver = driver

    def go_url(self, url):
        self._driver.get(url)

    def get_element(self, *locator):
        return self._driver_wait.until(EC.visibility_of_element_located((locator[0], locator[1])))

    def get_elements(self, *locator):
        return self._driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.get_element(*locator).send_keys(text)

    def click(self, *locator):
        self.get_element(*locator).click()

    def is_displayed(self, *locator):
        return self.get_element(*locator).is_displayed()

    def open_tab(self):
        self._driver.execute_script(
            '''window.open("about:blank", "_blank");'''
        )
        self._driver.switch_to_window(self._driver.window_handles[1])

    def close_tab(self):
        self._driver.close()
        self._driver.switch_to_window(self._driver.window_handles[0])

    def sleep(self, time_sleep):
        time.sleep(time_sleep)

    def get_text(self, *locator):
        return self.get_element(*locator).text

    def click_element_in_elements(self, *locator, txt_element):
        elements = self.get_elements(*locator)
        for element in elements:
            if element.text == txt_element:
                element.click()
                break

    def close(self):
        self._driver.quit()
