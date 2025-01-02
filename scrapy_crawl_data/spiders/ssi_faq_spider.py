import scrapy
from scrapy_crawl_data.items import FAQItem

class CafeFSpider(scrapy.Spider):
    name = 'cafef'
    allowed_domains = ['cafef.vn']
    start_urls = ['https://cafef.vn/']

    def __init__(self, results=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.results = results if results is not None else []

    def parse(self, response):
        # Tìm tất cả các bài viết trong phần chính
        articles = response.css("div.top_noibat_row1, div.top_noibat_row2 div.big")

        for article in articles:
            # Lấy tiêu đề (title)
            title = article.css("h2 a::attr(title)").get()
            # Lấy đường dẫn URL
            url = article.css("h2 a::attr(href)").get()
            if url and not url.startswith("http"):
                url = response.urljoin(url)  # Chuyển đổi URL tương đối thành tuyệt đối

            if title and url:
                # Lưu kết quả vào item
                faq_item = FAQItem()
                faq_item['title'] = title
                faq_item['url'] = url

                # Thêm vào danh sách kết quả
                self.results.append({'title': title, 'url': url})
                yield faq_item
