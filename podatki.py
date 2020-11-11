import re
import pandas as pd
import orodja
import requests

URL = 'https://www.studentski-servis.com/index.php?t=prostaDela&page=1&perPage=1000&podjetje=&sort=1&workType=1&keyword=&urnaPostavkaMin=4.56&urnaPostavkaMax=20.00'

vzorec_sifre = r'Šifra:\s{1,100}</strong>\s{1,100}(?P<Šifra>\d{6})\s{1,100}'

vzorec_podrobnosti = re.compile(
    r'Delo:.*?<td class="tdDataMain">\s{1,100}(?P<delo>.*?)\s{1,100}</td>.*?'
    r'Kraj / Regija:.*?<td class="tdDataMain">\s{1,100}(?P<kraj>.*?)\s{1,100}'
    r'<br/>\s{1,100}\((?P<Regija>.*?)\)\s{1,100}</td>.*?'
    r'Plačilo:.*?<td class="tdDataMain">\s{1,100}(?P<plačilo>.*?)\s{1,100}</td>.*?'
    r'Naslov:.*?<td class="tdData" style="">\s{1,100}(?P<naslov>.*?)\s{1,100}</td>.*?'
    r'Datum pričetka:.*?<td class="tdData">\s{1,100}(?P<datum_pričetka>.*?)\s{1,100}</td>.*?'
    r'Delovnik:.*?<td class="tdData">\s{1,100}(?P<delovnik>.*?)\s{1,100}</td>.*?'
    r'Št\. članov:.*?<td class="tdData">\s{1,100}(?P<število_članov>\d{1,2})\s{1,100}</td>.*?'
    r'Trajanje:.*?<td class="tdData">\s{1,100}(?P<trajanje>.*?)\s{1,100}</td>.*?'
    r'Šifra oglasa:.*?<td class="tdData">\s{1,100}(?P<šifra>\d{6})\s{1,100}</td>.*?'
    r'Opis:.*?<p>\s{1,100}(?P<opis>.*?)\s{1,100}</p>.*?'
    r'Podjetje:.*?<td class="tdData">\s{1,100}(?P<podjetje>.*?)\s{1,100}(</td>|<p class="contactData">)',
    flags=re.DOTALL
)

def podrobnosti(sifra):
    url = (
        f'https://www.studentski-servis.com'
        f'/ess/podrobnosti.php?id={sifra}'
    )
    ime_datoteke = 'zajeti-podatki/podrobnosti-oglasa.{}.html'.format(sifra)
    orodja.shrani_spletno_stran(url, ime_datoteke)
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    return izloci_podatke_oglasa(vsebina)

def izloci_podatke_oglasa(vsebina):
    oglas = vzorec_podrobnosti.search(vsebina).groupdict()
    return oglas

orodja.shrani_spletno_stran(URL, 'zajeti-podatki/prosta-dela.html')
vsebina = orodja.vsebina_datoteke('zajeti-podatki/prosta-dela.html')
#sifre = re.findall(vzorec_sifre, vsebina, flags=re.DOTALL)
sifre = ['326859', '326855', '326854', '326853', '326852', '326851', '326850', '326849', '326845', '326842', '326841', '326840', '326839', '326838', '326837', '326836', '326834', '326832', '326830', '326829', '326828', '326827', '326826', '326824', '326823', '326822', '326820', '326819', '326818', '326817', '326814', '326812', '326810', '326809', '326808', '326807', '326804', '326803', '326802', '326799', '326798', '326796', '326795', '326792', '326791', '326790', '326789', '326788', '326787', '326785', '326780', '326778', '326777', '326776', '326775', '326774']

oglasi = []

for sifra in sifre:
    oglasi.append(podrobnosti(sifra))
orodja.zapisi_json(oglasi, 'obdelani-podatki/oglasi.json')
orodja.zapisi_csv(
    oglasi,
    ['delo', 'kraj', 'Regija', 'plačilo', 'naslov', 'datum_pričetka', 'delovnik', 'število_članov', 'trajanje', 'šifra', 'opis', 'podjetje'],
    'obdelani-podatki/oglasi.csv'
    )

print(len(sifre))
print(len(oglasi))