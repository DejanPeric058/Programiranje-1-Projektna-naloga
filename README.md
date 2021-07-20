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
* Kje je največ prostih študentskih del in kje najmanj?
* Programiranje je najbolje plačano študentsko delo.
* Katero je povprečno najslabše plačano delo?

V datoteki oglasi.csv so shranjeni podatki o oglasih. Zajel sem podatke: delo, kraj, regija, plačilo(neto in bruto oz. po dogovoru), naslov, datum pričetka, delovnik, število članov(število iskanih študentov za delo), šifra, opis in ime podjetja, ki ponuja delo.

Za zajem podrobnosti oglasov sem najprej iz osnovne strani zajel vse šifre oglasov, prek katerih sem se potem zapeljal za pridobitev podatkov s spletnih strani o podrobnostih oglasov.

Uspelo mi je zajeti 751 oglasov za razpoložljiva študentska dela. 
Podatki teh oglasov so zapisani v csv in json datoteki. V reporzitoriju je tudi datoteka prijava.py, s pomočjo katere lahko pobiram podatke s strani, na katerih moram biti prijavljen.
