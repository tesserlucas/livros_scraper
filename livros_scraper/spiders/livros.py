import scrapy

class LivrosSpider(scrapy.Spider):
    name = "livros"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/catalogue/category/books_1/index.html"]

    def parse(self, response):
        # Extrair informações dos livros na página atual
        for livro in response.css('article.product_pod'):
            yield {
                'titulo': livro.css('h3 a::attr(title)').get(),
                'preco': livro.css('div.product_price p.price_color::text').get(),
                'imagem_url': response.urljoin(livro.css('div.image_container img::attr(src)').get()),
                'detalhes_url': response.urljoin(livro.css('h3 a::attr(href)').get()),
            }
  
        # Seguir para a próxima página de categorias, se existir
        proxima_pagina = response.css('ul.pager li.next a::attr(href)').get()
        if proxima_pagina:
            yield response.follow(proxima_pagina, callback=self.parse)
