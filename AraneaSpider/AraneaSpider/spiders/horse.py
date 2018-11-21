import scrapy

class HorseSpider(scrapy.Spider):
    name = 'ike'

    def start_requests(self):
        # Defines the initial request and how to follow links
        urls = ['https://treehouse-projects.github.io/horseland/index.html','https://treehouse-projects.github.io/horseland/mustang.html']

        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self,response):
        url = response.url
        page = url.split('/')[-1]
        filename = 'horses-%s' % page
        print('URL is: {}'.format(url))
        with open(filename, 'wb') as file: 
            file.write(response.body)
        print('Saved file name %s' % filename)