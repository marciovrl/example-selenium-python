from selenium import webdriver
from features.helpers.base_page import BasePage

def before_all(context):
    context.browser = BasePage()

def after_all(context):
    context.browser.close()