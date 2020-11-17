import os

imena = []

def preimenuj(datoteka):
    with open (datoteka, 'r', encoding='utf-8') as f:
        string = f.read()
        for x in imena:
            string = string.replace(x, 'uporabnik')
    with open (datoteka, 'w', encoding='utf-8') as f:
        f.write(string)
   

for datoteka in os.listdir('zajeti-podatki'):
    preimenuj('zajeti-podatki/' + datoteka)