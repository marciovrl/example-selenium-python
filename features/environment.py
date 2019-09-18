from features.helpers.browser import Browser


def before_all(context):
    print ("before all")


def before_scenario(context, scenario):
    context.browser = Browser().create_browser(
        browser=context.config.userdata["env_browser"])


def after_scenario(context, scenario):
    if context.browser is not None:
        context.browser.close()


def after_all(context):
    print ("after all")
