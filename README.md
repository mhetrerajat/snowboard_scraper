# Deal.com Test
This project involves two scrapers which collects data from https://www.lobstersnowboards.com/shop/
1. **CountrySpider** : Scrapes country name and code where given website sales snowboards
2. **SnowboardSpider** : Scrapes product details of snowboards like its name, image, price, available sizes etc.


### Installation
Install *pipenv* and then install all project dependencies with following command
```
pipenv install
```


### Usage
Go to project directory
```
cd assignment
```

This will run CountrySpider and collect all countries' name and codes.
```
scrapy crawl countries -o countries.json
```
To run SnowboardSpider, run following command

NOTE: This requires countries.json file to run
```
scrapy crawl snowboards -t csv -o snowboards.csv
```

### Information
1. SnowboardSpider requires **countries.json** as it contains country name and code. Given website stores country code in cookies as *site_country_id*, to show country specific snowboards to its users.
2. This scraper makes requests to all countries given in website and collects snowboards details.
3. On product detail page, they give link to another/similar product in select option if given product is out of stock. This scraper also follows these links to collect product information.
4. Entire project is build with *Python* based web scarping framework *scrapy*.
