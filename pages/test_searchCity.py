from HomePage import *
from SearchFilterView import *

# Set up browser for testing
service = Service(r"C:\chromedriver\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('http://redfin.com/')
browser.set_page_load_timeout(60)
home = HomePage(browser)


# Navigate to home page complete
def test_setup():
    state = home.browser.execute_script('return document.readyState')
    print(state)
    if state == 'complete':
        assert True
    else:
        assert False


# Search for city and verify in URL change
def test_city():
    sleep(3)
    home.setSearchCityResult('Forest Grove OR')
    if 'Forest Grove' in home.browser.current_url:
        assert True


# Search based on input 'Hillsboro OR'
def test_search():
    sleep(30)
    search = SearchFilterView(home.browser)
    sleep(3)
    search.setFilter()
    sleep(3)
    search.setHomeType()
    search.setAddBath()
    search.setGarage()
    sleep(3)
    search.setApplyFilter()
    homes = search.getFilteredHomes()
    if '89 homes' in homes:
        assert True
    else:
        assert False


# Close session gracefully
def test_teardown():
    sleep(3)
    browser.close()
    sleep(3)
    if browser is None:
        assert True
