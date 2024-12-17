import requests

BASE_URL = "http://127.0.0.1:5000"

def post_product():
    new_product = {
        "name": "sugar",
        "description": "A test product description.",
        "price": 10,
        "stock": 9
    }

    response = requests.post(f"{BASE_URL}/postproduct", json=new_product)
    if response.status_code == 201:
        print("POST /products test passed.",response.json())
    else:
        print("Failed to create product.")



def get_products():
    response = requests.get(f"{BASE_URL}/getproducts")
    if response.status_code == 200:
        product_list = response.json()
        print("Available Products:")
        for product in product_list:
            print(f"ID: {product['id']}, Name: {product['name']}, Description: {product['description']}, Price: {product['price']}, Stock: {product['stock']}")
        print("GET /products test passed.")
    else:
        print("Failed to retrieve products:", response.json() if response.status_code != 500 else "Internal Server Error.")


def place_order():
    order_data = {
        "products": [
            {"id": 165, "quantity": 1},  # Assuming product ID 1 exists and has enough stock
            {"id": 136, "quantity": 1}   # Assuming product ID 2 exists and has enough stock
        ]
    }
    response = requests.post(f"{BASE_URL}/postorder", json=order_data)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 201:
        order_info = response.json()
        print("Order created successfully:",order_info)
    else:
        print(response , response.status_code , response.json())
        print("Failed to create order:", response.json() if response.status_code != 500 else "Internal Server Error.")



def get_products():
    response = requests.get(f"{BASE_URL}/getproducts")
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        product_list = response.json()
        print("Available Products:")
        for product in product_list:
            print(f"ID: {product['id']}, Name: {product['name']}, Description: {product['description']}, Price: {product['price']}, Stock: {product['stock']}")
        print("GET /products test passed.")
    else:
        print("Failed to retrieve products:", response.json() if response.status_code != 500 else "Internal Server Error.")


# Call the function
# post_product()
# get_products()
place_order()




