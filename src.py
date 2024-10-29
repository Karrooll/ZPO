#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional


class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)

    def __init__(self, name, price):
        self.name = name
        self.price = price
        # tutaj trzeba zadeklarować atrybty i dać odpowiednią walidacje

    def __eq__(self, other):
        # metoda powinna porównywać 2 produkty(obiekty)
        return None  # FIXME: zwróć odpowiednią wartość

    def __hash__(self):
        # to trzeba zmienić tak by działało
        return hash((self.name, self.price))


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