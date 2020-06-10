from .base_page import BasePage
from .locators import ContactPages
import re
import pytest

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'# optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class ContactPage(BasePage):

    def page_instagram(self):
        self.is_element_present(*ContactPages.INSTA_LINK)
        link = self.browser.find_element(*ContactPages.INSTA_LINK).get_attribute("href")
        result = re.match(regex, link)
        assert result, "линк инстаграма не существует"

    def page_facebook(self):
        self.is_element_present(*ContactPages.FB_LINK)
        link = self.browser.find_element(*ContactPages.FB_LINK).get_attribute("href")
        result = re.match(regex, link)
        assert result, "линк Fb  не существует "

    def page_vk(self):
        self.is_element_present(*ContactPages.VK_LINK)
        link = self.browser.find_element(*ContactPages.VK_LINK).get_attribute("href")
        result = re.match(regex, link)
        assert result, "линк Вк  не существует "

