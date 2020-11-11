# Prosta študentska dela

Projektna naloga iz analize podatkov pri predmetu Programiranje 1

Zajel in analiziral bom razpoložljiva delovna mesta ponujena na spletni strani [e-Študentski servis](https://www.studentski-servis.com/index.php?t=prostaDela&page=1&perPage=10&podjetje=&sort=1&workType=1&keyword=&urnaPostavkaMin=&urnaPostavkaMax=).

Zajel bom naslednje podatke:
* Vrsta dela
* Lokacija izvajanja dela
* Plačilo dela (€/h neto oz. bruto)
* Trajanje dela
* Delovnik

Na podlagi teh podatkov nameravam preveriti:
* V kateri regiji so ponujena študentska dela povprečno najbolje plačana in kje najslabše?
* Kakšen je najpogostejši tip delovnika?
* Katera vrsta del v določenih regijah prevladujejo?

V datoteki oglasi.csv so shranjeni podatki o oglasih. Zajel sem podatke: delo, kraj, regija, plačilo(neto in bruto oz. po dogovoru, naslov, datum pričetka, delovnik, število članov(število iskanih študentov za delo), šifra, opis in ime podjetja, ki ponuja delo.

Za zajem podrobnosti oglasov sem najprej iz osnovne strani zajel vse šifre oglasov, prek katerih sem se potem zapeljal za pridobitev podatkov s spletnih strani o podrobnostih oglasov.

Zaradi omejitve strani, da lahko pregledam samo 30 podrobnosti oglasov, jih bom zajemal do decembra, zaenkrat pa mi jih je uspelo zajeti 56. 
Podatki teh oglasov so zapisani v csv in json datoteki. V reporzitoriju je tudi datoteka prijava.py, s pomočjo katere lahko pobiram podatke s strani, na katerih moram biti prijavljen.
