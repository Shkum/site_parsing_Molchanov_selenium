from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from PIL import Image
from pytesseract import image_to_string

import pytesseract


import os
os.putenv('TESSDATA_PREFIX','path/to/your/tessdata/file')
s = os.putenv('TESSDATA_PREFIX',r'C:\Program Files (x86)\Tesseract-OCR\tessdata\rus.traineddata')
print(s)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def tel_recon(self):
        image = Image.open('tel.gif')
        # print(image_to_string(image, lang='rus'))
        print(image_to_string(image))

    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        image.crop((x, y, x + width / 3, y + height)).save('tel.gif')  # set size of the crop    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.tel_recon()

    def navigate(self):
        self.driver.get('https://www.avito.ru/chelyabinsk/telefony/smartfon_htc_one_m7_dual_sim_2574911077?slocation=637640')
        button = self.driver.find_element("xpath",
                                          '//button[@class="button-button-eBrUW button-button_phone-_Yo3v button-button_card-AkthM button-button-CmK9a button-size-s-r9SeD button-success-_ytiQ"]')
        button.click()
        sleep(3)
        self.take_screenshot()
        image = self.driver.find_element("xpath",
                                         '//h2[@class="styles-module-root-nvJ_K styles-module-root-uDlrk styles-module-size_xxxl-Jv1dY styles-module-size_xxxl-JWdXg stylesMarningNormal-module-root-CpQir stylesMarningNormal-module-h1-IhXry styles-module-root_bottom-rV7ey styles-module-margin-bottom_20-DAp6T"]')
        location = image.location
        size = image.size
        self.crop(location, size)


def main():
    b = Bot()


if __name__ == '__main__':
    main()
