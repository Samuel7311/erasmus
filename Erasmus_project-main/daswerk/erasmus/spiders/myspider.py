import scrapy
import re

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.daswerk.org/']

    custom_settings = {
        'FEEDS': {
            'oDaswerk.json': {
                'format': 'json',
                'overwrite': True,  # If the file already exists, it will overwrite it
            },
        },
    }

    def parse(self, response):
        # Scraping the main page
        self.logger.info(f"Scraping main page: {response}")

        # Extracting links to individual party pages
        links = response.css('a.preview-item--link::attr(href)').getall()

        # Following each link to the party page
        for link in links:
            yield response.follow(link, callback=self.parse_event)

    def parse_event(self, response):
        # Extracting the title from the party page
        title = response.css('p.main--header-title::text').get()
        date = response.css('li::text').get()

        # Process date format
        day, month = self.extract_day_and_month(date)

        yield {
            'Link': response.url,
            'Title': title,
            'Day': day,
            'Month': month,
        }

    def extract_day_and_month(self, date_str):
        # Regular expression to match the date format
        date_pattern = re.compile(r'(\d{1,2})\.?\s*([A-Za-zäöüß]{3})')

        # Search for the day and the first three letters of the month in the string
        match = date_pattern.search(date_str)
        if match:
            day = match.group(1)
            month = match.group(2)
            return day, month
        else:
            return None, None
