# tablica = []
# tablica.append(1)
# tablica.append(2)
# tablica.append(3)
# print (tablica[0]) # wypisze 1
# print (tablica[1]) # wypisze 2
# print (tablica[2]) # wypisze 3
########################################################################################################################
# # wypisze kolejno 1, 2, 3
# for x in tablica:
#     print (x)
#
# liczby = [1,2,3]
# napisy = ["witaj", 'swiecie']
# drugie_imie = napisy[1]
# print (drugie_imie)
########################################################################################################################
# reszta = 11 % 3
# print (reszta)
########################################################################################################################
# wielewitaj = "witaj " * 10
# print(wielewitaj)
########################################################################################################################
# parzyste_dodatnie = [2,4,6,8]
# nieparzyste_dodatnie = [1,3,5,7]
# naturalne = parzyste_dodatnie + nieparzyste_dodatnie
# print(naturalne)
########################################################################################################################
# x = object()
# y = object()
#
# x_tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# y_tab = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# duza_tab = x_tab + y_tab
#
# print ("x_tab zawiera %d obiektow" % len(x_tab))
# print ("y_tab zawiera %d obiektow" % len(y_tab))
# print ("duza_tab zawiera %d obiektow" % len(duza_tab))
#
# print(x_tab.count(0), y_tab.count(1))
########################################################################################################################
# wiek = [10, 30, 50]
# imiona = ["Marek", "Jola", "Basia"]
# print ("Witaj, %s, masz %d lat!" % (imiona[0], wiek[0]))
# imie = "Dorota"
# print ("Witaj, %s, masz %d lat!" % (imiona[1], wiek[1]))
########################################################################################################################
# dane = ("Dorota", 5, 32)
# print ("%s mieszka w bloku nr %d w mieszkaniu %d" % dane)
########################################################################################################################
# rzeczywista_1 = 4.345
# calkowita = 15
#
# print ("rzeczywista_1 = %f" % rzeczywista_1) #4.345000
# print ("rzeczywista_2 = %.1f" % rzeczywista_1) #4.3
# print ("W systemie szesnastkowym %d ma postac %X" % (calkowita, calkowita)) #15 ma postac F
########################################################################################################################
# napis = "AAA BBB ..."
# print (len(napis)) #11
########################################################################################################################
# napis = "abcdeabcde"
# print (napis.index("a")) # 0
# print (napis.index("d")) # 3
########################################################################################################################
# napis = "abrakadabra"
# print (napis.count("a"))  # 5
# print (napis.count("ab")) # 2
########################################################################################################################
# napis = "abcdefghijk"
# print (napis[2:4])
########################################################################################################################
# napis = "Witaj"
# print (napis.upper()) # WITAJ
########################################################################################################################
# napis = "Ala ma kota."
# print(napis.__contains__("ma")) #True
########################################################################################################################
# napis = "Ala ma kota."
# tablica_slow = napis.split(" ")
# tablica_slow[1] = tablica_slow.__contains__("ma") #jak pobrac tekst
# print (tablica_slow) # ['Ala', 'ma', 'kota']
########################################################################################################################
# imie = "Jan"
# wiek = 23
# if imie == "Jan" and wiek == 23:
#     print ("Nazywasz sie %s i masz %d lata." % (imie, wiek))
# elif imie in ["Robert", "Stefan"]:
#     print("Nie nazywasz się Jan")
# else:
#     print("Nie należysz do naszej spółki")
########################################################################################################################
# pierwsze = [2,3,5,7]
# for pierwsza in pierwsze:
#     print+ (pierwsza)
########################################################################################################################
# for x in range(6):
#     print (x),
########################################################################################################################
# tablica = [1,2,3,5,7,8,9,11,14,15,20]
# x = 0
# while x < len(tablica):
#     if tablica[x] % 2 == 0: print (tablica[x]),
#     x += 1
########################################################################################################################
# def przywitanie_imienne(imie, zyczenia):
#     return ("Witaj " + imie + ". Zycze Tobie " + zyczenia)
#
# print(przywitanie_imienne("Marcin", "szczescia"))
########################################################################################################################
# def lista_korzysci():
#     tablica = ["Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"]
#     return tablica
#
# def buduj_zdanie(info):
#     korzysci = ""
#     x = 0
#     while x < len(lista_korzysci()):
#         korzysci += lista_korzysci()[x] + ", "
#         x+= 1
#     odpowiedz = info + "Zaleta funkcji jest: " + korzysci
#     return odpowiedz
#
# def nazwij_korzysci_z_funkcji():
#     print (buduj_zdanie("Rozpoczynamy! "))
#
# nazwij_korzysci_z_funkcji()
########################################################################################################################
# class Pojazd:
#     kolor = ""
#     rodzaj = ""
#     wartosc = 0.00
#     nazwa = ""
#     def opis(self):
#         opis = ("%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc))
#         return opis
#
# Auto1 = Pojazd()
# Auto1.kolor = "czerwony"
# Auto1.rodzaj = "kabriolet"
# Auto1.wartosc = 60000
# Auto1.nazwa = "Ferrari"
#
# Auto2 = Pojazd()
# Auto2.kolor = "niebieski"
# Auto2.rodzaj = "autobus"
# Auto2.wartosc = 10000
# Auto2.nazwa = "Ikarus"
#
# print (Auto1.opis())
# print (Auto2.opis())
########################################################################################################################
# kolory = {
#     1 :	"biały",
#     2 :	"brązowy",
#     3 :	"czarny",
#     4 :	"czerwony",
#     5 :	"fioletowy",
#     6 :	"niebieski",
#     7 :	"pomarańczowy",
#     8 :	"różowy",
#     9 :	"szary",
#     10 : "zielony",
#     11 : "żółty"
# }
#
# for numer in kolory:
#     if kolory[numer] == "biały":
#         del kolory[numer]
#         break
#
# for numer in kolory:
#     print ("%d ma kolor: %s" % (numer, kolory[numer]))
########################################################################################################################
# import module
# help(module)
# print (module.lista_korzysci())
# if __name__ == '__main__':
#     print(a)
########################################################################################################################
# import module
# lista = "Duży czarny kot wszedł na płot, a później z niego spadł"
# print (module.lista_skladana(lista))
########################################################################################################################
# import module
# module.zmienna_liczba_argumentow("chcę", "złączyć", "kilka", "słów")
########################################################################################################################
import module
module.wypisz_ilosc_zmiennych(1, 2, 3, 4, 5)