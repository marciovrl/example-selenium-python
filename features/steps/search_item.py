from selenium import webdriver

from features.pages.home_page import HomePage

@step(u'that it is on the homepage of Mercado Livre')
def step_impl(context):
    context.home_page = HomePage()
    context.home_page.navigate_to()

@step(u'I search for "{item}"')
def step_impl(context, item):
    context.home_page.search_item(item)

@step(u'I view items according to my search')
def step_impl(context):
    assert context.home_page.is_item_searched_displayed() is True