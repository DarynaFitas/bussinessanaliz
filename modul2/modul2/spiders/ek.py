import csv
import scrapy
from SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class EkSpider(scrapy.Spider):
    name = "ek"
    start_urls = ["https://ek.ua/ua/list/122/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, '.model-short-block')),
            )

    def parse(self, response):
        items = []

        phones = response.css('.model-short-block')
        for phone in phones:
            model = phone.css('.model-short-title::text').get()
            image_url = phone.css('.model-short-img img::attr(src)').get()
            shop = phone.css('.model-shop::text').get()
            city = phone.css('.model-city::text').get()
            price = phone.css('.model-short-price span::text').get()

            items.append({
                'Модель': model,
                'URL зображення': image_url,
                'Магазин': shop,
                'Місто продажу': city,
                'Ціна': price,
            })

        self.write_to_csv(items)

    def write_to_csv(self, items):
        filename = 'ek_smartphones.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Модель', 'URL зображення', 'Магазин', 'Місто продажу', 'Ціна'])
            writer.writeheader()
            writer.writerows(items)
        self.log("Saved file %s" % filename)
