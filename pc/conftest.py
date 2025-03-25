from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# 커맨드 라인 옵션 추가
# 명렁어 pytest --browser_name firefox
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome, firefox, edge"
    )


@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("해당 브라우저는 지원하지 않습니다")  # 예외 처리 추가

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
