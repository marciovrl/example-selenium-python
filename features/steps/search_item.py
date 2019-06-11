from selenium import webdriver

@given(u'that it is on the homepage of Mercado Livre')
def step_impl(self):
    self.driver = webdriver.Chrome()
    self.driver.get('https://mercadolivre.com.br/')

@when(u'I search for "{item}"')
def step_impl(self, item):
    self.driver.find_element_by_name('as_word').send_keys(item)
    self.driver.find_element_by_xpath("//button[@class='nav-search-btn']").click()

@then(u'I view items according to my search')
def step_impl(self):
    assert self.driver.find_element_by_xpath("//h1[@class='breadcrumb__title'][text()='golf']").is_displayed() is True