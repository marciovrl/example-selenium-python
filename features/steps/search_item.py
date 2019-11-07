from features.pages.home_page import HomePage
from features.pages.result_page import ResultPage


@step(u'that it is on the homepage of Mercado Livre')
def step_impl(context):
    if not hasattr(context, 'home_page'):
        context.home_page = HomePage(context.browser)

    context.home_page.navigate_to(context.config.userdata['url'])


@step(u'I search for "{item}"')
def step_impl(context, item):
    context.home_page.search_item(item)


@step(u'I view items according to my search')
def step_impl(context):
    if not hasattr(context, 'result_page'):
        context.result_page = ResultPage(context.browser)

    assert context.result_page.is_item_searched_displayed('golf') is True


@step(u'Select "{option}" option')
def step_impl(context, option):
    context.home_page.go_to_menu_item(option)


@step(u'I see Deals of the week')
def step_impl(context):
    if not hasattr(context, 'result_page'):
        context.result_page = ResultPage(context.browser)

    assert context.result_page.is_page_the_selected(
        'Ofertas da semana') is True
