from features.ui.all_imports import *

class Login(BasePage): 

    # LOCATORs 
    email_box = "email" #by id
    password_box = "password" #by id 
    login_btn_box = "submit" #by name

    def enter_email(self, email): 
        self.enter_text_by_id(self.email_box, email) 

    def enter_password(self, password): 
        self.enter_text_by_id(self.password_box, password)

    def click_login_btn(self): 
        self.click_element_by_name(self.login_btn_box)