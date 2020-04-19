from features.ui.all_imports import *

class Balance_Enquiry(BasePage): 

    # LOCATORs 
    account_no_box = "accountno"
    amount_box = "ammount"
    description_box = "desc"
    submit_box = "AccSubmit"
    reset_box = "res"

    def enter_account_no(self, number): 
        self.enter_text_by_name(self.account_no_box, number)
    
    def enter_amount(self, amount):
        self.enter_text_by_name(self.amount_box, amount)

    def enter_description(self, desc): 
        self.enter_text_by_name(self.description_box, desc)

    def click_submit_btn(self): 
        self.click_element_by_name(self.submit_box)

    def click_reset_btn(self): 
        self.click_element_by_name(self.reset_box)

