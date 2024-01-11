class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        pole = self.bok ** 2
        return pole

    def oblicz_obwod(self):
        obwod = 4 * self.bok
        return obwod

kwadrat1 = Kwadrat(5)

pole = kwadrat1.oblicz_pole()
obwod = kwadrat1.oblicz_obwod()

print(f'Pole kwadratu: {pole}')
print(f'Obwód kwadratu: {obwod}')