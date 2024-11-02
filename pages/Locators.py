# Locators based on XPATH for selenium
class Locator(object):
    # Home Page locators
    login = "//button[contains(.,'Sign in')]"
    sign_up = "//span[contains(.,'Join')]"
    search_button = "//button[@value='']"
    search_bar = "//input[@id='search-box-input']"

    # Search page locators
    filters = '//*[@id="WideSidepaneHeader--container"]/div/form/div[5]'
    home_type = '//*[@id="filterContent"]/div/div[5]/div[2]/div/div[1]'
    add_bath = '//*[@id="filterContent"]/div/div[4]/div[2]/div/div[4]'
    garage = ('//*[@id="filterContent"]/div/div[8]/div[2]/div[1]/div[1]/'
              'div[1]/div[2]/div/div[3]')
    apply_filter = '//*[@id="searchForm"]/form/div[2]/div/div[2]/div/button'
    filtered_list = ('//*[@id="sidepane-header-sticky-container"]/div[2]'
                     '/div/div[1]')
