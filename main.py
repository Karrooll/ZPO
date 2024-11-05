from src import (
    Product,
    ListServer,
    MapServer,
    TooManyProductsFoundError,
    sort_list,
    valid_founder_list,
    find_product, Client
)
products = [
            Product("AB12", 29.99),
            Product("x0129", 19.99),
            Product("ab123", 39.99),
            Product("CD34", 24.99)
        ]

serv_list = ListServer(products)
s = 'A'
clinet = Client(serv_list)
print(s.lower())
print(clinet.get_total_price(2))
