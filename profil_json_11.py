import pathlib
import json

file = pathlib.Path("profil.json")
try:
    content = file.read_text()
    profil = json.loads(content)
    print(profil)  
except :    
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    omiljeni_predmet = input("Unesite omiljeni predmet: ")
    profil = {
              "ime": ime, 
              "prezime": prezime, 
              "omiljeni_predmet": omiljeni_predmet
              }
    content = json.dumps(profil)
    file.write_text(content)
    print("Profil saved")
