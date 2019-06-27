from selenium import webdriver

class BasePage(object):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)

    def go_url(context, url):
        context.driver.get(url)

    def input_text(context, text, *locator):
        context.driver.find_element(*locator).send_keys(text)

    def click(context, *locator):
        context.driver.find_element(*locator).click()

    def is_displayed(context, *locator):
        return context.driver.find_element(*locator).is_displayed()

    def close(context):
        context.driver.close()