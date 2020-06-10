from .base_page import BasePage
from .locators import ModelContent


class PrivateOrder(BasePage):

    def modal_present_element(self):
        self.is_element_present(*ModelContent.MODEL_CONTENT)
        self.browser.find_element(*ModelContent.FIO).send_keys("Nikolay Petrov")
        self.browser.find_element(*ModelContent.PHONE).send_keys("+79858902845")
        self.browser.find_element(*ModelContent.EMAIL).send_keys("mkaragebakyan@gmail.com")
        self.browser.find_element(*ModelContent.DESCRIPTION).send_keys("lav sayta")
        self.is_element_present(*ModelContent.SUBMIT_CONTENT)

