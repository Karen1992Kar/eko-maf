from pages.contact_page import ContactPage
from pages.main_page import MainPage
from pages.private_order import PrivateOrder
from pages.our_work_page import OurWorkPage
from pages.our_work_images_page import OurWorkImagesPage
import time
import pytest
link = "http://xn----7sbzhhkhe0bh1c.xn--p1ai/web/"


@pytest.mark.home_link                  # проверка кнопки главная
def test_home_button(browser):
    page = MainPage(browser, link)
    page.open()
    page.rows(browser)
    time.sleep(3)


@pytest.mark.contact_check              # проверка контакт
def test_contact_page(browser):
    page = ContactPage(browser, link)
    page.open()
    page.contact_link()
    page.go_tu_contact_page()
    page.social_link()
    time.sleep(5)


@pytest.mark.private_order              # проверка работы
def test_private_order(browser):
    page = PrivateOrder(browser, link)
    page.open()
    page.go_tu_private_order()
    page.modal_present_element()
    time.sleep(5)


@pytest.mark.our_work                   # проверка фото работы
def test_our_work(browser):
    page = OurWorkPage(browser, link)
    page.open()
    page.go_tu_our_work_page()
    page.works()
    page1 = OurWorkImagesPage(browser, browser.current_url)
    page1.work_images()
    page1.right_left_arrow_key()
    time.sleep(5)


@pytest.mark.menu
def test_menu(browser):
    page = MainPage(browser, link)
    page.open()
    page.menu_check(browser)
    time.sleep(3)




