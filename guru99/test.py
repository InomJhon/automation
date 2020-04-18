from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pytest
import XLUtils

 
def test_launching(browser): 
    browser.get("http://demo.guru99.com/V4/index.php")

    print("title: ", browser.title)