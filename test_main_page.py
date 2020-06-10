from pages.contact_page import ContactPage
from pages.main_page import MainPage
from pages.private_order import PrivateOrder
import time
import pytest
link = "http://xn----7sbzhhkhe0bh1c.xn--p1ai/web/"


@pytest.mark.home_link
def test_home_button(browser):
    page = MainPage(browser, link)
    page.open()
    page.home_link()


@pytest.mark.contact_check
def test_contact_page(browser):
    page = ContactPage(browser, link)
    page.open()
    page.contact_link()
    page.go_tu_contact_page()
    page.social_link()
    time.sleep(5)


@pytest.mark.private_order
def test_private_order(browser):
    page = PrivateOrder(browser, link)
    page.open()
    page.go_tu_private_order()
    page.modal_present_element()
    time.sleep(5)

