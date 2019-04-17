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
    print("podane argumenty: %s" % list)

def wypisz_ilosc_argumentow(*elementy):
    liczba = 0
    for ilosc in elementy:
        liczba += 1
    if liczba == 0 or liczba > 4:
        print("Użytkownik podał %d elementów" % liczba)
    else: print("Użytkownik podał %d elementy" % liczba)