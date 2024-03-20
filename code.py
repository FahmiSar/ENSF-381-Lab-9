import json
import requests



def fetch_product_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Return directly the list of products
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def list_all_products(products):
    for product in products:
        print(product)
        
            
def search_product(products, name):
    found = False  # Initialize found flag
    for product in products:
        # Check if the product dictionary has the 'name' key
        if 'name' in product:
            # Check if the provided name matches any product name
            if name.lower() in product['name'].lower():  # Convert both to lowercase for case-insensitive comparison
                found = True
                # Print product details
                print(json.dumps(product, indent=4))
                break  # Exit loop once a match is found
    if not found:
        print("Product not found.")

def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n> ")
            if choice == '1':
                list_all_products(products)
            elif choice == '2':
                product_name = input("Enter the product name: ")
                search_product(products, product_name)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Failed to fetch product data.")

if __name__ == "__main__":
     main()
