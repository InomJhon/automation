from features.ui.all_imports import *
from features.ui.pages import registration_page
from time import sleep

data = utils.yaml_loader("/Users/inomnematov/Desktop/automation/insurance/data/configs.yaml")
logger = utils.create_logger()

def test_registration(browser): 

    # Data from yaml
    browser.get(data['url'])

    txt = (browser.find_element_by_css_selector("body:nth-child(2) div.content:nth-child(7) > h1:nth-child(3)").text)
    assert txt == "Sign up as a new user"

    test_registration = Registration_page(browser)
    
    logger.info("Entering new customer info ...")
    test_registration.pick_title(data['title'])
    test_registration.enter_first_name(data['first_name'])
    test_registration.enter_surname(data['last_name'])
    test_registration.enter_phone_number(data['phone_number'])
    test_registration.pick_year_of_birth(data['year_of_birth'])
    test_registration.pick_month_of_birth(data['month_of_birth'])
    test_registration.pick_day_of_birth(data['day_of_birth'])
    test_registration.pick_provisional()
    #test_registration.pick_full()
    test_registration.enter_street_and_address(data['year_of_birth'])
    test_registration.enter_city(data['city'])
    test_registration.enter_country(data['country'])
    test_registration.enter_post_code(data['zip'])
    test_registration.enter_email(data['email'])
    test_registration.enter_password(data['password'])
    test_registration.enter_confirm_password(data['password'])
    logger.info("done entering new custoemr info ...")

    sleep(2)
    #test_registration.click_create_btn()
    sleep(2)

# # # # ------------------------------------------------ # # #

# def test_login(browser):
#     browser.get("http://demo.guru99.com/insurance/v1/index.php")
#     assert (browser.title) == "Insurance Broker System - Login"

#     login = Login(browser)
#     login.enter_email("aaa@gmail.com")
#     login.enter_password("111")
#     login.click_login_btn()

#     assert (browser.find_element_by_id("tabs-1").text) == "Broker Insurance WebPage"
# # # # ------------------------------------------------ # # #

# def test_request_quotation(browser): 
#     browser.find_element_by_id("ui-id-2").click()
#     verify = browser.find_element_by_xpath("//*[@id='tabs-2']/h2")
#     assert verify.text == "Request a quotation"
#     print(verify.text)
    

#     request_quotation = Request_Quotation(browser)

#     request_quotation.pick_break_down_cover("At home")
    
#     request_quotation.pick_windScreenRepair_yes_btn()
#     request_quotation.enter_incidents("1")
#     request_quotation.enter_registration("1")
#     request_quotation.enter_annual_mileage("1000")
#     request_quotation.enter_estimated_value("1000")

#     request_quotation.pick_parking_location("Public Place")
    
#     request_quotation.pick_start_of_policy_year("2020")
#     request_quotation.pick_start_of_policy_month("April")
#     request_quotation.pick_start_of_policy_day("10")
#     sleep(3)
#     request_quotation.click_calculate_premium_btn()
#     sleep(3)
#     request_quotation.click_save_quotation_btn()
#     sleep(10)