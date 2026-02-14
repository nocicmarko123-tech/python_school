class Auto:
    """Klasa koja predstavlja automobil."""

    def __init__(self, proizvodjac, model):
        """Inicijalizujte atribute da bi ste opisali automobil."""
        self.proizvodjac = proizvodjac
        self.model = model
        self.kilometraza = 2345

    def opisi_auto(self):
        """Prikazuje osnovne podatke automobila."""
        print(f" Auto je  {self.proizvodjac}  , model {self.model} ")

    def godiste_kilometraza(self, godina, kilometara):
        """Prikazuje godiste i ukupnu kilometražu automobila."""
        print(f"Auto ima {2025 - godina}  godina.")
        self.kilometraza += kilometara
        print(f"Auto je presao {self.kilometraza} kilometara.")

    def punjenje(self):  # Preklopljena metoda
        print("Pazite da li vaš auto koristi dizel ili benzin! ")
