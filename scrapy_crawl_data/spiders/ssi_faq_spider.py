import scrapy
from scrapy_crawl_data.items import FAQItem

class SSIFAQSpider(scrapy.Spider):
    name = 'ssi_faq'
    allowed_domains = ['ssi.com.vn']
    start_urls = ['https://www.ssi.com.vn/khach-hang-ca-nhan/phai-sinh-faq']

    def parse(self, response):
        # Lấy danh sách các thẻ chứa FAQ
        faq_cards = response.css("div.card")

        for card in faq_cards:
            # Lấy câu hỏi
            question = card.css("button.btn-card::text").get()
            if question:
                question = question.strip()

            # Lấy câu trả lời
            answer = " ".join(card.css("div.card-body *::text").getall()).strip()

            # Lưu dữ liệu vào FAQItem
            faq_item = FAQItem()
            faq_item['question'] = question
            faq_item['answer'] = answer

            yield faq_item
