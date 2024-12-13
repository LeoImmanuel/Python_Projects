import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # Get all the books details from the webpage 
        books = response.css('article.product_pod')

        # For each book get name, pice and url 
        for book in books:
            yield {
                    'name' : book.css('h3 a::text').get(),
                    'price' : book.css('.product_price .price_color::text').get(),
                    'url' : book.css('h3 a').attrib['href']
            }
        
        # Get next page URLs
        next_page = response.css('li.next a::attr(href)').get()

        # Validation for pagination
        if next_page is not None:
            # Check if URL contains 'catalogue'
            if next_page.startswith('catalogue'):
                # Concatenate url 
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                # Without 'catalogue' in the URL
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            
            yield response.follow(next_page_url, callback = self.parse)