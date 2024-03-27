import scrapy

class HotlineVacumSpider(scrapy.Spider):
    name = 'hotline_vacum'
    start_urls = ['https://hotline.ua/ua/bt/pylesosy/']

    def parse(self, response):
        for product in response.xpath('//div[@class="catalog container"]//div[@class="list-item"]'):
            title = product.xpath('.//a[@class="item-title"]/text()').get().strip()
            link = response.urljoin(product.xpath('.//a[@class="item-title"]/@href').get())
            image = response.urljoin(product.xpath('.//div[@class="list-item__photo"]//img/@src').get())
            price = product.xpath('.//div[@class="list-item__value-price"]/text()').get().strip()
            offers = product.xpath('.//a/text()').re_first(r'(\d+) пропозицій?')

            yield scrapy.Request(url=link, callback=self.parse_product_details, meta={'title': title, 'link': link, 'image': image, 'price': price, 'offers': offers})

    def parse_product_details(self, response):
        title = response.meta['title']
        link = response.meta['link']
        image = response.meta['image']
        price = response.meta['price']

        shop_name = response.xpath('//a[@class="shop__title"]/text()').get().strip()

        yield {
            'title': title,
            'link': link,
            'image': image,
            'price': price,
            'offers': offers,
            'shop_name': shop_name
        }
