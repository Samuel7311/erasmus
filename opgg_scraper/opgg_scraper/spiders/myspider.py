import scrapy
import json

class OPGGSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.op.gg/summoners/euw/Caps-45555']

    custom_settings = {
        'FEEDS': {
            'op_gg.json': {
                'format': 'json',
                'overwrite': True,  # If the file already exists, it will overwrite it
            },
        },

    }

    def parse(self, response):
        # Find all table rows
        table_rows = response.xpath('//tr[@class="overview-player"]')

        # Create an empty list to store data
        data = []

        # Iterate over each table row
        for row in table_rows:
            # Create a dictionary to store row data
            row_data = {}

            # Extract data from each cell and add it to the dictionary
            row_data['champion'] = row.xpath('td[@class="champion"]/text()').get().strip()
            row_data['spells'] = row.xpath('td[@class="spells"]/text()').get().strip()
            row_data['runes'] = row.xpath('td[@class="runes"]/text()').get().strip()
            row_data['name'] = row.xpath('td[@class="name"]/text()').get().strip()
            row_data['op-score-wrapper'] = row.xpath('td[@class="op-score-wrapper"]/text()').get().strip()
            row_data['kda'] = row.xpath('td[@class="kda"]/text()').get().strip()
            row_data['damage'] = row.xpath('td[@class="damage"]/text()').get().strip()
            row_data['ward'] = row.xpath('td[@class="ward"]/text()').get().strip()
            row_data['cs'] = row.xpath('td[@class="cs"]/text()').get().strip()

            # Append the row data to the list
            data.append(row_data)

        # Write JSON data to the file
        with open('op_gg.json', 'w') as f:
            json.dump(data, f, indent=4)

