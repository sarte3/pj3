import scrapy


class Movie1Spider(scrapy.Spider):
    name = 'movie1'
    allowed_domains = ['movie.naver.com/movie/running/current.nhn']
    start_urls = ['https://movie.naver.com/movie/running/current.nhn']

    def parse(self, response):
        # print(response.status)
        mlist = response.css('dl.lst_dsc')
        for m in mlist:
            title = m.css('a::text').get()
            grade = m.css('span.num::text').get()
            rate = m.css('div.star_t1.b_star > span.num::text').get()
            print(title, grade, rate)
            title = title.replace(',', '')
            yield {
                'title': title,
                'grade': grade,
                'rate': rate
            }
        
