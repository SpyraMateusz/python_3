import math

class Okrąg:
    def __init__(self, promien):
        self.promien = promien

    def __str__(self):
        return f'Okrąg o promieniu {self.promien}'

    def __add__(self, other):
        if isinstance(other, Okrąg):
            # Suma promieni dwóch okręgów
            nowy_promien = self.promien + other.promien
            return Okrąg(nowy_promien)
        else:
            raise TypeError("Operacja dostępna tylko dla obiektów klasy 'Okrąg'.")

okrag1 = Okrąg(5)
okrag2 = Okrąg(3)

print(okrag1) 
print(okrag2)  

nowy_okrag = okrag1 + okrag2
print(nowy_okrag) 