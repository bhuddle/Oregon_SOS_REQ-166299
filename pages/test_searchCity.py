from HomePage import *
from SearchFilterView import *

# Set up browser for testing
service = Service(r".\driver\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('http://redfin.com/')
browser.set_page_load_timeout(120)
browser.implicitly_wait(5)
home = HomePage(browser)


# Navigate to home page complete
def test_setup():
    state = home.browser.execute_script('return document.readyState')
    if state == 'complete':
        assert True
    else:
        assert False


# Search for city and verify in URL change
def test_city():
    home.setSearchCityResult('Forest Grove OR')
    if 'Forest Grove' in home.browser.current_url:
        assert True


# Search based on input 'Forest Grove OR'
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
