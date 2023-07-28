import pytest
import time

from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from PageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLoginButton()

        self.logger.info("********* Login is Successful ******")
        self.logger.info("******* Starting Add Customer Test *********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickCustomerMenu()
        self.addcust.ClickCustomerOption()
        self.addcust.AddNewCustomer()
        self.logger.info("****** Providing Customer Info ******")
        self.email = random_generator() + "@gmail.com"
        self.addcust.EnterEmailId(self.email)
        self.addcust.EnterPassword("test@123")
        self.addcust.CustomerRoles("Guests")
        self.addcust.Managerforvendor("Vendor 2")
        self.addcust.SetGender("Male")
        self.addcust.EnterFirstname("Deepak")
        self.addcust.EnterLastname("M S")
        self.addcust.AddDOB("07/20/1991")
        self.addcust.AddCompanyInfo("BusyQA")
        self.addcust.Addcomments("Sample comments")
        self.addcust.ClickSaveButton()

        self.logger.info("****** Saving Customer info ******")

        self.logger.info("***** Add Customer validated started")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_pass_scr.png")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_fail_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
