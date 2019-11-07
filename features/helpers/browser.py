from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Browser:
    def create_browser(self, **kwargs):
        """Pass as argument the type of browser that the test will run.
            If you are informed of one that is not listed, the test will run in Chrome.
        """

        browser = kwargs.get('browser')

        if(browser == 'firefox_headless'):
            options = Options()
            options.add_argument('-headless')
            options.add_argument('--start-maximized')
            return webdriver.Firefox(options=options)

        elif(browser == 'chrome_headless'):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1400,600')
            return webdriver.Chrome(chrome_options=chrome_options)

        elif(browser == 'chrome_mobile'):
            mobile_emulation = {'deviceName': 'Nexus 5'}
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_experimental_option(
                "mobileEmulation", mobile_emulation)
            return webdriver.Chrome(chrome_options=chrome_options)

        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            return webdriver.Chrome(chrome_options=chrome_options)
