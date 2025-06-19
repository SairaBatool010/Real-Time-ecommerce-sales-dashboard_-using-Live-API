import requests
import json


print("hello")

def fetch_products():
    URL="https://fakestoreapi.com/products"
    response= requests.get(URL)
    if response.status_code==200:
        product=response.json() # covert json fetched data to python list dictionaries
        print(f"fetched {len(product)} products.")
        return product
    else:
        print("failed to fetched the data")
        return[]

if __name__== "__main__":
    products=fetch_products()
    titles=[product['title'] for product in products]
    print(json.dumps(list(set(titles)), indent=2))  #covert back to json format