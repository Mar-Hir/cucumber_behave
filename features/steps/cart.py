from behave import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains


@given('the user goes to page {url}')
def step_impl(context, url):
    context.browser.get(url)


@given('the cart is empty')
def step_impl(context):
    cart_empty = context.browser.find_element_by_xpath("//span[contains(text(),'(empty)')]")
    assert cart_empty.is_displayed()
    time.sleep(1)


@given('the user clicks T-Shirts button')
def step_impl(context):
    button = context.browser.find_element_by_xpath("//li[3]//a[@title='T-shirts']")
    button.click()
    wait = WebDriverWait(context.browser, 10, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
    wait.until(EC.title_is("T-shirts - My Store"))


@when('user hovers over the first visible image')
def step_impl(context):
    hover_button = context.browser.find_element_by_xpath("//img[@itemprop='image']")
    actions = ActionChains(context.browser)
    actions.move_to_element(hover_button).perform()
    time.sleep(2)


@when('the Add to cart button is visible')
def step_impl(context):
    cart_button = context.browser.find_element_by_xpath("//span[contains(text(),'Add to cart')]")
    assert cart_button.is_displayed()


@when('user clicks the button Add to cart')
def step_impl(context):
    cart_button = context.browser.find_element_by_xpath("//span[contains(text(),'Add to cart')]")
    actions = ActionChains(context.browser)
    actions.move_to_element(cart_button).click().perform()
    time.sleep(2)


@then('an item is added to the cart')
def step_impl(context):
    product_added = context.browser.find_element_by_xpath("//h2[contains(.,'Product successfully "
                                                          "added to your shopping cart')]")
    item_count = context.browser.find_element_by_xpath("//span[contains(.,'There is 1 item in your cart')]")
    assert product_added.is_displayed()
    assert item_count.is_displayed()



