#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional


class Product:
    """Klasa reprezentująca produkt: <ciąg_liter><ciąg_cyfr> : cena
            np.  x0129, AB12, ab123"""
    def __init__(self, name: str, price: float):
        """Metoda inicjalizująca"""

        # Sprawdzenie, czy podane dane do metody init są odpowiedniego typu
        if isinstance(name, str) and isinstance(price, float):
            self.name = name
            self.price = price

        else:
            # W przeciwnym wypadku wyrzuca ValueError
            raise ValueError("Nawa musi być typu 'str', a cena 'float'")

    def __eq__(self, other):
        """Metoa __eq__ porównuje dwie instancje klasy. W tym przypadku sprawdza czy mają taką samą nazwę i cenę."""

        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price

        #Jeśli się różnią lub other nie jest instancją Product to zwraca False
        return False

    def __hash__(self):
        """Gdy nadpisuje się __eq__ to dobrą praktyką jest nadpisanie __hash__.

        Ta tworzy hash - ciąg liczb, który używany jest, gdy obiekt jest w set(), albo jest kluczem słownika
        Poniższa definicja bierze hashe z atrybutów i wykonuje na nich bitowego XOR, generując unikalny hash dla
        kombinacji title i pages. Wyprintujcie se z ciekawości hash(instacja_Product).
        """
        return hash(self.name) ^ hash(self.price)

#PYTANIE1 Co jak produkty mają takie same nazwy ale różne ceny? - Chyba kompetencje serwera



class TooManyProductsFoundError:
    # jak w instrukcji jest napisane że ma być rzucony włansy wyjątek to właśnie o ten chodzi
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania

class ListServer:
    def __init__(self, lista_obj):
        self.lista_obj = lista_obj
        # metoda który zaninicjalizuje serwer listowy

    def add_product(self, product):
        self.lista_obj.append(product) # to co tutaj wchodzi jako produkt to obiekt który chcemy dodać do serwera; listy
    pass


class MapServer:
    def __init__(self, dic_obj):
        self.dic_obj = dic_obj
    def add_product(self, product):
        self.dic_obj[product.name] = product # to co tu wchodzi jako produkt to obiekt który chcemy dodać do serwera; słowinka
        # metoda inicjalizująca serwer słownikowy
    pass


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, serwer):
        self.serwer = serwer
        # przy inicjalizacji podajemy serwer w którym szukamy produktów




    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        # pobiera nazwy obiektów, wyszukuje w serwerze, zbiera cene
        raise NotImplementedError()