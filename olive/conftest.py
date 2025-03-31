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
    #options.appPackage = "com.oliveyoung"
    #options.appActivity = "com.oliveyoung.presentation.home.MainActivity"
    options.no_reset = True
    options.set_capability("noReset", False)
    # 원격 드라이버 생성 (앱 실행)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    driver.activate_app("com.oliveyoung")
    yield driver  # 테스트 함수에서 driver를 사용할 수 있도록 반환
    driver.terminate_app("com.oliveyoung")
    driver.quit()  # 테스트 후 드라이버 종료

@pytest.fixture(scope="session")
def login_credentials():
    return {
        "ID1" : "카카오 계정",
        "PW1" : "카카오 비밀번호",
        "ID2" : "slsss002",
        "PW2" : "0002"
    }


@pytest.fixture(scope="function")
def login_process(driver):
    def _login(ID, PW):
        # 로그인 절차 수행
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"olive.widget.EditText\").instance(0)").send_keys(ID)  # ID 입력
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"olive.widget.EditText\").instance(1)").send_keys(PW)  # PW 입력
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"로그인\")").click()  # 로그인 클릭
        return driver  # 로그인 후 드라이버 반환
    return _login