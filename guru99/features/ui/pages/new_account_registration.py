from features.ui.all_imports import *

class New_Customer_Registration(BasePage): 

    # Locators
    customer_id_box = "cusid" # name
    account_type_box = "selaccount" # name
    initial_deposit_box = "inideposit" # name
    submit_button_box = "button2" # name
    reset_button_box = "reset" # name


    def enter_customer_id(self, id): 
        self.enter_text_by_name(self.customer_id_box, id)

    def enter_account_type(self, value): 
        self.select_one_by_visible_text(self.account_type_box, value)

    def enter_initial_deposit(self, amount): 
        self.enter_text_by_name(self.initial_deposit_box, amount)

    def click_submit_button(self): 
        self.click_element_by_name(self.submit_button_box)

    def click_reset_button(self): 
        self.click_element_by_name(self.reset_button_box)