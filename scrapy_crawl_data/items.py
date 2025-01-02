import scrapy

class FAQItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
