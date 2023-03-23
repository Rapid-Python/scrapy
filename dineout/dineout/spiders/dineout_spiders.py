import scrapy
from scrapy.loader import ItemLoader


class DineOutSpiderSpider(scrapy.Spider):

    name = 'dineout_spider'
    page_number = 1
    allowed_domains = ['dineout.co.in']

    def __init__(self, state=None, *args, **kwargs):
        super(DineOutSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            f'https://www.dineout.co.in/{state.lower()}-restaurants'
        ]

    def restaurant_page_parser(self, response):
        for i in response.css('div.review-post'):
            yield {
                'Name': response.css('h1.restnt-name').css('a::text').get(),
                'Location': ",".join(response.css('div.restnt-loc').css('a::text').getall()),
                'Price': response.css('div.fs16.marginB5').css('strong::text').get(),
                'Cuisine Type': ",".join(response.css('div.cuisine-type').css('a::text').getall()),
                'Rating': response.css('div.rating.rating-4::text').get(),
                'Total votes': response.css('div.rating-txt').css('a::text').get(),
                'Total Review': response.css('div.rating-txt::text').get(),
                'Link': response.request.url,
                'User Name': i.css('div.name').css('h5::text').get(),
                'Post Date': i.css('span.date::text').get(),
                'Review': i.css('span.more::text').get()
            }

    def parse(self, response):

        base_url = 'https://www.dineout.co.in'

        for product in response.css('div.restnt-card.restaurant'):

            restaurant_link = f"{base_url}{product.css('a::attr(href)').get()}/review/?revpage=100"
            yield response.follow(restaurant_link, callback=self.restaurant_page_parser, headers=response.request.headers)

        self.page_number += 1
        next_page = f"{self.start_urls[0]}?p={self.page_number}"

        if not response.css('h2::text').get() or \
                response.css('h2::text').get().lower() != 'food not found':

            yield response.follow(next_page, callback=self.parse, headers=response.request.headers)


