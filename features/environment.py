import os

from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_browser_chrome(context):
    chrome_path = os.environ.get("CHROME_EXE_PATH")
    if chrome_path is None:
        print("You need to set CHROME_EXE_PATH env variable. See the README for details.")
    else:
        print(chrome_path)

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    driver.maximize_window()
    driver.implicitly_wait(4)
    context.browser = driver
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
