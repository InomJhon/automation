from features.ui.all_imports import *

class ChangePassword(BasePage): 

    # LOCATORS 
    old_password_box    = "oldpassword"     # by name
    new_password_box    = "newpassword"     # by name
    confirm_password_box = "confirmpassword" # by name
    submit_box = "sub" # by name
    reset_box = "res" # by name

    def enter_old_password(self, password): 
        self.enter_text_by_name(self.old_password_box, password)

    def enter_new_password(self, password): 
        self.enter_text_by_name(self.new_password_box, password)

    def enter_confirm_password(self, conf_password): 
        self.enter_text_by_name(self.confirm_password_box, conf_password)

    def click_submit_btn(self): 
        self.click_element_by_name(self.submit_box)

    def click_reset_btn(self): 
        self.click_element_by_name(self.reset_box)

    def take_care_alert(self, browser): 
        alert = browser.switch_to.alert
        txt = alert.text
        print("Alert window message >>", txt)
        alert.accept()