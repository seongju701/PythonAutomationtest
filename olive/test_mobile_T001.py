import pytest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from olive.conftest import login_credentials

@pytest.mark.usefixtures("driver")
class TestOne:
    def test_login1(self, driver):
        # 권한 허용 버튼 클릭
        driver.find_element(AppiumBy.ID, "com.oliveyoung:id/confirm_tv").click()
        driver.find_element(AppiumBy.ID, "com.olive.permissioncontroller:id/permission_allow_button").click()
        driver.find_element(AppiumBy.ID, "com.oliveyoung:id/close_iv").click()
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"todaySpecial\")").click()
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"home\")").click()
    def test_login2(self, driver,login_credentials):
        # 로그인 얼럿 창 확인
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiSelector().className(\"olive.view.View\").instance(9)").click()
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"loginId\")").send_keys(
            "jsjjoo88")
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"password\")").send_keys(login_credentials["PW1"]
            )
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"로그인\")").click()
        driver.find_element(AppiumBy.ID, "olive:id/message").click()
        driver.find_element(AppiumBy.ID, "olive:id/button1").click()

    def test_login3(self, driver,login_credentials):
        # 로그인 진행
        driver.find_element(AppiumBy.XPATH,"//androidx.compose.ui.platform.b1/olive.view.View/olive.view.View[5]").click()
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"custom-login-btn\")").click()
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"loginId--1\")").send_keys(login_credentials["ID1"])
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"password--2\")").send_keys(login_credentials["PW1"])
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"로그인\")").click()
        mypage = driver.find_element(By.XPATH,"//olive.widget.TextView[@resource-id=\"subTitle\"]").text
        assert "마이페이지" in mypage