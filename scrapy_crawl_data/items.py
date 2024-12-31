import scrapy

class FAQItem(scrapy.Item):
    question = scrapy.Field()
    answer = scrapy.Field()
