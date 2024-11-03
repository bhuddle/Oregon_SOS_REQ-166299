from HomePage import *
from SearchFilterView import *

# Setting up initial browser for testing
service = Service(r".\driver\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('http://redfin.com/')
browser.set_page_load_timeout(120)
browser.implicitly_wait(5)
home = HomePage(browser)


# Checking for page load
def test_setup():
    state = home.browser.execute_script('return document.readyState')
    if state == 'complete':
        assert True
    else:
        assert False


# Search zip and check if URL has changed
def test_zip():
    home.setSearchZipResult('97116')
    if '97116' in home.browser.current_url:
        assert True


# Apply filters and check if page has changed number of homes available
def test_search():
    search = SearchFilterView(home.browser)
    search.setFilter()
    search.setHomeType()
    search.setAddBath()
    search.setGarage()
    search.setApplyFilter()
    homes = search.getFilteredHomes()
    if '90 homes' in homes:
        assert True
    else:
        assert False, homes


# Close session gracefully
def test_teardown():
    browser.close()
    if browser is None:
        assert True
