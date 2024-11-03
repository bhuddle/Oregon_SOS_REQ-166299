from Locators import Locator


# View after search performed
class SearchFilterView(object):

    # Initialize elements that are visible
    def __init__(self, driver):
        # Set up driver
        self.browser = driver

        # Filter visible so we are able to initialize
        self.filters = ''
        self.home_type, self.add_bath, self.garage, self.apply_filter = \
            ('', '', '', '')

    # Clicking to expand filter
    def setFilter(self):
        self.browser.implicitly_wait(5)
        self.filters = self.browser.find_element("xpath", Locator.filters)
        self.filters.click()

    # Using JS to click hidden elements
    def setHomeType(self):
        self.browser.implicitly_wait(5)
        self.home_type = self.browser.find_element("xpath", Locator.home_type)
        self.browser.execute_script('arguments[0].click();', self.home_type)

    # Adding a filter option of +2 bath
    def setAddBath(self):
        self.browser.implicitly_wait(5)
        self.add_bath = self.browser.find_element("xpath", Locator.add_bath)
        self.browser.execute_script('arguments[0].click();', self.add_bath)

    # Clicking the option to have a garage
    def setGarage(self):
        self.browser.implicitly_wait(5)
        self.garage = self.browser.find_element("xpath", Locator.garage)
        self.browser.execute_script('arguments[0].click();', self.garage)

    # Apply the filter
    def setApplyFilter(self):
        self.browser.implicitly_wait(5)
        self.apply_filter = self.browser.find_element("xpath",
                                                      Locator.apply_filter)
        self.browser.execute_script('arguments[0].click();', self.apply_filter)

    # Get text output of how many homes with or without filter
    def getFilteredHomes(self):
        return self.browser.find_element("xpath", Locator.filtered_list).text
