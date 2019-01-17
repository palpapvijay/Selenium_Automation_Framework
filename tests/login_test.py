from selenium import webdriver
import pytest
from pages.loginpage import LoginPage
from pages.homepage import Homepage
from utils import util as util
import allure



@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(util.URL)
        login = LoginPage(driver)
        login.enter_username(util.USERNAME)
        login.enter_password(util.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            home = Homepage(driver)
            home.click_welcome()
            home.click_logout()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as Error:
            print("Assertion Error Occured")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = util.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name = screenshotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/vijayago/PycharmProjects/Automation_Framework1/screenshots/"+screenshotName+".png")
            print(Error)
            raise

        except:
            print("There was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = util.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:/Users/vijayago/PycharmProjects/Automation_Framework1/screenshots/" + screenshotName + ".png")

        else:
            print("There was no Error")

        finally:
            print("Final block executed")