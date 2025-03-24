from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("setup")
class TestOne:
    def test_Login_T001(self,setup):
        #로그인
        setup.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/form/fieldset/div[1]/input[1]").send_keys("adm_sjcho88")
        setup.find_element(By.XPATH, "//*[@id=\"login_pwd\"]").send_keys("89016410")
        setup.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/form/fieldset/div[1]/button").click()
        # 기본창 메뉴 확인
        setup.switch_to.window(setup.window_handles[0])
        gnbCount = setup.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div/div/div")
        # 관리자 계정 회원상담관리 클릭
        for gnb in gnbCount:
            gnbText = gnb.find_element(By.XPATH,"a").text
            print(gnbText)
            if gnbText=="회원상담관리":
                gnb.find_element(By.XPATH,"a").click()
                break
        #회원검색
        setup.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/a[1]").click()
        #팝업처리
        setup.switch_to.window(setup.window_handles[1])
        #학생검색
        setup.find_element(By.XPATH,"//*[@id=\"s_keyword\"]").send_keys("testplan98")
        setup.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div/div[1]/div/div[2]/button").click()
        #명시적 대기
        wait = WebDriverWait(setup,5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[1]/form/div[2]/div/div[2]/div[1]/table/tbody/tr/td[3]")))
        #학생팝업 이동
        setup.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div/div[2]/div[1]/table/tbody/tr/td[3]").click()
        setup.switch_to.window(setup.window_handles[2])
        stPopup = setup.find_element(By.XPATH,"/html/body/div[1]/div[1]/h1").text
        print(stPopup)


