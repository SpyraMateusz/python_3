class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def oblicz_wartosc(self):
        return self.cena * self.ilosc

produkt1 = Produkt("Laptop", 2500, 2)
produkt2 = Produkt("Smartfon", 1200, 3)
produkt3 = Produkt("Klawiatura", 150, 5)

wartosc_produktu1 = produkt1.oblicz_wartosc()
wartosc_produktu2 = produkt2.oblicz_wartosc()
wartosc_produktu3 = produkt3.oblicz_wartosc()

print(f'Wartość produktu "{produkt1.nazwa}": {wartosc_produktu1} zł')
print(f'Wartość produktu "{produkt2.nazwa}": {wartosc_produktu2} zł')
print(f'Wartość produktu "{produkt3.nazwa}": {wartosc_produktu3} zł')