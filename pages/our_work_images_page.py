from .base_page import BasePage
from .locators import WorkImages
from .locators import ArrowKey


class OurWorkImagesPage(BasePage):

    def work_images(self):
        self.is_element_present(*WorkImages.WORK_IMAGE)
        image = self.browser.find_element(*WorkImages.WORK_IMAGE)
        image.click()

    def right_left_arrow_key(self):
        self.is_element_present(*ArrowKey.RIGHT_KEY)
        images = len(self.browser.find_elements(*WorkImages.WORK_IMAGES))
        for _ in range(images):
            self.browser.find_element(*ArrowKey.RIGHT_KEY).send_keys(u'\ue007')

        for _ in range(images):
            self.browser.find_element(*ArrowKey.LEFT_KEY).click()

        self.browser.find_element(*ArrowKey.MFP_CLOSE).click()


