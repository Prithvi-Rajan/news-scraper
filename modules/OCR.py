import pytesseract
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
import os
import datetime


class OCR:
    def _get_text(self, image, words_list):
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        image = image.convert('RGB')
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        image.save(f'./temp/{current_date}.png')
        self.text = pytesseract.image_to_string(image, lang='tam')
        # os.remove(f'./temp/{current_date}.png')
        self.text_words = self.text.split(' ')
        return self._get_words(words_list)

    def _get_words(self, words_list):
        hit = True
        for word in words_list:
            if self.text.find(word) < 0:
                hit = False
                break
        return hit

    def check_for_shutdown(self, image):
        words = ['பொள்ளாச்சி', 'மின்தடை']
        return self._get_text(image, words)


# def main():
#     ocr = OCR()
#     images = ['https://i.ibb.co/bK5NNG5/Screenshot-2021-12-30-120709.jpg']
#     words = ['பொள்ளாச்சி', 'மின்தடை']
#     if ocr.get_text(images, words):
#         print('found')
#     else:
#         print('not found')


# if __name__ == '__main__':
#     main()
