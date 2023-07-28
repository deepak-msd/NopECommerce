from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    useremail_id = "Email"
    Password_id = "Password"
    LoginButton = "//button[contains(text(),'Log in')]"
    Logout_linktext = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def SetUsername(self, useremail):
        self.driver.find_element(By.ID, self.useremail_id).clear()
        self.driver.find_element(By.ID, self.useremail_id).send_keys(useremail)

    def SetPassword(self, password):
        self.driver.find_element(By.ID, self.Password_id).clear()
        self.driver.find_element(By.ID, self.Password_id).send_keys(password)

    def ClickLoginButton(self):
        self.driver.find_element(By.XPATH, self.LoginButton).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH, self.Logout_linktext).click()
