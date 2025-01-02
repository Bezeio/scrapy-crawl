from flask import Flask, jsonify, request
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer

app = Flask(__name__)

# CrawlerRunner để chạy Scrapy spider
runner = CrawlerRunner(get_project_settings())

# Lưu kết quả từ spider
results = []

# Hàm chạy spider
@defer.inlineCallbacks
def crawl(spider_name):
    global results
    results.clear()  # Xóa kết quả cũ trước khi chạy spider
    yield runner.crawl(spider_name, results=results)
    reactor.stop()  # Dừng reactor sau khi spider hoàn thành

@app.route('/run-spider', methods=['GET'])
def run_spider_endpoint():
    spider_name = request.args.get("spider_name", "cafef")  # Mặc định là spider 'cafef'

    try:
        # Chạy spider
        reactor.callWhenRunning(crawl, spider_name)
        reactor.run()  # Bắt đầu Scrapy
        return jsonify({"message": "Spider ran successfully", "data": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
