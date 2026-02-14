from class4_auto_composition_auto import Auto

class Baterija:
    def __init__(self, baterija=45):  # podrazum. vrednost moze i ovako
        self.baterija = baterija  # instanciramo atribut klase Baterija !!!

    def opis_baterije(self):  # ovaj metod smo premestili u klasu Baterija
        print(f"Ovaj auto ima {self.baterija} kWh bateriju")


class ElekticniAuto(Auto):  # Ovim smo rekli da je ElekticniAuto dete klase Auto
    def __init__(self, proizvodjac, model, baterija):  # dete preuzima atribute
        super().__init__(proizvodjac, model)  # preuzima atr. i met. klase roditelj
        self.baterija = Baterija(baterija)  # dodajemo novi atribut samo za el. Automobile

    # def opis_baterije(self):
    #    print(f"Ovaj auto ima {self.baterija} kWh bateriju")

    def punjenje(self):
        print("Koristite isključivo utičnice odgovarajuće snage! ")

    def opisi_auto(self):  # "Pametni" overriding
        # Prvo kažemo roditelju da ispiše ono što on zna
        super().opisi_auto()
        # Zatim mi dodajemo ono što je specifično za nas
        # print(f"Ovaj auto ima {self.baterija} kWh bateriju")