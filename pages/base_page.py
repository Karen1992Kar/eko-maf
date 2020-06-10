from .locators import HomeLink
from .locators import ContactLink
from .locators import PrivateOrder
from . locators import OurWork


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def home_link(self):
        self.is_element_present(*HomeLink.HOME_LINK)

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

    def is_element_present(self, how, what):
        assert self.browser.find_element(how, what), "нету такой элемент "
