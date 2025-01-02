# settings.py

BOT_NAME = 'scrapy_crawl_data'

SPIDER_MODULES = ['scrapy_crawl_data.spiders']
NEWSPIDER_MODULE = 'scrapy_crawl_data.spiders'

# Respect robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines (if needed)
ITEM_PIPELINES = {
    # 'scrapy_crawl_data.pipelines.YourPipeline': 300,
}

#Unicode
FEED_EXPORT_ENCODING = 'utf-8'

# Crawl tối đa 3 cấp liên kết
DEPTH_LIMIT = 3

#Loại bỏ trùng lặp URL
DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'
