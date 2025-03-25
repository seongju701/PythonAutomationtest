# conftest.py

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()

    # 개별적으로 옵션 설정
    options.platform_name = "Android"
    options.device_name = "R9PT7000CKM"  # 실제 연결된 디바이스의 이름
    options.automation_name = "UiAutomator2"
    options.appPackage = "com.homelearn.schoollearn"
    options.appActivity = "com.homelearn.essential.activity.MainActivity"
    options.no_reset = True
    options.set_capability("noReset", True)
    # 원격 드라이버 생성 (앱 실행)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    driver.activate_app("com.homelearn.schoollearn")
    yield driver  # 테스트 함수에서 driver를 사용할 수 있도록 반환
    driver.terminate_app("com.homelearn.schoollearn")
    driver.quit()  # 테스트 후 드라이버 종료

@pytest.fixture(scope="session")
def login_credentials():
    return {
        "ID1" : "slsss001",
        "PW1" : "0001",
        "ID2" : "slsss002",
        "PW2" : "0002"
    }