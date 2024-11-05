import unittest

# Zakładam, że powyższy kod został zapisany w pliku o nazwie `product_module.py`
# i importuję potrzebne klasy oraz funkcje.
from src import (
    Product,
    ListServer,
    MapServer,
    TooManyProductsFoundError,
    sort_list,
    valid_founder_list,
    find_product
)


class TestProduct(unittest.TestCase):
    def test_init_valid(self):
        """Test poprawnej inicjalizacji obiektu Product."""
        product = Product("AB12", 29.99)
        self.assertEqual(product.name, "AB12")
        self.assertEqual(product.price, 29.99)

    def test_init_invalid(self):
        """Test inicjalizacji obiektu Product z nieprawidłowymi typami danych."""
        with self.assertRaises(ValueError):
            Product(123, "29.99")

    def test_eq_same(self):
        """Test porównania dwóch identycznych produktów."""
        product1 = Product("AB12", 29.99)
        product2 = Product("AB12", 29.99)
        self.assertEqual(product1, product2)

    def test_eq_different(self):
        """Test porównania dwóch różnych produktów."""
        product1 = Product("AB12", 29.99)
        product2 = Product("AB12", 39.99)
        self.assertNotEqual(product1, product2)

    def test_hash(self):
        """Test poprawności metody __hash__."""
        product1 = Product("AB12", 29.99)
        product2 = Product("AB12", 29.99)
        self.assertEqual(hash(product1), hash(product2))


class TestListServer(unittest.TestCase):
    def setUp(self):
        """Przygotowanie listy produktów do testów."""
        self.products = [
            Product("AB12", 29.99),
            Product("x0129", 19.99),
            Product("ab123", 39.99),
            Product("CD34", 24.99)
        ]
        self.server = ListServer(self.products)

    def test_init_valid(self):
        """Test poprawnej inicjalizacji ListServer."""
        self.assertEqual(self.server.list_obj, self.products)

    def test_init_invalid(self):
        """Test inicjalizacji ListServer z nieprawidłowym typem danych."""
        with self.assertRaises(ValueError):
            ListServer("NieLista")

    def test_search_in_catalog_valid(self):
        """Test wyszukiwania produktów z prawidłową liczbą liter."""
        result = self.server.get_entries(2)
        expected = [self.products[0], self.products[2], self.products[3]]
        self.assertEqual(result, expected)

    def test_search_in_catalog_invalid_n_letters(self):
        """Test wyszukiwania produktów z nieprawidłową liczbą liter."""
        with self.assertRaises(ValueError):
            self.server.get_entries(-1)


class TestMapServer(unittest.TestCase):
    def setUp(self):
        """Przygotowanie listy produktów do testów."""
        self.products = [
            Product("AB12", 29.99),
            Product("x0129", 19.99),
            Product("ab123", 39.99),
            Product("CD34", 24.99)
        ]
        self.server = MapServer(self.products)

    def test_init_valid(self):
        """Test poprawnej inicjalizacji MapServer."""
        expected_dict = {product.name: product for product in self.products}
        self.assertEqual(self.server.dict_obj, expected_dict)

    def test_init_invalid(self):
        """Test inicjalizacji MapServer z nieprawidłowym typem danych."""
        with self.assertRaises(ValueError):
            MapServer("NieLista")

    def test_search_in_catalog_valid(self):
        """Test wyszukiwania produktów z prawidłową liczbą liter."""
        result = self.server.get_entries(2)
        expected = [self.products[0], self.products[1], self.products[3]]
        self.assertEqual(result, expected)

    def test_search_in_catalog_invalid_n_letters(self):
        """Test wyszukiwania produktów z nieprawidłową liczbą liter."""
        with self.assertRaises(ValueError):
            self.server.get_entries(0)


class TestUtilityFunctions(unittest.TestCase):
    def setUp(self):
        """Przygotowanie listy produktów do testów."""
        self.products = [
            Product("AB12", 29.99),
            Product("x0129", 19.99),
            Product("ab123", 39.99),
            Product("CD34", 24.99)
        ]

    def test_sort_list(self):
        """Test funkcji sort_list."""
        sort_list(self.products)
        sorted_prices = [19.99, 24.99, 29.99, 39.99]
        self.assertEqual([p.price for p in self.products], sorted_prices)

    def test_valid_founder_list_empty(self):
        """Test funkcji valid_founder_list z pustą listą."""
        result = valid_founder_list([])
        self.assertEqual(result, [])

    def test_valid_founder_list_too_few(self):
        """Test funkcji valid_founder_list z za małą liczbą produktów."""
        small_list = [self.products[0]]
        result = valid_founder_list(small_list)
        self.assertEqual(result, [])

    def test_valid_founder_list_too_many(self):
        """Test funkcji valid_founder_list z za dużą liczbą produktów."""
        large_list = self.products * 3  # 12 produktów
        with self.assertRaises(TooManyProductsFoundError):
            valid_founder_list(large_list)

    def test_valid_founder_list_valid(self):
        """Test funkcji valid_founder_list z prawidłową liczbą produktów."""
        result = valid_founder_list(self.products)
        expected_sorted = sorted(self.products, key=lambda p: p.price)
        self.assertEqual(result, expected_sorted)

    def test_find_product_valid(self):
        """Test funkcji find_product z prawidłowymi danymi."""
        result = find_product(self.products, 2)
        expected = [self.products[0], self.products[1], self.products[3]]
        self.assertEqual(result, expected)

    def test_find_product_invalid_n_letters(self):
        """Test funkcji find_product z nieprawidłową liczbą liter."""
        with self.assertRaises(ValueError):
            find_product(self.products, -2)

    def test_find_product_no_matches(self):
        """Test funkcji find_product gdy brak dopasowań."""
        result = find_product(self.products, 5)
        self.assertEqual(result, [])


class TestTooManyProductsFoundError(unittest.TestCase):
    def test_default_message(self):
        """Test domyślnej wiadomości wyjątku."""
        try:
            raise TooManyProductsFoundError()
        except TooManyProductsFoundError as e:
            self.assertEqual(str(e), "Znaleziono za dużo produktów")

    def test_custom_message(self):
        """Test wyjątku z niestandardową wiadomością."""
        custom_msg = "Przekroczono limit produktów"
        try:
            raise TooManyProductsFoundError(custom_msg)
        except TooManyProductsFoundError as e:
            self.assertEqual(str(e), custom_msg)


if __name__ == '__main__':
    unittest.main()
