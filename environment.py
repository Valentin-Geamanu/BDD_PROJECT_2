from base_page import BasePage
from browser import Browser
from pages.login_page import LoginPage


def before_all(context):
    """
    Vom defini toate instructiunile care trebuie executate
    inaintea rulari tuturor pasilor.
    """
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()


def after_all(context):
    """
    Vom defini toate instructiunile care trebuie executate
    dupa rularea tuturor pasilor
    """
    context.browser.close()
