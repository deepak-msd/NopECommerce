import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    linkCustomer_menu_xpath = "(//*[@class='nav-link'])[21]" #xpath
    linkCustomer_option_xpath = "(//*[@class='nav-link'])[22]"
    AddnewCustomer_xpath = "//a[normalize-space()='Add new']"
    AddEmail_Id = "Email"
    AddPassword_id = "Password"
    AddFirstname_id = "FirstName"
    AddLastname_id = "LastName"
    AddMaleGender_id = "Gender_Male"
    AddFemaleGender_id = "Gender_Female"
    AddDOB_id = "DateOfBirth"
    AddCompany_id = "Company"
    CustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    lstitemsAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitemsForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    lstitemsGuests_xpath = "//li[contains(text(), 'Guests')]"
    lstitemsRegistered_xpath = "//li[contains(text(), 'Registered')]"
    lstitemsVendors_xpath = "//li[contains(text(), 'Vendors')]"
    AddNewsletter_xpath = "(//div[@role='listbox'])[1]"
    AddVendor_id = "VendorId"
    VendorsList_xpath = "//option[normalize-space()='Vendor 1']"
    AddComment_id = "AdminComment"
    SaveButton_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_xpath).click()

    def ClickCustomerOption(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_option_xpath).click()

    def AddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.AddnewCustomer_xpath).click()

    def EnterEmailId(self, email):
        self.driver.find_element(By.ID, self.AddEmail_Id).send_keys(email)

    def EnterPassword(self, password):
        self.driver.find_element(By.ID, self.AddPassword_id).send_keys(password)

    def CustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.CustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem =self.driver.find_element(By.XPATH, self.lstitemsRegistered_xpath)
        elif role == "Administrators":
            self.listitem= self.driver.find_element(By.XPATH, self.lstitemsAdministrators_xpath)
        elif role == "Guests":
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemsGuests_xpath)
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemsGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemsRegistered_xpath)
        elif role == "Vendors":
            self.listitem= self.driver.find_element(By.XPATH, self.lstitemsVendors_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemsGuests_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def Managerforvendor(self, value):
        val= Select(self.driver.find_element(By.ID, self.AddVendor_id))
        val.select_by_visible_text(value)

    def SetGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.AddMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.AddFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.AddMaleGender_id).click()

    def EnterFirstname(self, fname):
        self.driver.find_element(By.ID, self.AddFirstname_id).send_keys(fname)

    def EnterLastname(self, lname):
        self.driver.find_element(By.ID, self.AddLastname_id).send_keys(lname)


    def AddDOB(self, dob):
        self.driver.find_element(By.ID, self.AddDOB_id).send_keys(dob)

    def AddCompanyInfo(self, companyname):
        self.driver.find_element(By.ID, self.AddCompany_id).send_keys(companyname)

    def AddNewsletter(self):
        self.driver.find_element(By.XPATH, self.AddNewsletter_xpath).click()

    def AddvendorInfo(self):
        self.driver.find_element(By.ID, self.AddVendor_id).click()

    def AddVendorfromlist(self):
        self.driver.find_element(By.XPATH, self.VendorsList_xpath).click()

    def Addcomments(self,contents):
        self.driver.find_element(By.ID, self.AddComment_id).send_keys(contents)

    def ClickSaveButton(self):
        self.driver.find_element(By.XPATH, self.SaveButton_xpath).click()





