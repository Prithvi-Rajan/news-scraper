# import all the modules
import modules.OCR as OCR
import modules.image_scraper as image_scraper


def main():
    url = 'https://epaper.dinakaran.com/3333692/Pollachi-Coimbatore-Supplement/29-12-2021#page/2/1'
    scraper = image_scraper.ImageScraper(url)
    ocr = OCR.OCR()
    ocr.check_for_shutdown(scraper.images)


if __name__ == '__main__':
    main()
