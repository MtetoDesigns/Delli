import scrapy


class DellispiderSpider(scrapy.Spider):
    name = "dellispider"
    allowed_domains = ["delli.market"]
    start_urls = ["https://delli.market/collections/condiments-sauces-marinades"]

    def parse(self, response):
        products = response.css('article.product-card')
        for product in products:
            yield {
                'name': product.css('a.product-card-title::text').get(),
                'price':product.css('span.price-item.price-item-regular::text').get(),
                'url': product.css('a.product-card-title::attr(href)').get()}
            
        next_page = response.css('a.pagination-button.arrow-button.next::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://delli.market' + next_page
            yield response.follow(next_page_url, callback=self.parse)
            
