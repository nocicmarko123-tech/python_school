from class4_auto_composition_elektricni import Baterija
from class4_auto_composition_elektricni import ElekticniAuto
from class4_auto_composition_elektricni import Auto

def unos1():
    proizvodjac = input("Koji je proizvodjac automobila? ")
    model = input("Koji je model automobila? ")
    return (proizvodjac, model)


def unos2():
    godina = int(input("Koje godine je auto proizveden?  "))
    kilometara = int(input("Za koliko je uvecana kilometraza? "))
    return (godina, kilometara)


moj_auto = Auto(*unos1())
moj_auto.opisi_auto()
moj_auto.godiste_kilometraza(*unos2())
moj_auto.punjenje()

print("-" * 30)

baterija = int(input("Koliki je kapacitet baterije? "))
moja_tesla = ElekticniAuto(*unos1(), baterija)
moja_tesla.opisi_auto()
moja_tesla.godiste_kilometraza(*unos2())
moja_tesla.baterija.opis_baterije()  # poziv metode preko atributa
# moj_auto.opis_baterije()  <--  izbacilo bi ERROR jer moj_auto nije elektricni
moja_tesla.punjenje()  # Koristimo preklopljenu metodu