from features.pages.home import HomePage
from features.pages.list import ListPage


@step('that it is on the homepage of Mercado Livre')
def step_impl(context):
    if not hasattr(context, 'home_page'):
        context.home_page = HomePage(context.browser)

    context.home_page.navigate_to(context.config.userdata['url'])


@step('I search for "{item}"')
def step_impl(context, item):
    context.home_page.search_item(item)


@step('I view items according to my search')
def step_impl(context):
    if not hasattr(context, 'list_page'):
        context.list_page = ListPage(context.browser)

    assert 'golf' in context.list_page.is_item_searched_displayed()


@step('I select "{option}" option')
def step_impl(context, option):
    context.home_page.go_to_menu_item(option)


@step('I see deals')
def step_impl(context):
    if not hasattr(context, 'list_page'):
        context.list_page = ListPage(context.browser)

    assert 'Ofertas' in context.list_page.is_page_the_selected()
