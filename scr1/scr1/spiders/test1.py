import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    # name = 't1'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://alexa.com/topsites/']

    def parse(self, response):
        pass
        # print(response.body) # html
        # print(response.status) # 200
        # response.css('selector').get() or response().css('selector').getall()
        # print(response.css('div.listings.table div.td.DescriptionCell > p > a::text').get())
        # print(response.css('div.listings.table div.td.DescriptionCell > p > a::text').getall())
        # for sitename in response.css('div.listings.table div.td.DescriptionCell > p > a::text').getall():
        #     yield {
        #         'sitename':sitename
        #     }

        # print(response.css('div.listings.table > div:nth-child(2)').extract_first())
        # tr = response.css('div.listings.table > div:nth-child(2)').extract_first()
        # print(response.css('div.listings.table > div:nth-child(2) .td').extract_first())
        # print(response.css('div.listings.table > div:nth-child(2) > .td').extract())
        # for div in response.css('div.listings.table > div:nth-child(2)').extract():
        # print(response.css('div.listings.table > div').getall())
        # for tr in response.css('.site-listing .td::text').getall():
        #     print(tr)
        #     print(tr.css('.td').get())
        # print(response.css('.site-listing .td').getall())
        # tr = response.css('div.listings.table > div:nth-child(2)').get() # type(tr) str
        #
        # tr = response.css('div.listings.table > div:nth-child(2)')
        # print('순위', tr.css('.td::text').get())
        # print('사이트명', tr.css('.td a::text').get())
        # # print('r', tr.css('.td.right > p::text').getall())
        # print('r1', tr.css('.td.right > p::text').getall()[0])
        # print('r2', tr.css('.td.right > p::text').getall()[1])
        # print('r3', tr.css('.td.right > p::text').getall()[2])
        # print('r4', tr.css('.td.right > p::text').getall()[3])

        # 첫번째 줄 div.td 출력
        # for td in response.css('div.listings.table > div:nth-child(2) > .td'):
        #     print(td, '!!!')

        # 해당페이지 크롤링 해서 이름.csv 파일로 제출
        for tr in response.css('div.listings.table > div.tr.site-listing'):
            rank = tr.css('.td::text').get()
            name = tr.css('.td a::text').get()
            r1 = tr.css('.td.right > p::text').getall()[0]
            r2 = tr.css('.td.right > p::text').getall()[1]
            r3 = tr.css('.td.right > p::text').getall()[2]
            r4 = tr.css('.td.right > p::text').getall()[3]
            yield {
                'rank': rank,
                'sitename': name,
                'r1': r1,
                'r2': r2,
                'r3': r3,
                'r4': r4
            }