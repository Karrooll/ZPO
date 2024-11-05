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
            Product("A12", 29.99),
            Product("xd129", 19.99),
            Product("a123", 39.99),
            Product("123", 39.99),
            Product("Ckh34", 24.99),
            Product("llk12", 29.99),
            Product("o12", 29.99),
            Product("w12", 29.99),
            Product("v12", 29.99),
            Product("x12", 29.99),

        ]

serv_list = ListServer(products)
s = 'A'
clinet = Client(serv_list)
print(s.lower())
lista = clinet.get_total_price()

print(lista)
