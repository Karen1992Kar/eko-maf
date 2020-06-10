from selenium.webdriver.common.by import By


class HomeLink:
    HOME_LINK = (By.CSS_SELECTOR, "#headermenu > a > img")


class ContactLink:
    CONTACT_LINK = (By.CSS_SELECTOR, "#cssmenu > ul > li:nth-child(4) > a")


class ContactPages:
    INSTA_LINK = (By.CSS_SELECTOR, ".social-link")
    FB_LINK = (By.CSS_SELECTOR, "body > div:nth-child(3) > div > p:nth-child(5) > a:nth-child(3)")
    VK_LINK = (By.CSS_SELECTOR, "body > div:nth-child(3) > div > p:nth-child(5) > a:nth-child(4)")


class PrivateOrder:
    PRIVATE_ORDER = (By.CSS_SELECTOR, "#cssmenu > ul > li.button.unique-order")


class ModelContent:
    MODEL_CONTENT = (By.CSS_SELECTOR, "#uniqueForm")
    FIO = (By.CSS_SELECTOR, "#orders-fio")
    PHONE = (By.CSS_SELECTOR, "#orders-phone")
    EMAIL = (By.CSS_SELECTOR, "#orders-email")
    DESCRIPTION = (By.CSS_SELECTOR, "#orders-description")
    SUBMIT_CONTENT = (By.CSS_SELECTOR, "#submitUniqueForm")


class OurWork:
    OUR_WORK = (By.CSS_SELECTOR, "#cssmenu > ul > li:nth-child(3) > a")


class Works:
    WORKS = (By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div > div > p > button")


class WorkImages:
    WORK_IMAGES = (By.CSS_SELECTOR, "div.col-md-3")
    WORK_IMAGE = (By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div > a > img")


class ArrowKey:
    RIGHT_KEY = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-img-mobile.mfp-ready > div > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close")
    LEFT_KEY = (By.CSS_SELECTOR, "body > div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-img-mobile.mfp-ready > div > button.mfp-arrow.mfp-arrow-left.mfp-prevent-close")
    MFP_CLOSE = (By.CSS_SELECTOR, ".mfp-close")
