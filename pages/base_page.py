from .locators import HomeLink
from .locators import ContactLink
from .locators import PrivateOrder
from . locators import OurWork
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .locators import OrderButton
from selenium.webdriver.support.ui import WebDriverWait
from .locators import Row
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def rekurs_comrade_for_sale(self, browser):
        if self.is_element_present(*Row.DIV_ROW):
            res = len(self.browser.find_elements(*Row.ROW))
            for row in range(1, res):
                follow = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "(/html/body/div[2]/div/div)[" + str(row) + "]/div/p/button")))
                follow.click()
                self.rekurs_comrade_for_sale(browser)
                browser.back()
        elif self.is_element_present(*OrderButton.ORDER_BUTTON):
            print("vse ok")

    def open(self):
        self.browser.get(self.url)

    def home_link(self):
        self.is_element_present(*HomeLink.HOME_LINK)
        self.browser.find_element(*HomeLink.HOME_LINK).click()

    def contact_link(self):
        self.is_element_present(*ContactLink.CONTACT_LINK)

    def go_tu_contact_page(self):
        link = self.browser.find_element(*ContactLink.CONTACT_LINK)
        link.click()

    def go_tu_our_work_page(self):
        self.is_element_present(*OurWork.OUR_WORK)
        link = self.browser.find_element(*OurWork.OUR_WORK)
        link.click()

    def go_tu_private_order(self):
        link = self.browser.find_element(*PrivateOrder.PRIVATE_ORDER)
        link.click()

    def click_on_the_links(self, how, what):
        result = self.browser.find_elements(how, what)
        return result

    def click_on_the_link(self, how, what):
        self.browser.find_element(how, what).click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
