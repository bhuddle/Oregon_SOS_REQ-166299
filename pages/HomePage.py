from Locators import Locator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By

# Home page of redfin
class HomePage(object):

    # inintialize elements that are visible and set driver
    def __init__(self, driver):
        #setting driver
        self.browser = driver
        
        #setting locators
        self.login = driver.find_element("xpath", Locator.login)
        self.sign_up = driver.find_element("xpath", Locator.sign_up)
        self.search_button = driver.find_element("xpath", Locator.search_button)
        self.search_bar = driver.find_element("xpath", Locator.search_bar)
        
    
    # Returns the login element
    def getLogin(self):
        return self.login
        
    
    # Returns the sign up element
    def getSignUp(self):
        return self.sign_up
        
        
    # Returns the search button element
    def getSearchButton(self):
        return self.search_button
        
    
    # Returns the search bar element
    def getSearchBar(self):
        return self.search_bar
    
    
    # Clicks the login button
    def getLoginPage(self):
        # Not implementing past a click
        self.login.click()
    
    
    # Clicks the sign up button
    def getSignUpPage(self):
        self.sign_up.click()
        
        
    # Searches based on zip i.e. '97123'    
    def setSearchZipResult(self, zip):
        self.search_bar.clear()
        self.search_bar.send_keys(zip)
        self.search_button.click()
        return self.browser
        
    
    # Searches based on city entered
    # City required 'Hillsboro OR' to avoid duplicates
    def setSearchCityResult(self, city):
        self.search_bar.clear()
        self.search_bar.send_keys(city)
        self.search_button.click()
        return self.browser
