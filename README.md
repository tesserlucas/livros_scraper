# Books Scraper

Este é um projeto de um spider Scrapy que extrai dados de livros do site [books.toscrape.com](http://books.toscrape.com/). O objetivo é coletar informações sobre os 1000 livros disponíveis no site, seguindo algumas restrições específicas.

## Descrição do Projeto

O spider navega por todas as páginas de categorias e extrai os seguintes campos para cada livro:

- **Título do Livro (title)**
- **Preço do Livro (price)**
- **URL da Imagem do Livro (image_url)**
- **URL da Página de Detalhes do Livro (details_url)**

## Como Executar o Projeto

### 1. Instale as Dependências
Certifique-se de que o Python 3.6 ou superior está instalado e instale o Scrapy:

```bash
pip install scrapy
```

### 2. Clone o Repositório
Baixe o projeto para sua máquina local:

```bash
git clone https://github.com/seu-repositorio/livros-scraper.git
cd livros-scraper
```

### 3. Execute o Spider
Para iniciar o spider e salvar os dados em um arquivo JSON:

```bash
scrapy crawl livros -o livros.json
```

- **`-o livros.json`**: Especifica o nome do arquivo onde os dados serão salvos.

### 4. Resultado
O arquivo `livros.json` conterá as informações extraídas, como título, preço, URL da imagem e URL da página de detalhes dos livros.

## Estrutura do Projeto

```
livros_scraper/
│
├── livros_scraper/
│   ├── __init__.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── livros.py
│
└── scrapy.cfg
```
