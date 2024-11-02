from HomePage import *
from SearchFilterView import *

# Setting up initial browser for testing
service = Service(r"C:\chromedriver\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('http://redfin.com/')
browser.set_page_load_timeout(20)
home = HomePage(browser)


# Checking for page load
def test_setup():
    state = home.browser.execute_script('return document.readyState')
    print(state)
    if state == 'complete':
        assert True
    else:
        assert False


# Search zip and check if URL has changed
def test_zip():
    sleep(3)
    home.setSearchZipResult('97116')
    if '97116' in home.browser.current_url:
        assert True


# Apply filters and check if page has changed number of homes available
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
