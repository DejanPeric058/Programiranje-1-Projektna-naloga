import orodja
import re

#URL = 'https://www.studentski-servis.com/studenti/prosta-dela/'

#orodja.shrani_spletno_stran(URL, 'osnovna_spletna_stran.html')

with open('osnovna_spletna_stran.html',encoding='utf-8') as f:
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
slovar_del ={}
for blok in vzorec_blok.finditer(html):
    delo = vzorec.findall(blok.group(0))
    vrsta_dela = vrsta_del[0]
    slovar_del[vrsta_dela] = delo
    vrsta_del = vrsta_del[1:]
print(slovar_del)


           
