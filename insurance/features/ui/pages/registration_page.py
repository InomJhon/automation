from features.ui.all_imports import *

class Registration_page(BasePage): 
    
    # LOCATORs  
    title_box       = "user_title"      # by id
    first_name_box  = "user_firstname"  # by id
    surname_box     = "user_surname"    # by id
    phone_box       = "user_phone"      # by id   

    # date of birth - drop downs
    year_box = "user_dateofbirth_1i" # by id - dropdown
    month_box = "user_dateofbirth_2i" # by id - dropdown
    day_box = "user_dateofbirth_3i" # by id - dropdown

    full_box = "licencetype_t" # by id - radion btn
    provisional_box = "licencetype_f" # by id - radio btn
    licence_period_box = "user_licenceperiod" #by id - dropdown btn
    occupation_box = "user_occupation_id" #by id - dropdown btn
    address_street_box = "user_address_attributes_street" # by id
    city_box = "user_address_attributes_city" # id 
    country_box = "user_address_attributes_county" # id
    post_code_box = "user_address_attributes_postcode" # by id 
    email_box = "user_user_detail_attributes_email" # by id
    password_box = "user_user_detail_attributes_password" # by id
    confirm_password_box = "user_user_detail_attributes_password_confirmation" # by id
    reset_btn_box = "resetform" # by id
    create_btn_box = "submit" #by name

    def pick_title(self, title):
        self.select_drop_down_by_visible_text(self.title_box, title)

    def enter_first_name(self, name):
        self.enter_text_by_id(self.first_name_box, name) 

    def enter_surname(self, surname): 
        self.enter_text_by_id(self.surname_box, surname)

    def enter_phone_number(self, phone): 
        self.enter_text_by_id(self.phone_box, phone)

    def pick_year_of_birth(self, year): 
        self.select_drop_down_by_visible_text(self.year_box, year)

    def pick_month_of_birth(self, month): 
        self.select_drop_down_by_visible_text(self.month_box, month)

    def pick_day_of_birth(self, day): 
        self.select_drop_down_by_visible_text(self.day_box, day)
    
    # needs re-factoring 
    def pick_provisional(self): 
        self.select_radio_btn(self.provisional_box)

    def pick_full(self): 
        self.select_radio_btn(self.full_box)
    #-------------------

    def enter_street_and_address(self, addr): 
        self.enter_text_by_id(self.address_street_box, addr)
    
    def enter_city(self, city): 
        self.enter_text_by_id(self.city_box, city)
    
    def enter_country(self, country): 
        self.enter_text_by_id(self.country_box, country)

    def enter_post_code(self, code): 
        self.enter_text_by_id(self.post_code_box, code) 

    def enter_email(self, email): 
        self.enter_text_by_id(self.email_box, email)

    def enter_password(self, password): 
        self.enter_text_by_id(self.password_box, password)
    
    def enter_confirm_password(self, conf_password): 
        self.enter_text_by_id(self.confirm_password_box, conf_password)
    
    def click_reset_btn(self): 
        self.click_element_by_id(self.reset_btn_box)

    def click_create_btn(self): 
        self.click_element_by_name(self.create_btn_box)
        




    




