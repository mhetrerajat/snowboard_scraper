import scrapy


class CountrySpider(scrapy.Spider):
    name = "countries"
    start_urls = ["https://www.lobstersnowboards.com/shop/"]

    def parse(self, response):
        for item in response.css('#country_list option'):
            country_code = item.css('option::attr(value)').extract_first()
            if isinstance(country_code, str):
                country_code = int(country_code)
            yield {
                'name': item.css('option::text').extract_first(),
                'code': country_code
            }
