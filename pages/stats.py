from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By

class StatsPage(PageObject):
    first_team = PageElement(xpath='//table/tbody/tr[1]/td[1]')
    popup = PageElement(class_name='ab-close-button')

    def close_popup(self):
        self.popup.click()

    def get_first_team_name(self):
        return self.first_team.text

        
