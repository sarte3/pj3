import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikibook.co.kr/list']
    start_urls = ['https://wikibook.co.kr/list/']

    def parse(self, response):
        # print(response.status)
        # print(response.css('div.col-md-11.book-list-detail > a > h4').get())
        # print(response.css('div.col-md-11.book-list-detail > a').get())
        # print(response.css('div.col-md-11.book-list-detail > a::attr(href)').get())
        # print(response.css('div.col-md-11.book-list-detail > a > h4::text').get())
        yield {
            'title' : response.css('div.col-md-11.book-list-detail > a > h4::text').get(),
            'bookurl' : response.css('div.col-md-11.book-list-detail > a::attr(href)').get()
        }
# scrapy crawl wiki --nolog -o wiki.json
# scrapy crawl wiki --nolog -o wiki.csv
