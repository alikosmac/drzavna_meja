from bottle import *
import modeli2

@route('/')
def index():
    return template('prva')

@route('/iskanje2')
def iskanje():
    return template('iskanje2')

@route('/rezultati')
def rezultati():
    #O osebi
    ime = request.query.ime
    priimek = request.query.priimek
    datum_rojstva = request.query.datumR
    naslov = request.query.naslov
    spol = request.query.getall('spol')
    #O dokumentu
    st_dokumenta = request.query.st_dokumenta
    datum_izdajeD = request.query.datum_izdajeD
    datum_potekaD = request.query.datum_potekaD
    drzava = request.query.getall('drzava')
    tipD = request.query.getall('tip_dokumenta')
 

    #O vizi
    datum_izdajeV = request.query.datum_izdajeV
    datum_potekaV = request.query.datum_potekaV
    tipV = request.query.getall('vizumTip')
    print(tipV)

    #O prestopu
    namen = request.query.namen
    datum_prestopa = request.query.datumP
    mejni_prehod = request.query.getall('mejniPrehod')

    return template('rezultati', ime = ime, priimek = priimek, datum_rojstva = datum_rojstva, naslov = naslov, spol = spol,
    st_dokumenta = st_dokumenta, datum_izdajeD = datum_izdajeD, datum_potekaD = datum_potekaD, drzava = drzava, tipD = tipD,
    datum_izdajeV = datum_izdajeV, tipV = tipV, namen = namen, datum_prestopa = datum_prestopa, mejni_prehod = mejni_prehod, podatki = modeli2.rezultati(ime = ime, priimek = priimek, naslov = naslov, datumRojstva = datum_rojstva, spol = spol, st_dokumenta = st_dokumenta, datumIzdajeDokument = datum_izdajeD, tipDokumenta = tipD,datumPotekaDokument = datum_potekaD,kraticaDrzave = drzava, datumIzdajeViza = datum_izdajeV, tipVize = tipV, datumPotekaViza = datum_potekaV, namen = namen, datumPrestopa = datum_prestopa, mejniPrehod = mejni_prehod))


@route('/zacniDodajanje')
def zacniDodajanje():
    return template('zacniDodajanje')

#naredimo prazno speltno stran namenjeno preusmeritvi
@route('/preusmeri1')
def preusmeri1():
    dokument = request.query.dokument
    if dokument in modeli2.vsiDokumenti():
        mnozica = set()
        oseba = modeli2.najdiOsebaNaDokument(dokument)
        mnozica.add(oseba)

        if int(oseba) in modeli2.blackList():
            return template('neveljavniPapirji')
        
        else:  
            return template('dodajanjeZeZnan', dokument = dokument, podatkiOseba = modeli2.izpisVecih(mnozica))
    else:
        return template('dodajanje', dokument = dokument)

@route('/preusmeri2')
def preusmeri2():
    dokument = request.query.dokument
    namen = request.query.namen
    datumP = request.query.datumP
    mejniPrehod = request.query.mejniPrehod
    return template("uspeh", dokument = dokument, namen = namen, datumP = datumP, mejniPrehod = mejniPrehod, dodajanje = modeli2.dodajPrestop(dokument, namen, mejniPrehod, datumP))


@route('/preusmeri3')
def preusmeri3():
    #O osebi
    ime = request.query.ime
    priimek = request.query.priimek
    spol = request.query.spol
    naslov = request.query.naslov
    datumR = request.query.datumR

    #O dokumentu
    st_dokumenta = request.query.st_dokumenta
    tip_dokumenta = request.query.tip_dokumenta
    datum_izdajeD = request.query.datum_izdajeD
    datum_potekaD = request.query.datum_potekaD
    drzava = request.query.drzava

    #O vizumu
    vizumTip = request.query.vizumTip
    datum_izdajeV = request.query.datum_izdajeV
    datum_potekaV = request.query.datum_potekaV

    #O prestopu
    namen = request.query.namen
    mejniPrehod = request.query.mejniPrehod
    datumP = request.query.datumP
    
    return template("uspeh", ime = ime, priimek = priimek, spol = spol, naslov = naslov, datumR = datumR,
                    st_dokumenta = st_dokumenta, tip_dokumenta = tip_dokumenta, datum_izdajeD = datum_izdajeD, datum_potekaD = datum_potekaD, drzava = drzava,
                    vizumTip = vizumTip, datum_izdajeV = datum_izdajeV, datum_potekaV = datum_potekaV,
                    namen = namen, mejniPrehod = mejniPrehod, datumP = datumP, 
                    izvedba = modeli2.dodajVse(ime, priimek, spol, naslov, datumR, st_dokumenta, tip_dokumenta,
                    datum_izdajeD, datum_potekaD, drzava, vizumTip, datum_izdajeV, datum_potekaV, namen, mejniPrehod, datumP))

@route('/dodajanje')
def dodajanje():
    return template('dodajanje')

@route('/dodajanjeZeZnan')
def dodajanjeZeZnan():
    return template('dodajanjeZeZnan')

@route('/neveljavniPapirji')
def neveljavniPapirji():
    return template('neveljavniPapirji')


@route('<filename:re:.*\.css>',name='static')
def css(filename):
    return static_file(filename,root='.',mimetype='text/css')




run(reloder = True, debug = True)