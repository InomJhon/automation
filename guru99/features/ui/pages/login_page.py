from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from features.ui.pages.base_page import BasePage

class Login(BasePage):

    #Locators
    user_id_box = ("uid") # by name
    password_box = ("password") # by name 
    login_btn_box = ("btnLogin") # by name

    def enter_username(self, uname): 
        self.enter_text_by_name(self.user_id_box, uname)
    
    def enter_password(self, phrase): 
        self.enter_text_by_name(self.password_box, phrase)
    
    def click_login(self): 
        self.click_element_by_name(self.login_btn_box)

    @property
    def get_title(self): 
        return self.driver.title
