class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def podwyzka(self, procent_podwyzki):
        if procent_podwyzki > 0:
            self.pensja += self.pensja * (procent_podwyzki / 100)

pracownik1 = Pracownik("Jan", "Kowalski", 5000)

print(f'Początkowa pensja: {pracownik1.pensja}')

pracownik1.podwyzka(10) 
print(f'Pensja po podwyżce o 10%: {pracownik1.pensja}')

pracownik1.podwyzka(5) 
print(f'Pensja po kolejnej podwyżce o 5%: {pracownik1.pensja}')