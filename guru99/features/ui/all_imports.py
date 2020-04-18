from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import features.ui.step_definitions.utilities as utils
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from features.ui.pages.login_page import *
from features.ui.pages.new_customer import *
from features.ui.pages.edit_customer import *
from features.ui.pages.new_account_registration import *
from features.ui.pages.edit_account import *
import openpyxl
import XLUtils 