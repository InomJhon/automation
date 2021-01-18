from features.ui.all_imports import *

#UPDATE
class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = ActionChains(self.driver)
        self.logger = utils.create_logger()

    def enter_text_by_id(self, id_box, phrase):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.ID, id_box)))
            element.clear()
            element.send_keys(phrase)
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element}")


    def enter_text_by_xpath(self, xpath, phrase):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(phrase)
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element}")


    def enter_text_by_name(self, name, phrase):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.NAME, name)))
            element.clear()
            element.send_keys(phrase)
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element}")


    def click_element_by_xpath(self, xpath):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element}")


    def click_element_by_name(self, name):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.NAME, name)))
            element.click()
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element}")

    def click_element_by_id(self, by_id):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.ID, by_id)))
            element.click()
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element}")
    
    def click_radio_button_element_by_xpath(self, xpath):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if not element.is_selected(): 
                element.click()
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element}")


    def enter_hover_over(self, xpath, btn_xpath): #xpath, btn_xpath 
        try: 
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.actions.move_to_element(element).perform()
            btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, btn_xpath)))
            btn.click()
        except NoSuchElementException: 
            self.take_screenshot('error')
            #self.logger.error(f"element was not found {element}")

    
    def do_dd(self, elm1_xpath, elm2_xpath): 
        try:
            element1 = self.wait.until(EC.presence_of_element_located((By.XPATH, elm1_xpath)))
            element2 = self.wait.until(EC.presence_of_element_located((By.XPATH, elm2_xpath)))
            self.actions.drag_and_drop(element1, element1).perform()
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {element1}{element2}")


    def take_screenshot(self, phrase=""):
        filepath = f"./screenshots/{phrase}{utils.get_timestamp()}.png"
        self.driver.save_screenshot(filepath)
        #self.logger.info(f"screenshot is taken :{filepath}")


    def scroll_down(self, f, t): 
        self.driver.execute_script("window.scrollBy("+str(f)+","+str(t)+");")


    def is_alert_present(self): 
        try:
            self.driver.switch_to.alert
            return True
        except NoAlertPresentException: 
            return False


    def take_care_alert(self):
        alert = self.driver.switch_to.alert
        txt = alert.text
        print("Alert message >>>", txt)
        alert.accept()


    def select_drop_down_by_visible_text(self, by_id, text): 
        element = Select(self.driver.find_element_by_id(by_id))
        element.select_by_visible_text(text)

    def select_radio_btn(self, by_id): 
        element = self.driver.find_element_by_id(by_id)
        if not element.is_selected(): 
            element.click()

        
            