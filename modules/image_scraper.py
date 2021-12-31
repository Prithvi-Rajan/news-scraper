# given an url to a website, returns a list of all the image urls in the webpage
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
# import OCR
# import requests
# import re


class ImageScraper:
    def __init__(self):
        self.clip_urls = []
        self.chunks = []
        self.options = Options()
        self.options.headless = True
        self.newspaper_image = None
        url = 'https://epaper.dinakaran.com/t/22485'
        self._getLastNewsPaperPage(url)
        self._create_images()
        self._get_chunks()
        self._concat_images()

    def _concat_images(self):
        width, height = 700, 744
        new_image = Image.new('RGB', (width * 2, height * 3))
        paste_height = 0
        for url in self.chunks[:3]:
            im = Image.open(BytesIO(urlopen(url).read()))
            new_image.paste(im, (0, paste_height))
            paste_height += height
        paste_height = 0
        for url in self.chunks[3:]:
            im = Image.open(BytesIO(urlopen(url).read()))
            new_image.paste(im, (width, paste_height))
            paste_height += height
        self.newspaper_image = new_image

    def _get_clips(self, class_name):
        base_url = 'https://epaper.dinakaran.com/3333692/Pollachi-Coimbatore-Supplement/28-12-2021'
        clips = []
        for div in self.soup.find_all('div', class_=class_name):
            clips.append(div)
            self.clip_urls.append(base_url + div.get('data-cliphref'))
        return clips

    def _get_chunks(self):
        for chunk_number in range(6):
            chunk = self.soup.find(id=f'left-chunk-{chunk_number}')
            self.chunks.append(chunk.find_all('img')[0].get('src'))

    def _getLastNewsPaperPage(self, url):
        driver = webdriver.Chrome(
            executable_path=r"C:\\chromedriver.exe", options=self.options)
        driver.get(url)
        driver.execute_script('scrollTo(0, document.body.scrollHeight);')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        firstDiv = soup.find_all(
            'div', class_='col-12 sm-col-6 md-col-3 card-box')[0]
        redirect_url = firstDiv.find_all('a')[0].get('href')
        id = redirect_url.split('/')[-1]
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        self.url = f'https://epaper.dinakaran.com/{id}/Pollachi-Coimbatore-Supplement/{current_date}#page/2/2'
        # this url has shutdown text
        # self.url = f'https://epaper.dinakaran.com/3333692/Pollachi-Coimbatore-Supplement/28-12-2021#page/2/2'

    def _create_images(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\\chromedriver.exe", options=self.options)
        self.driver.get(self.url)
        # scroll to the bottom of the page
        self.driver.execute_script(
            'scrollTo(0, document.body.scrollHeight/2);')
        time.sleep(2)
        self.driver.execute_script(
            'scrollTo(document.body.scrollHeight/2, document.body.scrollHeight);')
        time.sleep(3)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def get_newspaper_image(self):
        return self.newspaper_image


# def main():
#     scraper = ImageScraper()
#     print(scraper.images)


# if __name__ == '__main__':
#     main()
