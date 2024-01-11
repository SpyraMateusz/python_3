class KontoBankowe:
    def __init__(self, numer_konta, saldo, waluta):
        self.numer_konta = numer_konta
        self.saldo = saldo
        self.waluta = waluta

    def __str__(self):
        return f"Konto {self.numer_konta} - Saldo: {self.saldo} {self.waluta}"

    def __add__(self, other):
        if isinstance(other, KontoBankowe):
        
            nowy_numer_konta = f"{self.numer_konta}+{other.numer_konta}"
            nowe_saldo = self.saldo + other.saldo
            nowa_waluta = self.waluta if self.saldo >= other.saldo else other.waluta

            return KontoBankowe(nowy_numer_konta, nowe_saldo, nowa_waluta)
        else:
            raise TypeError("Operacja dostępna tylko dla obiektów klasy 'KontoBankowe'.")

    def __sub__(self, other):
        if isinstance(other, KontoBankowe):
            
            nowy_numer_konta = f"{self.numer_konta}-{other.numer_konta}"
            nowe_saldo = self.saldo - other.saldo
            nowa_waluta = self.waluta if self.saldo >= other.saldo else other.waluta

            return KontoBankowe(nowy_numer_konta, nowe_saldo, nowa_waluta)
        else:
            raise TypeError("Operacja dostępna tylko dla obiektów klasy 'KontoBankowe'.")

    def __lt__(self, other):
        if isinstance(other, KontoBankowe):
            
            return self.saldo < other.saldo
        else:
            raise TypeError("Operacja dostępna tylko dla obiektów klasy 'KontoBankowe'.")

konto1 = KontoBankowe("12345", 1000, "PLN")
konto2 = KontoBankowe("67890", 500, "USD")

nowe_konto = konto1 + konto2
print(nowe_konto)

roznica_konta = konto1 - konto2
print(roznica_konta)

if konto1 < konto2:
    print(f"Konto {konto1.numer_konta} ma mniejsze saldo niż konto {konto2.numer_konta}")
else:
    print(f"Konto {konto1.numer_konta} ma większe saldo niż konto {konto2.numer_konta}")