import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.naver.com/movie/running/current.nhn']
    start_urls = ['https://movie.naver.com/movie/running/current.nhn']

    def parse(self, response):
        list = response.css('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

        for li in list:
            title = li.css('dl > dt > a::text').get()
            rating = li.css('dl > dd.star > dl.info_star > dd > div > a > span.num::text').get()
            book = li.css('dl > dd.star > dl.info_exp > dd > div > span.num::text').get()

            if book == None:
                book = 0

            print(title, rating, book)
            yield {
                'title': title,
                'rating': rating,
                'book': book
            }
