import scrapy

class FacultyItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
