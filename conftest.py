import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g.chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("browser")

    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:/Users/vijayago/PycharmProjects/Automation_Framework1/drivers/chromedriver.exe")
    elif browser == "firefox":
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        driver = webdriver.Firefox(capabilities=cap,
            executable_path="C:/Users/vijayago/PycharmProjects/Automation_Framework1/drivers/geckodriver.exe")
    elif browser == "ie":
        driver = webdriver.Ie(
            executable_path="C:/Users/vijayago/PycharmProjects/Automation_Framework1/drivers/IEDriverServer.exe")
    else:
        print("Please enter valid browser")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Testing Completed")
