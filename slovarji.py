import orodja
import re

# V tej python datoteki iz osnovne spletne strani zajamemo vsebino in naredimo slovar_del, 
# ki sporoča, katera dela spadajo pod določeno vrsto del. Analogno za slovar_regij, ki pa je 
# prepisan na roke.

URL = 'https://www.studentski-servis.com/studenti/prosta-dela/'

#orodja.shrani_spletno_stran(URL, 'zajeti-podatki/osnovna_spletna_stran.html')

with open('zajeti-podatki/osnovna_spletna_stran.html',encoding='utf-8') as f:
    html = f.read()

vzorec = re.compile(
    r'<label class="custom-control-label" for="group-A\d{3}">\s+(?P<delo>.*?)\s+</label>'
)

vzorec_blok = re.compile(
    r'<label class="custom-control-label" for="group-\d{3}">\s+(?P<vrsta_dela>.*?)\s+</label>.*?'
    r'</div>\s+</div>\s+</div>\s+</div>\s+</div>',
    flags=re.DOTALL
)

vrsta_del = vzorec_blok.findall(html)
vrsta_del = [x.upper() for x in vrsta_del]
slovar_del ={}
for blok in vzorec_blok.finditer(html):
    delo = vzorec.findall(blok.group(0))
    delo = [x.upper() for x in delo]
    vrsta_dela = vrsta_del[0]
    slovar_del[vrsta_dela] = delo
    vrsta_del = vrsta_del[1:]
slovar_del['STROKOVNA DELA'].append("UREJANJE DRUŽ. OMREŽIJ (FB,IN,TW)")
#print(slovar_del)

osrednjeslovenska = ['LJUBLJANA Z OKOLICO', 'DOMŽALE-KAMNIK', 'GROSUPLJE Z OKOLICO', 'VRHNIKA Z OKOLICO']
podravska = ['MARIBOR Z OKOLICO', 'PTUJ Z OKOLICO']
gorenjska = ['KRANJ Z OKOLICO', 'ŠKOFJA LOKA Z OKOLICO', 'RADOVLJICA Z OKOLICO', 'JESENICE Z OKOLICO']
obalnokraška = ['KOPER Z OKOLICO', 'IZOLA Z OKOLICO', 'PIRAN Z OKOLICO']
slovar_regij = {'OSREDNJESLOVENSKA': osrednjeslovenska, 'PODRAVSKA': podravska, 'GORENJSKA': gorenjska, 'OBALNOKRAŠKA': obalnokraška}
           
