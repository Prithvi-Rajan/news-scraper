# import all the modules
import modules.OCR as OCR
import modules.image_scraper as image_scraper


def main():
    scraper = image_scraper.ImageScraper()
    ocr = OCR.OCR()
    if ocr.check_for_shutdown(scraper.get_newspaper_image()):
        print('found')
    else:
        print('not found')


if __name__ == '__main__':
    main()
