import os
import allure

from features.helpers.browser import Browser
from allure_commons.types import AttachmentType


def before_all(context):
    print('Starting Testing')


def before_scenario(context, scenario):
    context.browser = Browser().create_browser(
        browser=context.config.userdata['env_browser'])


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        screenshot_file = os.getcwd() + '/report-allure/' + \
            scenario.name.replace(' ', '_').lower() + '.png'
        context.browser.save_screenshot(screenshot_file)
        allure.attach(context.browser.get_screenshot_as_png(),
                      name='Screenshot', attachment_type=AttachmentType.PNG)

    if context.browser is not None:
        context.browser.close()


def after_all(context):
    print('Finish Testing')
