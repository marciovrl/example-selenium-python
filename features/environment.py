from features.helpers.browser_factory import get_browser


def before_all(context):
    print('Starting Testing')


def before_scenario(context, scenario):
    context.browser = get_browser(
        context.config.userdata['browser']
    )


def after_scenario(context, scenario):
    if context.browser is not None:
        context.browser.quit()


def after_all(context):
    print('Finish Testing')
