import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.AddcustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    def test_searchCustomerByName(self, setup):
        self.logger.info("**** Search Customer By Name *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLoginButton()
        self.logger.info("****** Login Successful *****")
        self.logger.info("******** Starting to search Customer by Name *****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickCustomerMenu()
        self.addcust.ClickCustomerOption()
        self.logger.info("**** Searching Customer By Name *******")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Arthur")
        searchcust.setLastName("Holmes")
        searchcust.ClickButton()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Arthur Holmes")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchCustomerByName_pass_scr.png")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")

