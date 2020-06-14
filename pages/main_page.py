from .base_page import BasePage
from .locators import Menu


class MainPage(BasePage):

    def rows(self, browser):
        self.rekurs_comrade_for_sale(browser)

    def menu_check(self, browser):
        res = self.click_on_the_links(*Menu.LIES)
        for i in res:
            i.click()
            browser.back()


