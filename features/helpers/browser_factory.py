from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def create_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')

    return webdriver.Chrome(chrome_options=chrome_options)


def create_chrome_headless():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1400,600')

    return webdriver.Chrome(chrome_options=chrome_options)


def create_chrome_mobile():
    mobile_emulation = {
        'deviceName': 'Nexus 5'
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option(
        'mobileEmulation',
        mobile_emulation
    )

    return webdriver.Chrome(chrome_options=chrome_options)


def create_firefox():
    return webdriver.Firefox()


def create_firefox_headless():
    options = Options()
    options.add_argument('-headless')
    options.add_argument('--start-maximized')

    return webdriver.Firefox(options=options)


mapping = {
    'chrome': create_chrome,
    'chrome_headless': create_chrome_headless,
    'chrome_mobile': create_chrome_mobile,
    'firefox': create_firefox,
    'firefox_headless': create_firefox_headless,
    'default': create_chrome
}


def get_browser(browser):
    """Pass as argument the type of browser that the test will run.
        If you are informed of one that is not listed, the test will run in Chrome.
    """
    return mapping.get(browser, 'default')()
