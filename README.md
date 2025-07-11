# McDonald's Menu Scraper & API

### Description :
Uses Scrapy to collect links and titles to all menu products and save it to menu.json.

Uses Selenium to parse detailed information from each product page (description, calories, proteins, fats, carbohydrates, etc.).

Saves the scraped data to nutrients_data.json.

Serves the data via FastAPI with the following endpoints:

    * GET  /all_products/ ---- Returns a list of all products

    * GET  /products/{product_name} --- Returns full information about specific product

    * GET  /products/{product_name}/{product_field} --- Returns specific field of a product

### How to Run:

```
git clone https://github.com/mwellick/scrape_mcdonalds_menu.git
cd crape_mcdonalds_menu

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For MacOS/Linux
python3 -m venv venv
source venv/bin/activate

# Then proceed with the following:
pip install -r requirements.txt

#Collect all menu from menu page:
scrapy crawl menu -o menu.json


#Collect all data about each product:
python selenium_scrapy.py

#Run FastAPI server
uvicorn endpoints:app --reload

```

### API Documentation
* Swagger: Visit http://127.0.0.1:8000 

