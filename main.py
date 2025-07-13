# price_comparator.py
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_amazon(product_name):
    # Simulated scraping logic (real scraping requires headers, proxies, etc.)
    return {"site": "Amazon", "price": "₹1,999", "url": "https://amazon.in/example"}

def scrape_flipkart(product_name):
    return {"site": "Flipkart", "price": "₹1,899", "url": "https://flipkart.com/example"}

@app.route('/compare', methods=['GET'])
def compare_prices():
    product = request.args.get('product')
    results = [
        scrape_amazon(product),
        scrape_flipkart(product)
    ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)




