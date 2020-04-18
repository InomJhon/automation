from features.ui.all_imports import *

class Edit_Account(BasePage): 

    # Locators 
    account_no_box = "accountno" # by name 
    submit_button_box = "AccSubmit" # by name
    reset_button_box = "res" # by name
    type_of_account_box = "a_type" # by name
    reset_btn_box = "AccReset" # by name

    def enter_account_number(self, number): 
        self.enter_text_by_name(self.account_no_box, number)

    def click_submit_button(self): 
        self.click_element_by_name(self.submit_button_box)

    def click_reset_button(self): 
        self.click_element_by_name(self.reset_button_box)

    def enter_new_type_of_account(self, value): 
        self.select_one_by_visible_text(self.type_of_account_box, value)
    
    def click_reset_btn(self): 
        self.click_element_by_name(self.reset_btn_box)

