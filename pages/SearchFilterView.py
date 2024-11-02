from Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import re

# View after search performed 
class SearchFilterView(object):

    # Initialize elements that are visible 
    def __init__(self, driver):
        # Set up driver
        self.browser = driver
        
        # Filter visible so we are able to initialize
        self.filters = driver.find_element("xpath", Locator.filters)
        
        
    # Clicking to expand filter
    def setFilter(self):
        self.filters.click()
        
        
    # Using JS to click hidden elements
    def setHomeType(self):
        self.home_type = self.browser.find_element("xpath", Locator.home_type)
        self.browser.execute_script('arguments[0].click();', self.home_type)
        
        
    # Adding a filter option of +1 bath
    def setAddBath(self):
        self.add_bath = self.browser.find_element("xpath", Locator.add_bath)
        self.browser.execute_script('arguments[0].click();', self.add_bath)
        
       
    # Clicking the option to have a garage
    def setGarage(self):
        self.garage = self.browser.find_element("xpath", Locator.garage)
        self.browser.execute_script('arguments[0].click();', self.garage)
        
        
    # Apply the filter - webpage does it automatically it appears
    def setApplyFilter(self):
        self.apply_filter = self.browser.find_element("xpath", Locator.apply_filter)
        self.browser.execute_script('arguments[0].click();', self.apply_filter)
        

    def getFilteredHomes(self):
        return self.browser.find_element("xpath", Locator.filtered_list).text