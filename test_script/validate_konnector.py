"""
we create new konnector and validate Trigger and Action button using python and selenium
"""

# common
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# sleep
from time import sleep
# own package
from Data import data
from Locator import locator

class validate_konnector():

    def __init__(self,url):
        self.url=url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def boot(self):
        """
        this method get the url and maximize window
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(10)

    def login(self):
        """
        This method login konnectify page
        :return:navigate to home page of konnectors
        """
        sleep(2)
        # send mail and password and click login botton
        self.driver.find_element(By.XPATH, locator.WebLocator().mail_locator).send_keys(data.WebData().mail)
        sleep(2)
        self.driver.find_element(By.XPATH, locator.WebLocator().password_locator).send_keys(data.WebData().password)
        self.driver.find_element(By.XPATH, locator.WebLocator().login_button_locator).click()
        sleep(10)
        # check current url is equal to home page of konnectors url
        assert self.driver.current_url == "https://chitti2.konnectify.io/konnectors"

    def create_Konnector(self):
        """
        This method create new konnector
        """
        sleep(2)
        self.driver.find_element(By.XPATH, locator.WebLocator().create_konnector_locator).click()
        sleep(4)
        assert self.driver.current_url == "https://chitti2.konnectify.io/configure/new"
        print("konnecter is created successfully")


    def validate_Trigger(self):
        """
        This method validate Trigger field
        """
        sleep(2)
        # click Trigger button
        self.driver.find_element(By.XPATH, locator.WebLocator().Trigger_locator).click()
        sleep(3)
        # click search field and enter gmail text
        search= self.driver.find_element(By.XPATH, locator.WebLocator().search_button)
        search.click()
        search.send_keys("Gmail")
        # select Gmail app
        self.driver.find_element(By.XPATH, locator.WebLocator().Trigger_mail_locator).click()
        sleep(3)
        # select connection
        self.driver.find_element(By.XPATH,locator.WebLocator().select_connection).click()
        # select connection option
        self.driver.find_element(By.XPATH, locator.WebLocator().option_connection).click()
        sleep(4)
        # select event
        self.driver.find_element(By.XPATH, locator.WebLocator().select_event).click()
        self.driver.find_element(By.XPATH, locator.WebLocator().email_trigger).click()
        sleep(3)
        # click continue button to redirect to data output page
        self.driver.find_element(By.XPATH, locator.WebLocator().continue_configure).click()
        # click continue button in data output page ane ensure that our Trigger field changed green tick
        sleep(2)
        self.driver.find_element(By.XPATH, locator.WebLocator().continue_dataoutput).click()
    def validate_Action(self):
       # click action button
       self.driver.find_element(By.XPATH, locator.WebLocator().action_locator).click()
       # select app
       self.driver.find_element(By.XPATH, locator.WebLocator().action_select_app).click()
       sleep(3)
       # select connection
       self.driver.find_element(By.XPATH, locator.WebLocator().action_google_form_locator).click()
       # create connection
       self.driver.find_element(By.XPATH, locator.WebLocator().choose_connection).click()
       # enter connection name
       self.driver.find_element(By.XPATH, locator.WebLocator().connection_name).send_keys("testing")
       # click validate account
       self.driver.find_element(By.XPATH, locator.WebLocator().validate_account_loacator).click()
       # after validate account click save account
       self.driver.find_element(By.XPATH, locator.WebLocator().save_account).click()
       # select event
       self.driver.find_element(By.XPATH, locator.WebLocator().action_even).click()
       # select event drop down option
       self.driver.find_element(By.XPATH, locator.WebLocator().action_event_option).click()
       # click continue button in action configure
       self.driver.find_element(By.XPATH, locator.WebLocator().action_continue).click()
       # enter google form id
       self.driver.find_element(By.XPATH, locator.WebLocator().google_formid_locator).send_keys("Divya")
       # we got blue tick in action field
    def quit(self):
        self.driver.quit()



obj=validate_konnector("https://chitti2.konnectify.io/login")
obj.boot()
obj.login()
obj.create_Konnector()
obj.validate_Trigger()
obj.validate_Action()