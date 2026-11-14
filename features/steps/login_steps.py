from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@given('User launches the application')
def launch_application(context):

    context.playwright = sync_playwright().start()

    context.browser = context.playwright.chromium.launch(
        headless=False
    )

    context.page = context.browser.new_page()

    context.page.goto("https://www.saucedemo.com")


@when('User enters valid credentials')
def enter_credentials(context):

    login_page = LoginPage(context.page)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )


@then('User should login successfully')
def verify_login(context):

    assert "inventory" in context.page.url

    context.browser.close()

    context.playwright.stop()