import time
import random
from datetime import datetime
from fetch_data import fetch_products
from db_utils import init_db, insert_sale

def simulate_sale(products):
    product=random.choice(products)
    quantity=random.randint(1,10)
    revenue=round(product['price']*quantity,2)
    return {
        "product_id": product['id'],
        "title": product['title'],
        "category": product['category'],
        "price": product['price'],
        "quantity": quantity,
        "revenue": revenue,
        'sale_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__=='__main__':
    init_db()
    products=fetch_products()
    while True:
        sale=simulate_sale(products)
        insert_sale(sale)
        time.sleep(10)



