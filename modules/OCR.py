import pytesseract
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
from urllib.request import urlretrieve
import os


class OCR:
    # given an list of url to an image, it will return the text in the image
    # the text will be in tamil language
    # return if given list of words are present in the text

    # tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'

    def get_text(self, urls, words_list):
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        for idx, url in enumerate(urls):
            im = Image.open(BytesIO(urlopen(url).read()))
            im = im.convert('RGB')
            im.save('./temp/{idx}.jpg')
            self.text = pytesseract.image_to_string(im, lang='tam')
            os.remove('./temp/{idx}.jpg')
            self.text_words = self.text.split(' ')
            return self._get_words(words_list)

    def _get_words(self, words_list):
        hit = True
        for word in words_list:
            if self.text.find(word) < 0:
                hit = False
                break
        return hit

    def check_for_shutdown(self, urls):
        words = ['பொள்ளாச்சி', 'மின்தடை']
        if self.get_text(urls, words):
            print('found')
        else:
            print('not found')


def main():
    ocr = OCR()
    images = ['https://i.ibb.co/bK5NNG5/Screenshot-2021-12-30-120709.jpg']
    words = ['பொள்ளாச்சி', 'மின்தடை']
    if ocr.get_text(images, words):
        print('found')
    else:
        print('not found')


if __name__ == '__main__':
    main()
