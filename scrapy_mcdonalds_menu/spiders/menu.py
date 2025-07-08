import scrapy
from scrapy.http import Response


class MenuSpider(scrapy.Spider):
    name = "menu"
    allowed_domains = ["www.mcdonalds.com"]
    start_urls = ["https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"]

    def parse(self, response: Response, **kwargs):
        for menu in response.css(".cmp-category__item"):
            title = menu.css(".cmp-category__item-name::text").get()
            url = response.urljoin(menu.css("a::attr(href)").get())
            yield {
                "title": title,
                "url": url
            }
