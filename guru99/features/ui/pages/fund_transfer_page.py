from features.ui.all_imports import *

class FundTransfer(BasePage): 

    # LOCATORS 
    payers_account_no_box   = "payersaccount"   # by name
    payees_account_no_box   = "payeeaccount"    # by name 
    amount_box              = "ammount"         # by name
    description_box         = "desc"            # by name
    submit_box              = "AccSubmit"       # by name
    reset_box               = "res"             # by name

    def enter_payers_account_no(self, number): 
        self.enter_text_by_name(self.payers_account_no_box, number)

    def enter_payees_account_no(self, number): 
        self.enter_text_by_name(self.payees_account_no_box, number)

    def enter_amount(self, amount): 
        self.enter_text_by_name(self.amount_box, amount)

    def enter_description(self, desc): 
        self.enter_text_by_name(self.description_box, desc)

    def click_submit_btn(self): 
        self.click_element_by_name(self.submit_box)
    
    def click_reset_btn(self): 
        self.click_element_by_name(self.reset_box)

    def take_care_alert(self, browser):
        alert = browser.switch_to.alert
        txt = alert.text
        print(txt)
        alert.accept()
    