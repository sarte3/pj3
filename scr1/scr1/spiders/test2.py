import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['movie.naver.com/movie/running/current.nhn']
    start_urls = ['https://movie.naver.com/movie/running/current.nhn']

    def parse(self, response):
        pass
