import allure
import allure_commons
import pytest
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
from project import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    browser_platform = config.browser_platform
    if browser_platform == "android":
        options = UiAutomator2Options().load_capabilities({
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": config.app,
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": config.user_name,
                "accessKey": config.access_key
            }
        })
        browser.config.driver = webdriver.Remote(config.remote_url, options=options)

    else:
        options = XCUITestOptions().load_capabilities({
            "platformName": "ios",
            "platformVersion": "16",
            "deviceName": "iPhone 14",
            "app": config.app,
            'bstack:options': {
                "projectName": "First Python project IOS",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test_ios",
                "userName": config.user_name,
                "accessKey": config.access_key
            }
        })
        browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    browser.config.timeout = config.timeout
    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG
    )
    allure.attach(
        browser.driver.page_source,
        name='Page source XML',
        attachment_type=allure.attachment_type.XML
    )
    session_id = browser.driver.session_id

    browser.quit()

    browser_stack_session = requests.get(f'https://api-cloud.browserstack.com/app-automate/sessions/{session_id}.json',
                                         auth=(config.user_name, config.access_key)).json()
    video_url = browser_stack_session['automation_session']['video_url']

    allure.attach(
        "<html><body>"
        "<video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'>"
        "</video>"
        "</body></html>",
        name='mobile video',
        attachment_type=allure.attachment_type.HTML
    )
