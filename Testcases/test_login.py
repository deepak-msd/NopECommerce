import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_Homepagetitle(self, setup):

        self.logger.info("*********** Test_001_login *********")
        self.logger.info("*********** Verifying Home Page Title *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Home Page Title Test is Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Homepagetitle.png")
            self.driver.close()
            self.logger.error("*********** Home Page Title Test is Failed *********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Loginpage(self, setup):
        self.logger.info("*********** Verifying the Login Test *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLoginButton()
        post_act_title = self.driver.title
        if post_act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********** Login Test is Passed *********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Loginpage.png")
            self.driver.close()
            self.logger.error("*********** Login Title Test is Failed *********")
            assert False
