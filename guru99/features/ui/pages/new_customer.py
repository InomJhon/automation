from features.ui.all_imports import *

class New_customer(BasePage): 

    # Locators 
    new_customer_box = "name" #by name
    radio_button_female_box = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]" # xpath
    radio_button_male_box = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]" #by xpath
    birth_date_box = "dob" # by name
    address_box = "addr" #by name
    city_box = "city" #by name
    state_box = "state" #by name
    zip_code_box = "pinno" #by name
    phone_number_box = "telephoneno" #by name
    email_box = "emailid" #by name
    password_box = "password" #by name
    submit_button_box = "sub" #by name

    def enter_name(self, uname): 
        self.enter_text_by_name(self.new_customer_box, uname)

    def check_radio_button(self, gender): 
        if gender == "m":
            gender_picker = self.radio_button_male_box
        if gender == "f": 
            gender_picker = self.radio_button_female_box
        
        self.click_radio_button_element_by_xpath(gender_picker)

    def enter_dateofbirth(self, dob): 
        self.enter_text_by_name(self.birth_date_box, dob)

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

    def enter_password(self, password): 
        self.enter_text_by_name(self.password_box, password)

    def click_submit_button(self): 
        self.click_element_by_name(self.submit_button_box)
        

