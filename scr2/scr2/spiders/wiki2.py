import scrapy


# class Wiki2Spider(scrapy.Spider):
#     name = 'wiki2'
#     allowed_domains = ['wikibook.co.kr/list']
#     start_urls = ['https://wikibook.co.kr/list/']
#
#     def parse(self, response):
#         # print(response.status)
#         booklist = response.css('.book-url')
#         for a in booklist[:3]:
#             href = a.css('::attr(href)').get()
#             title = a.css('h4::text').get()
#             print(href, title)
#             yield {
#                 'url': href,
#                 'title': title
#             }
#         # scrapy crawl wiki2 --nolog -o wiki.json
#

class Wiki2Spider(scrapy.Spider):
    name = 'wiki2'
    allowed_domains = ['wikibook.co.kr']
    start_urls = ['https://wikibook.co.kr/list/']

    def parse(self, response):
        booklist = response.css('.book-url')
        for a in booklist[:3]:
            href = a.css('::attr(href)').get()
            print(href)
            # yield response.follow(url, 메서드)
            yield response.follow(href, self.bookDetail)
            

    def bookDetail(self, response):
        print('-'*30)