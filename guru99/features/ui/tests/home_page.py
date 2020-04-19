from features.ui.all_imports import *

data = utils.yaml_loader("/Users/inomnematov/Desktop/automation/guru99/data/configs.yaml") 
logger = utils.create_logger()

# # # ================================================================= # # # 

# def test_login(browser): 
    
#     # Data 
#     url = data['url']
#     user_name = data['username']
#     password = data['password']
#     browser.get(url)

#     login_page = Login(browser)
#     logger.info("Login page started...")
#     login_page.enter_username(user_name)
#     login_page.enter_password(password)
#     login_page.click_login()
#     assert browser.title == "Guru99 Bank Manager HomePage"
#     manager_id = (browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[3]/td").text)
#     assert "Manger Id : mngr254844" == manager_id, "failed "
#     logger.info("Login, Taking screenshot...")
#     login_page.take_screenshot()
#     logger.info("Login test complited")
#     # browser.back()

# # # ================================================================= # # # 

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
        
# # # ================================================================= # # # 

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

# # # ================================================================= # # # 

# def test_edit_customer(browser): 
#     edit_customer = EditCustomer(browser)

#     edit_customer.click_element_by_xpath("/html/body/div[3]/div/ul/li[3]/a")
    
#     edit_customer.enter_customer_id("19757")
#     edit_customer.click_submit_button()
    
#     # do separate method in edit_customer.py for handeling alert
#     if edit_customer.is_alert_present(): 
#         logger.info("Switing to Alert")
#         alert = browser.switch_to.alert
#         alert_text = alert.text
#         print('\n', '-',alert_text, '-')
#         sleep(2)
#         alert.accept()
#         sleep(2)

#     edit_customer.enter_city("bbb")
#     sleep(2)
#     #edit_customer.click_submit_btn()
#     logger.info("Done tesing edit customer page")
#     sleep(2)

# # # ================================================================= # # # 

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

# # # ================================================================= # # # 

# def test_new_account_registration(browser): 
#     browser.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
#     new_account_reg = New_Customer_Registration(browser)

#     new_account_reg.enter_customer_id("76814")
#     new_account_reg.enter_account_type("Current")
#     new_account_reg.enter_initial_deposit("600")
    
#     sleep(3)
#     new_account_reg.click_reset_button()

# # # ================================================================= # # # 

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

# def test_deposit(browser): 
    
#     browser.get("http://demo.guru99.com/V4/manager/DepositInput.php")
#     deposit = Deposit(browser)

#     deposit.enter_account_no("77292")
#     deposit.enter_amount("100")
#     deposit.enter_description("added $100")
#     sleep(2)
#     deposit.click_submit_btn()
#     sleep(2)

#     if deposit.is_alert_present(): 
#         deposit.take_care_alert(browser)

#     assert "Account 77292" in browser.find_element_by_xpath("//*[@id='deposit']/tbody/tr[1]/td/p").text
    
#     print(browser.find_element_by_xpath("//*[@id='deposit']/tbody/tr[23]/td[2]").text)

# # # ================================================================= # # # 

# def test_withdrawal(browser): 
    
#     browser.get("http://demo.guru99.com/V4/manager/WithdrawalInput.php")
#     assert "Withdrawal" in browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text
    
#     withdrawal = Withdrawal(browser)

#     withdrawal.enter_account_no("77292")
#     withdrawal.enter_amount("100")
#     withdrawal.enter_description("took $100")
#     sleep(2)
#     withdrawal.click_submit_btn()
#     sleep(2)

#     if withdrawal.is_alert_present(): 
#         withdrawal.take_care_alert(browser)

#     assert "Account 77292" in browser.find_element_by_xpath("//p[@class='heading3']").text
    
#     print(browser.find_element_by_xpath("//*[@id='withdraw']/tbody/tr[23]/td[2]").text)

# # # ================================================================= # # # 

# def test_fund_transfer(browser): 

#     browser.get("http://demo.guru99.com/V4/manager/FundTransInput.php")
#     assert "Fund transfer" == browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text
#     print(browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text)
    
#     fund_transfer = FundTransfer(browser)

#     fund_transfer.enter_payers_account_no("77292")
#     fund_transfer.enter_payees_account_no("77295")
#     fund_transfer.enter_amount("10")
#     fund_transfer.enter_description("adf")
#     sleep(2)

#     fund_transfer.click_submit_btn()

#     if fund_transfer.is_alert_present(): 
#         fund_transfer.take_care_alert(browser)

#     sleep(2)

#     txt = browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/p").text
#     txt = txt.strip()
#     print("text >>>" , txt)
#     assert "Fund Transfer Details" == txt
#     sleep(2)

# # # ================================================================= # # # 

# def test_change_password(browser): 

#     browser.get("http://demo.guru99.com/V4/manager/PasswordInput.php")

#     print("-"+browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text+"-")
#     assert "Change Password" == (browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text).strip()

#     change_password = ChangePassword(browser)

#     change_password.enter_old_password("ArUbUpa")
#     change_password.enter_new_password("222$")
#     change_password.enter_confirm_password("222$")
#     sleep(2)
#     change_password.click_submit_btn()
    
#     if change_password.is_alert_present(): 
#         change_password.take_care_alert(browser)

# # # ================================================================= # # # 

# def test_balance_enquiry(browser): 
#     browser.get("http://demo.guru99.com/V4/manager/WithdrawalInput.php")
#     print("-"+browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text+"-")

#     balance_enquiry = Balance_Enquiry(browser)

#     balance_enquiry.enter_account_no("123")
#     balance_enquiry.enter_amount("123")
#     balance_enquiry.enter_description("aaa")
#     sleep(2)
    
#     balance_enquiry.click_submit_btn()

#     if balance_enquiry.is_alert_present(): 
#         balance_enquiry.take_care_alert()

# # # ================================================================= # # # 


def test_mini_statement(browser): 
    browser.get("http://demo.guru99.com/V4/manager/MiniStatementInput.php")
    txt = (browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text).strip()
    print(txt)
    assert "Mini Statement Form" == txt

    mini_statement = Mini_Statement(browser)

    mini_statement.enter_account_no("123")
    sleep(2)
    mini_statement.click_submit_btn()

    if mini_statement.is_alert_present(): 
        mini_statement.take_care_alert()

    txt = (browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/p").text).strip()
    print(txt)
    assert "Last Five Transaction Details for Account No: 77292" == txt

# # # ================================================================= # # # 

