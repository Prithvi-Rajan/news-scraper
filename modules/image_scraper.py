# given an url to a website, returns a list of all the image urls in the webpage
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import requests
import OCR
# import re


class ImageScraper:
    def __init__(self, url):
        self.clip_urls = []
        self.options = Options()
        self.options.headless = True
        self.getLastNewsPaperPage(url)
        self.driver = webdriver.Chrome(
            executable_path=r"C:\\chromedriver.exe", options=self.options)
        self.driver.get(self.url)
        self.soup = self._get_soup()
        self.clips = self.get_clips('clip-box clippageview')
        self._get_images()
        # self.driver.quit()

    def _get_soup(self):
        # r = requests.get(self.url)
        return BeautifulSoup(self.driver.page_source, 'html.parser')

    def _get_images(self):
        self.images = []
        for clip_url in self.clip_urls:
            driver = webdriver.Chrome(
                executable_path=r"C:\\chromedriver.exe", options=self.options)
            driver.get(clip_url)
            # req = requests.get(clip_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            self.images.append(soup.find_all(
                'img', class_='clip-enlarged clip-enlarged-image')[1].get('src'))
            driver.quit()
        return self.images

    def get_clips(self, class_name):
        base_url = 'https://epaper.dinakaran.com/3333692/Pollachi-Coimbatore-Supplement/28-12-2021'
        clips = []
        for div in self.soup.find_all('div', class_=class_name):
            clips.append(div)
            self.clip_urls.append(base_url + div.get('data-cliphref'))
        return clips

    def getLastNewsPaperPage(self, url):
        driver = webdriver.Chrome(
            executable_path=r"C:\\chromedriver.exe", options=self.options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        firstDiv = soup.find_all(
            'div', class_='col-12 sm-col-6 md-col-3 card-box')[0]
        self.url = firstDiv.find_all('a')[0].get('href')


def main():
    url = 'https://epaper.dinakaran.com/t/22485'
    scraper = ImageScraper(url)
    print(scraper.images)


if __name__ == '__main__':
    main()
