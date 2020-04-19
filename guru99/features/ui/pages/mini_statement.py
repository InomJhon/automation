from features.ui.all_imports import * 

class Mini_Statement(BasePage): 

    # LOCATORs 
    account_no_box = "accountno" # by name
    submit_box = "AccSubmit" # by name
    reset_box = "res" # by name

    def enter_account_no(self, number): 
        self.enter_text_by_name(self.account_no_box, number)

    def click_submit_btn(self): 
        self.click_element_by_name(self.submit_box)

    def click_reset_btn(self): 
        self.click_element_by_name(self.reset_box)