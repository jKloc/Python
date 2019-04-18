import re
import actors

def lista_korzysci():
    tablica = ["Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"]
    print (tablica)

def lista_skladana(lista):
    slowa = lista.split()
    return slowa

def zmienna_liczba_argumentow(*elementy):
    list = ""
    for argumenty in elementy:
        list += argumenty + " "
    return("podane argumenty: %s" % list)

def wypisz_ilosc_argumentow(*elementy):
    liczba = 0
    for ilosc in elementy:
        liczba += 1
    if liczba == 0 or liczba > 4:
        return("Użytkownik podał %d elementów" % liczba)
    else: return("Użytkownik podał %d elementy" % liczba)

def czy_poprawny_email(twoje_wyrazenie):
    wyrazenie = re.compile(twoje_wyrazenie)
    adresy = ["john@example.com", "python-list@python.org", '"wha.t.`1an?ug{}ly@email.com"']
    for adres in adresy:
        if not re.match(wyrazenie, adres):
            print ("Nie udalo ci sie przyporzadkowac %s" % (adres))
        elif not twoje_wyrazenie:
            print ("Nie wprowadziles wyrazenia do funkcji test_email")
        else:
            print ("Dobrze")

def czy_poprawny_email(adresy):
    walidator = r"(?:(?:[a-zA-Z0-9][a-zA-Z0-9\-]*)?[a-zA-Z0-9])"
    for adres in adresy:
        if not re.match(walidator, adres):
            print ("Nie udalo ci sie przyporzadkowac %s" % adres)
        elif not walidator:
            print ("Nie wprowadziles wyrazenia do funkcji test_email")
        else:
            print ("Dobrze")

def zwroc_imiona_nazwiska(parameter):
    imie = []
    nazwisko = []
    try:
        aktorzy = actors.aktorzy
    except AttributeError:
        return ("Słownik aktorów jest pusty")
    for dane in aktorzy:
        liczba = 0
        list = ""
        lista_podzielna = aktorzy[dane].split(" ")
        first, rest = lista_podzielna[0], lista_podzielna[1:]
        if parameter == "nazwisko":
            for ilosc in rest:
                liczba += 1
            if liczba != 1:
                for argumenty in rest:
                    list += argumenty + " "
                nazwisko += list.split(",")
            else:
                nazwisko += rest
        elif parameter == "imie":
            list += first
            imie += list.split(",")
    if parameter == "nazwisko":
        return nazwisko
    elif parameter == "imie":
        return imie
    else:
        return("Jako parametr musisz podać: imie, nazwisko")

