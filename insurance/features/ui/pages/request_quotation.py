from features.ui.all_imports import *

class Request_Quotation(BasePage): 

    # locators 
    break_down_cover_box = "quotation_breakdowncover" #by id - drop down 
    #------ radio button ----
    yes_box = "quotation_windscreenrepair_t" # by id - radio btn
    no_box = "quotation_windscreenrepair_f" # by id - radio btn 
    #-------------------------
    incidents_box = "quotation_incidents" #by id 
    registration_box = "quotation_vehicle_attributes_registration" #by id
    annual_mileage_box = "quotation_vehicle_attributes_mileage" #by id
    estimated_value_box = "quotation_vehicle_attributes_value" #by id
    parking_location_box = "quotation_vehicle_attributes_parkinglocation" # by id - drop down
    year_start_of_policy_box = "quotation_vehicle_attributes_policystart_1i" # by id - drop down
    month_start_of_policy_box = "quotation_vehicle_attributes_policystart_2i" # by id - drop down
    day_start_of_policy_box = "quotation_vehicle_attributes_policystart_3i" #by id - drop down

    btn_calculate_premium_box = "//*[@id='new_quotation']/div[8]/input[1]" #by xpath
    btn_reset_form_box = "resetquote" #by id 
    btn_save_quotation_box = "submit" #by name

    def pick_break_down_cover(self, value): 
        self.select_drop_down_by_visible_text(self.break_down_cover_box, value)

    def pick_windScreenRepair_yes_btn(self): 
        self.select_radio_btn(self.yes_box)

    def pick_windScreenRepair_no_btn(self): 
        self.select_radio_btn(self.no_box)

    def enter_incidents(self, value): 
        self.enter_text_by_id(self.incidents_box, value)

    def enter_registration(self, value): 
        self.enter_text_by_id(self.registration_box, value) 
    
    def enter_annual_mileage(self, value): 
        self.enter_text_by_id(self.annual_mileage_box, value) 

    def enter_estimated_value(self, value): 
        self.enter_text_by_id(self.estimated_value_box, value)

    def pick_parking_location(self, value): 
        self.select_drop_down_by_visible_text(self.parking_location_box, value)

    def pick_start_of_policy_year(self, year):
        self.select_drop_down_by_visible_text(self.year_start_of_policy_box, year)

    def pick_start_of_policy_month(self, month): 
        self.select_drop_down_by_visible_text(self.month_start_of_policy_box, month)

    def pick_start_of_policy_day(self, day): 
        self.select_drop_down_by_visible_text(self.day_start_of_policy_box, day)

    def click_calculate_premium_btn(self): 
        self.click_element_by_xpath(self.btn_calculate_premium_box)
    
    def click_reset_form_btn(self): 
        self.click_element_by_id(self.btn_reset_form_box)

    def click_save_quotation_btn(self): 
        self.click_element_by_name(self.btn_save_quotation_box)