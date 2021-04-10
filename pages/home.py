from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.stats import StatsPage

class HomePage(PageObject):
    link_standings = PageElement(partial_link_text='Standings')

    def goto_standings(self,driver):
        self.link_standings.click()
        return StatsPage(driver)