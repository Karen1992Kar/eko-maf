from .base_page import BasePage
from . locators import Works


class OurWorkPage(BasePage):

    def works(self):
        link = self.browser.find_element(*Works.WORKS)
        link.click()





