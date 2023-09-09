from behave import *


# scenario 1
@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert a "{email}" email')
def step_impl(context, email):
    context.login_page.insert_email(email)


@when("I insert a password")
def step_impl(context):
    context.login_page.insert_a_password()


@when("I click on the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("Main error is displayed")
def step_impl(context):
    context.login_page.main_error_is_displayed()
