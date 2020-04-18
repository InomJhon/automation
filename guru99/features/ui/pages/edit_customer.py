from features.ui.all_imports import *

class EditCustomer(BasePage): 

    # Locators to login 
    new_customer_box = "/html/body/div[2]/div/div/ul/li[3]/a" # xpath
    customer_id_box = "cusid" # name
    submit_button_box = "AccSubmit" # name
    reset_button_box = "res" # name
    
    # Locators -> inside edit_customer page
    address_box = "addr" #by name
    city_box = "city" #by name
    state_box = "state" #by name
    zip_code_box = "pinno" #by name
    phone_number_box = "telephoneno" #by name
    email_box = "emailid" #by name
    submit_btn_box = "sub" # name

    def enter_customer_id(self, id): 
        self.enter_text_by_name(self.customer_id_box, id)

    def click_reset_button(self): 
        self.click_element_by_name(self.reset_button_box)

    def click_submit_button(self):
        self.click_element_by_name(self.submit_button_box)

    def enter_address(self, addr): 
        self.enter_text_by_name(self.address_box, addr)
    
    def enter_city(self, city): 
        self.enter_text_by_name(self.city_box, city) 
    
    def enter_state(self, state): 
        self.enter_text_by_name(self.state_box, state)

    def enter_zip(self, zip): 
        self.enter_text_by_name(self.zip_code_box, zip)

    def enter_phone_number(self, phone_number): 
        self.enter_text_by_name(self.phone_number_box, phone_number)

    def enter_email(self, email): 
        self.enter_text_by_name(self.email_box, email)

    def click_submit_btn(self): 
        self.click_element_by_name(self.submit_btn_box)
    

    
    