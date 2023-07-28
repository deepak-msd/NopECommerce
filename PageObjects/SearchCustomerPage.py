from selenium.webdriver.common.by import By
import sys


class SearchCustomer:
    # Add Customer Page

    txtemail_id = "SearchEmail"
    txtfirstname_id = "SearchFirstName"
    txtlastname_id = "SearchLastName"
    btnsearchbutton_id = "search-customers"
    tableSearch_xpath = "//div[@id='customers-grid_wrapper']"
    table_xpath = "//table[@id='customers-grid']"
    tablerows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tablecolumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtemail_id).clear()
        self.driver.find_element(By.ID, self.txtemail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtfirstname_id).clear()
        self.driver.find_element(By.ID, self.txtfirstname_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtlastname_id).clear()
        self.driver.find_element(By.ID, self.txtlastname_id).send_keys(lname)

    def ClickButton(self):
        self.driver.find_element(By.ID, self.btnsearchbutton_id).click()

    def TableResults(self):
        (self.driver.find_element(By.XPATH, self.table_xpath))

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tablerows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
