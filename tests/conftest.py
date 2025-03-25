from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://sem.home-learn.com/sigong/login/loginForm.do")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def login_credentials():
    return {
        "adm_id": "adm_sjcho88",
        "adm_pw": "89016410",
        "stu_id": "testplan98"
    }


