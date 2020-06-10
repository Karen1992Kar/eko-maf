from .base_page import BasePage
from .locators import ContactPages
import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'# optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class ContactPage(BasePage):

    def social_link(self):
        self.is_element_present(*ContactPages.INSTA_LINK)
        links = self.browser.find_elements(*ContactPages.INSTA_LINK)
        for url in links:
            link = url.get_attribute("href")
            result = re.match(regex, link)
            assert result, f"линк {link} не существует"


