import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from project import config


def test_open_article():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")
    with step('Open article'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/view_featured_article_card_article_title")).click()
