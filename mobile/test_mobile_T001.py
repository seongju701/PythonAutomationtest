import pytest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from mobile.conftest import login_credentials

@pytest.mark.usefixtures("driver")
class TestOne:
    def test_login1(self, driver):
        # 권한 허용 버튼 클릭
        try:
            # 권한 허용 버튼들이 표시되면 클릭
            driver.find_element(by=AppiumBy.ID,value="com.homelearn.schoollearn:id/popup_check_permission_btn_confirm").click()
            driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
            driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
            driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/permission_allow_button").click()
        except Exception as e:
            print("권한 팝업 처리 중 오류 발생 또는 팝업이 표시되지 않음:", e)
            # 권한 허용 버튼 클릭
        try:
            # 미성년자 앱 접근 확인
            driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                value="new UiSelector().className(\"android.view.View\").instance(5)").click()
            driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText").click()
            keycodes = [8, 16, 15, 15]  # '1988 입력
            for keycode in keycodes:
                driver.execute_script('mobile: pressKey', {"keycode": keycode})
            driver.execute_script('mobile: hideKeyboard')
            driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"확인\")").click()
            sleep(2)
        except Exception as e:
            print("권한 팝업 처리 중 오류 발생 또는 팝업이 표시되지 않음:", e)

    def test_login2(self,driver,login_credentials):
        #비밀번호 오류 팝업 확인
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"android.widget.EditText\").instance(0)").send_keys(login_credentials["ID1"])
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"android.widget.EditText\").instance(1)").send_keys(login_credentials["PW2"])
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"로그인\")").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"비밀번호가 맞지 않거나\n등록된 사용자가 아닙니다.\")").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"확인\")").click()
        #정상적으로 로그인 확인
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"android.widget.EditText\").instance(0)").send_keys(login_credentials["ID1"])
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().className(\"android.widget.EditText\").instance(1)").send_keys(login_credentials["PW1"])
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"로그인\")").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"1\")").click()
        #로그아웃
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"닫기버튼\")").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"로그아웃\")").click()
        #로그인 유지 상태 로그인
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(0)").send_keys(login_credentials["ID1"])
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(1)").send_keys(login_credentials["PW1"])
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"로그인 유지\")").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"로그인\")").click()
        driver.terminate_app("com.homelearn.schoollearn")
        driver.activate_app("com.homelearn.schoollearn")
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"1\")").click()

    def test_login3(self, driver,login_process,login_credentials):
        try:
            driver = login_process(login_credentials["ID1"],login_credentials["PW1"])  # login_process에 ID와 PW 전달하여 로그인 수행
            print("이건가")
        except Exception as e:
            print("권한 팝업 처리 중 오류 발생 또는 팝업이 표시되지 않음:", e)
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"속담의 달인\")").click()
        driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Image").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"닫기\").instance(1)").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"날씨\")").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"날씨\")").click()
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value="new UiSelector().className(\"android.widget.Button\").instance(0)").click()
        driver.find_element(by=AppiumBy.ID, value="com.homelearn.schoollearn:id/txtMessage").click()
        driver.find_element(by=AppiumBy.ID, value="com.homelearn.schoollearn:id/btnYes").click()