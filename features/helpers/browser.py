from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Browser:
    def create_browser(self, **kwargs):
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
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            return webdriver.Chrome(chrome_options=chrome_options)