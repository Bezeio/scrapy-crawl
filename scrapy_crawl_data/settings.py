# settings.py

BOT_NAME = 'scrapy_craw_data'

SPIDER_MODULES = ['scrapy_craw_data.spiders']
NEWSPIDER_MODULE = 'scrapy_craw_data.spiders'

# Respect robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines (if needed)
ITEM_PIPELINES = {
    # 'scrapy_craw_data.pipelines.YourPipeline': 300,
}

#Unicode
FEED_EXPORT_ENCODING = 'utf-8'