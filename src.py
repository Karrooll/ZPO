#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABCMeta
from curses.ascii import isalpha
from itertools import product
from re import search
from typing import Optional, List, Dict
from abc import ABC, abstractmethod


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



class TooManyProductsFoundError(Exception):
    def __init__(self, msg:str = None) -> None:
        if msg is None:
            msg = "Znaleziono za dużo produktów"
        super().__init__(msg) # wywołaj konstruktor klasy macierzystej z msg

    # jak w instrukcji jest napisane że ma być rzucony włansy wyjątek to właśnie o ten chodzi
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.



# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania

def sort_list(list_to_sort: List[Product]): # funkcja która sortuje liste produktów
    change = 0
    out = True
    j = 1

    while out:
        change_2 = change
        for i in range(0, len(list_to_sort) - j):
            change += 1
            if list_to_sort[i].price > list_to_sort[i + 1].price:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
        j += 1
        if (change - change_2) == 0:
            out = False


def valid_founder_list(list_to_validate: List[Product]): # funkcja która odrzuca niepoprawne listy produktów
    if not list_to_validate: # jeżeli lista jest pusta
        return list_to_validate

    elif Server.n_max_returned_entries[0] <= len(list_to_validate) <= Server.n_max_returned_entries[1]: # sprawdzanie czy lista produktów jest odpowiedniej długości
        sort_list(list_to_validate) # sortowanie listy rosnąco cenami
        return list_to_validate

    raise TooManyProductsFoundError("Znaleziono nie odpowiednią liczbę produktów") # w każdym innym przypadku wywołaj wyjątek

def find_product(list_to_find: List[Product], n_letters: int) -> List[Product]: # funkcja znajdująca produkty

    if isinstance(n_letters, int) == False or n_letters <= 0:
        raise ValueError("Podano złą liczbę liter do wyszukania")

    found_product = []
    for product_ in list_to_find:
        counter_of_letter = sum(1 for sign in product_.name if sign.isalpha())  # sprawdzenie ile liter ma nazwa produktu
        counter_of_number = sum(1 for sign in product_.name if sign.isdigit())  # sprawdzenie ile cyfr ma nazwa produktu
        if counter_of_letter == n_letters and (counter_of_number == 2 or counter_of_number == 3):
            found_product.append(product_)

    return valid_founder_list(found_product)


class Server(ABC):
    n_max_returned_entries = [3, 7]  # atrybut klasowy

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abstractmethod
    def search_in_catalog(self, n_letters):
        pass


class ListServer(Server):
    def __init__(self, list_obj: list[Product], *args, **kwargs): # metoda który zaninicjalizuje serwer listowy
        super().__init__(*args, **kwargs)

        if isinstance(list_obj, list) or list_obj is not None or list_obj != []:
            self.list_obj = list_obj
        else:
            raise ValueError("Przekazano nieodpowiedni parametr do inicjalizacji obiektu MapServer")

    def search_in_catalog(self, n_letters):
        return find_product(self.list_obj, n_letters)


class MapServer(Server):

    def __init__(self, list_obj: list[Product], *args, **kwargs): # metoda inicjalizująca serwer słownikowy
        super().__init__(*args, **kwargs)

        if isinstance(list_obj, list) or list_obj is not None or list_obj != []:
            self.dict_obj = {product_.name: product_ for product_ in list_obj} # dict comprehension
        else:
            raise ValueError("Przekazano nieodpowiedni parametr do inicjalizacji obiektu MapServer")

    def search_in_catalog(self, n_letters):
        return find_product(list(self.dict_obj.values()), n_letters)  # Tworzenie listy produktów na podstawie słownika



class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, serwer):
        self.serwer = serwer
        # przy inicjalizacji podajemy serwer w którym szukamy produktów

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        # pobiera nazwy obiektów, wyszukuje w serwerze, zbiera cene
        raise NotImplementedError()