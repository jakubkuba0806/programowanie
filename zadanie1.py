#zadanie 1
print("Zadanie 1A:")
print(type(1 + 2))
print(type(1 + 4.5))
print(type(3 / 2))
print(type(4 / 2))
print(type(3 // 2))
print(type(-3 // 2))
print(type(11 % 2))
print(type(2 ** 10))
print(type(8 ** (1/3)))
print()

print("Zadanie 1B:")
print(int(3.0)) # funkcja int() zamienia liczbe na liczbe calkowita (int), usuwajac część dziesiętną
print(float(3)) # funkcja float() zamienia liczbe calkowita na liczbe zmiennoprzecinkowa (float)
print(float("3")) # funckja float() zamienia tekst "3" na liczbe zmiennoprzecinkowa (float)
print(str(12.4)) # funkcja str() zanuebua kuczbe na tekst (str)
print(bool(0)) # funkcja bool() zamienia waretosc na logiczna (bool). Liczba 0 oznacza False.

#zadanie 2
print("Zadanie 2:")
print()
uczelnia = "Studiuje na WSIiZ"
print(uczelnia)

#zadanie 3
print("Zadanie 3:")
print()
imie = 'Jan'
wiek = 20
wzrost = 178
print("Nazywam się", imie, "i mam", wiek, "lat.")
print("Mój wzrost to", wzrost, "cm ")

#zadanie 4
print("Zadanie 4:")
print()

cena = 39.99
rabat = 0.2
cena_koncowa = cena * (1 - rabat)
print("Cena poczatkowa:", cena, "PLN")
print("Rabat:", rabat * 100, "%")
print("cena po rabacie:", round(cena_koncowa, 2), "PLN")

#zadanie 5
print("Zadanie 5:")
print()

a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku:"))

pole = a * b
obwod = 2 * (a + b)

print("Pole prostokata:", pole)
print("Obwod prostokata:", obwod)

#zadanie 6
print("Zadanie 6:")
print()

droga = float(input("Podaj dlugosc trasy w km: "))
spalanie = float(input("Podaj srednie spalanie w litrach na 100km: "))

cena_paliwa = 6.5

zuzycie = droga * spalanie / 100
koszt = zuzycie * cena_paliwa

print("Przewidywane zuzycie paliwa:", round(zuzycie, 2), "1")
print("Szacowany koszt podrozy: ", round(koszt, 2), "PLN")

#zadanie 6A
print("Zadanie 6A:")
print()

import random
droga = random.randint(100, 1000)
spalanie = float(input("Podaj srednie:"))

cena_paliwa = 6.5

zuzycie = droga * spalanie / 100
koszt = zuzycie * cena_paliwa

print("Dlugosc trasy: ", droga, "km")
print("Przewidywane zuzycie paliwa:", round(zuzycie, 2), "1")
print("Szacowany koszt podrozy:", round(koszt, 2), "PLN")

#zadanie 6B
print("Zadanie 6B:")
print()

import random
droga = random.randint(100, 1000)
spalanie = float(input("Podaj srednie spalanie w litrach na 100km:"))
cena_paliwa = 6.5
zuzycie = droga * spalanie / 100
koszt = zuzycie * cena_paliwa

print(f"dlugosc trasy: {droga} km")
print(f"Srednie spalanie: {spalanie} 1 / 100 km")
print(f"Przewidywane zuzycie paliwa: {zuzycie} PLN")
print(f"Szacowany koszt podrozy: {koszt} PLN")



