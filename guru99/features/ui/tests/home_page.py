from features.ui.all_imports import *

data = utils.yaml_loader("/Users/inomnematov/Desktop/automation/guru99/data/configs.yaml")
logger = utils.create_logger()

def test_login(browser): 
    
    # Data 
    url = data['url']
    user_name = data['username']
    password = data['password']
    browser.get(url)

    login_page = Login(browser)
    logger.info("Login page started...")
    login_page.enter_username(user_name)
    login_page.enter_password(password)
    login_page.click_login()
    assert browser.title == "Guru99 Bank Manager HomePage"
    manager_id = (browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[3]/td").text)
    assert "Manger Id : mngr254844" == manager_id, "failed "
    logger.info("Login, Taking screenshot...")
    login_page.take_screenshot()
    logger.info("Login test complited")
    # browser.back()

# def test_parametrize(browser):
#     login_page = Login(browser)
#     path = "/Users/inomnematov/Desktop/automation/guru99/Book1.xlsx"
#     rows = XLUtils.get_row_count(path, "Sheet1")
#     for r in range(2, rows+1): 
#         user_name = XLUtils.read_data(path, "Sheet1", r, 1)
#         password = XLUtils.read_data(path, "Sheet1", r, 2)

#         login_page.enter_username(user_name)
#         login_page.enter_password(password)
#         login_page.click_login()
       
#         obj = browser.switch_to.alert
#         obj.accept()

#         if browser.title == "Guru99 Bank Manager HomePage": 
#             print("test passed")
#             XLUtils.write_data(path, "Sheet1", r, 3, "test Passed")
#         else: 
#             print("test failed")
#             XLUtils.write_data(path, "Sheet1", r, 3, "Test failed")
        

# def test_new_customer_registration(browser): 
#     new_customer = New_customer(browser)
#     # new customer btn 
#     new_customer.click_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a")
    
#     logger.info("Filling up New Customer form")
#     new_customer.enter_name("Inom")
#     new_customer.check_radio_button("f")
#     new_customer.enter_dateofbirth("03141986")
#     new_customer.enter_address("1947 Ocean Ave")
#     new_customer.enter_city("Brooklyn")
#     new_customer.enter_state("NY")
#     new_customer.enter_zip("112300")
#     new_customer.enter_phone_number("6665559999")
#     new_customer.enter_email("hoho@gmail.com")
#     new_customer.enter_password("1234")
#     new_customer.click_submit_button()
#     sleep(5)
#     logger.info("Complited New Customer Form")



def test_edit_customer(browser): 
    edit_customer = EditCustomer(browser)

    edit_customer.click_element_by_xpath("/html/body/div[3]/div/ul/li[3]/a")
    
    edit_customer.enter_customer_id("19757")
    edit_customer.click_submit_button()
    
    # do separate method in edit_customer.py for handeling alert
    if edit_customer.is_alert_present(): 
        logger.info("Switing to Alert")
        alert = browser.switch_to.alert
        alert_text = alert.text
        print('\n', '-',alert_text, '-')
        sleep(2)
        alert.accept()
        sleep(2)

    edit_customer.enter_city("bbb")
    sleep(2)
    #edit_customer.click_submit_btn()
    logger.info("Done tesing edit customer page")
    sleep(2)

# def test_delete_cusotmer(browser):
#     browser.get("http://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
#     delete_customer = BasePage(browser)

#     txt = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p")
#     print('\n',txt.text)
#     browser.find_element_by_name("cusid").send_keys("80725")
#     delete_customer.click_element_by_name("AccSubmit")
#     sleep(2)

#     if delete_customer.is_alert_present(): 
#         alert = browser.switch_to.alert
#         alert_text = alert.text
#         print('\n', '-',alert_text, '-')
#         sleep(2)
#         alert.accept()
#         sleep(2)
#         print((browser.switch_to.alert).text)

# def test_new_account_registration(browser): 
#     browser.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
#     new_account_reg = New_Customer_Registration(browser)

#     new_account_reg.enter_customer_id("76814")
#     new_account_reg.enter_account_type("Current")
#     new_account_reg.enter_initial_deposit("600")
    
#     sleep(3)
#     new_account_reg.click_reset_button()

# def test_edit_account(browser): 
#     browser.find_element_by_xpath("/html/body/div[3]/div/ul/li[6]/a").click()

#     edit_account = Edit_Account(browser)
#     edit_account.enter_account_number("76816")
#     edit_account.click_submit_button()
#     sleep(2)

#     edit_account.enter_new_type_of_account("Current")
#     sleep(2)
#     edit_account.click_submit_button()
#     sleep(2)