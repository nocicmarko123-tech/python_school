class Konzola:
    def __init__(self, naziv):
        self.naziv = naziv

    def pokreni_igru(self, ime_igre):
        # Koristimo self.naziv za ime konzole, a ime_igre kao parametar
        print(f"[{self.naziv}] Učitava se igra: {ime_igre}")

class SuperKonzola(Konzola):
    def __init__(self, naziv, kapacitet):
        # Pozivamo konstruktor roditeljske klase
        super().__init__(naziv)
        self.kapacitet = kapacitet

    def pokreni_igru(self, ime_igre):
        print(f"\n--- {self.naziv} PRO MOD ---")
        print("Proveravam licencu na internetu...")
        print(f"Igra '{ime_igre}' se pokreće sa SSD-a kapaciteta {self.kapacitet}")

# Unos podataka
ime_igre = input("Ime igre: ").title()
ime_konzole = input("Ime konzole: ").title()
kapacitet = input("Kapacitet SSD-a: ")

# 1. Kreiramo objekte (instance)
obicna_konzola = Konzola(ime_konzole)
mocna_konzola = SuperKonzola(ime_konzole, kapacitet)

# 2. Pozivamo metode nad objektima
obicna_konzola.pokreni_igru(ime_igre)
mocna_konzola.pokreni_igru(ime_igre)
