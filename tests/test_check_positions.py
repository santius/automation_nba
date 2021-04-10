from pytest_bdd import scenario, given, when, then
from selenium import webdriver
import pytest
from pages.home import HomePage
from pages.stats import StatsPage
from helpers.dataConnector import DBHelper

@pytest.fixture(autouse=True, scope='module')
def setup(request):
    global driver
    global home
    global stats
    global db
    driver = webdriver.Chrome()
    home = HomePage(driver, root_uri='https://www.nba.com')
    stats = StatsPage(driver)

@scenario('../features/check_positions.feature', 'Check team in first position')
def test_position():
    pass

@given("I open the browser and navigate to the NBA page")
def open_nba_page():
    home.get('/')

@given("I go to standings page")
def goto_standings():
    home.goto_standings(driver)
    stats.close_popup()

@then("I expect the team returned by the api call getFirstPlace to be the one in first place")
def check_first_place():
    assert stats.get_first_team_name().__contains__(DBHelper.getFirstPlace("127.0.0.1", 27017, "nba_sample"))