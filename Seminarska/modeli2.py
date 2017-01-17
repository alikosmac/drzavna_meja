import sqlite3

con = sqlite3.connect("meja16.sqlite")

def vseOsebeID():
    sql = """SELECT oseba.id FROM oseba """
    izvedba = con.execute(sql)
    stevilke = []
    for _ in izvedba:
        stevilke.append(_[0])
    return stevilke

def vsiDokumenti():
    sql = "SELECT dokument.st_dokumenta FROM dokument"
    izvedba = con.execute(sql)
    dokumenti = []
    for _ in izvedba:
        dokumenti.append(_[0])
    return dokumenti

def najdiOsebo(ime, priimek, spol, naslov, datumR):
    sql = "SELECT oseba.id FROM oseba WHERE oseba.ime = ? AND oseba.priimek = ? AND oseba.spol = ? AND oseba.naslov = ? AND oseba.datum_rojstva = ?"
    izvedba = con.execute(sql, [ime, priimek, spol, naslov, datumR])
    osebe = []
    for _ in izvedba:
        osebe.append(_[0])
    return osebe[0]

def najdiOsebaNaDokument(st_dokumenta):
    """ Najde ID osebe glede na dokument """
    sql = "SELECT oseba.id FROM oseba JOIN dokument on oseba.id = dokument.oseba WHERE dokument.st_dokumenta = ?"
    izvedba = con.execute(sql, [st_dokumenta])
    return list(izvedba)[0][0]

def isci_parametri(ime = "", priimek = "", spol = "", naslov = "", datumRojstva = "",
                    st_dokumenta = "", tipDokumenta = "", datumIzdajeDokument = "", datumPotekaDokument = "", kraticaDrzave = "",
                     vizaID = "", tipVize = "", datumIzdajeViza = "", datumPotekaViza = "",
                    prestopID = "", namen = "", mejniPrehod = "", datumPrestopa = ""):
                    """ Funkcija sprejme določene paramtere in na to glede na te vrne podatke, ki jih iščemo. Lahko se odločimo, da bomo vizo imeli, ali pa ne """
                    osebe = [] #Funkcija vrača le ID-je oseb, ki jih iščemo
                    #najprej zgradimo osnovni sql stavek, ki mu postopoma dodajamo pogoje v WHERE ali FROM stavku
                    sql = ""
                    
                    sql = """SELECT oseba.id
                                FROM oseba
                                    JOIN
                                    dokument ON oseba.id = dokument.oseba
                                    JOIN
                                    prestop ON dokument.st_dokumenta = prestop.dokument
                                    LEFT OUTER JOIN
                                    vizum ON dokument.st_dokumenta = vizum.dokument
                                    WHERE """
                    
                    pogoji = [] #Tu bomo dodajali pogoje, ki jih kasneje nalepimo, na naš sql stavek
                    parametri = [] #tukaj se dodajajo parametri, ki so argumenti funkcij
                    #Kar se tiče osebe
                    
                    if ime is not "":
                        pogoji.append(" oseba.ime LIKE ? ")
                        parametri.append("%"+ime+"%")
                    
                    if priimek is not "":
                        pogoji.append(" oseba.priimek LIKE ? ")
                        parametri.append("%"+priimek+"%")
                    
                    if len(spol) != 0:
                        pogoji.append(" oseba.spol IN ({0}) ".format(', '.join('?' for _ in spol)))
                        parametri += spol
                    
                    if naslov is not "":
                        pogoji.append(" oseba.naslov LIKE ? ")
                        parametri.append("%"+naslov+"%")
                    
                    if datumRojstva is not "":
                        pogoji.append(" oseba.datum_rojstva LIKE ? ")
                        parametri.append("%"+datumRojstva+"%")
                    
                    #Kar se tiče dokumenta

                    if st_dokumenta is not "":
                        pogoji.append(" dokument.st_dokumenta LIKE ? ")
                        parametri.append("%"+st_dokumenta+"%")
                    
                    if len(tipDokumenta) != 0:
                        pogoji.append(" dokument.tip IN ({0}) ".format(', '.join('?' for _ in tipDokumenta)))
                        parametri += tipDokumenta
                    
                    if datumIzdajeDokument is not "":
                        pogoji.append(" dokument.datum_izdaje LIKE ? ")
                        parametri.append("%"+datumIzdajeDokument+"%")
                    
                    if datumPotekaDokument is not "":
                        pogoji.append(" dokument.datum_poteka LIKE ? ")
                        parametri.append("%"+datumPotekaDokument+"%")
                    
                    if len(kraticaDrzave) != 0:
                        pogoji.append(" dokument.drzava IN ({0}) ".format(', '.join('?' for _ in kraticaDrzave)))
                        parametri += kraticaDrzave
                    
                    
                    #Kar se tiče prestopa

                    if prestopID is not "":
                        pogoji.append(" prestop.id LIKE ? ")
                        parametri.append("%"+prestopID+"%")
                    
                    if namen is not "":
                        pogoji.append(" prestop.namen LIKE ? ")
                        parametri.append(namen)
                    
                    if datumPrestopa is not "":
                        pogoji.append(" prestop.datum LIKE ? ")
                        parametri.append("%"+datumPrestopa+"%")
                    
                    if len(mejniPrehod) != 0:
                        pogoji.append(" prestop.mejni_prehod IN ({0}) ".format(', '.join('?' for _ in mejniPrehod)))
                        parametri += mejniPrehod
                    

                    #Kar se tiče vize

                    
                    if vizaID is not "":
                        pogoji.append(" vizum.id LIKE ? ")
                        parametri.append(vizaID)
                        
                    if len(tipVize) != 0:
                        pogoji.append(" vizum.tip IN ({0}) ".format(', '.join('?' for _ in tipVize)))
                        parametri += tipVize
                        
                    if datumIzdajeViza is not "":
                        pogoji.append(" vizum.datum_izdaje LIKE ? ")
                        parametri.append("%"+datumIzdajeViza+"%")
                        
                    if datumPotekaViza is not "":
                        pogoji.append(" vizum.datum_poteka LIKE ? ")
                        parametri.append("%"+datumPotekaViza+"%")

                    sql += " AND ".join(pogoji)
                    izvedi = con.execute(sql, parametri)
                    for x in izvedi:
                        osebe.append(x[0])
                    return set(osebe)

def izpisPodatkov(stevilke):
    """Prejme ID neke osebe in vrne podatke, ki jih želimo izpisati v uporabniškem vmesniku"""
    sql = """SELECT oseba.ime, oseba.priimek, oseba.spol, oseba.naslov, drzava.naziv, oseba.datum_rojstva, dokument.st_dokumenta
            FROM oseba JOIN dokument ON oseba.id = dokument.oseba JOIN drzava on dokument.drzava = drzava.kratica JOIN prestop ON dokument.st_dokumenta = prestop.dokument JOIN mejni_prehod ON prestop.mejni_prehod = mejni_prehod.koda
            WHERE oseba.id = ? """
    izvedba = con.execute(sql, [stevilke])
    oseba = []
    for x in list(izvedba)[0]:
        oseba.append(x)
    return oseba

def izpisVecih(stevilke):
    osebe = []
    for x in stevilke:
        if int(x) in vseOsebeID():
            osebe.append("_".join(izpisPodatkov(x)))
    
    return "_".join(osebe)
##############################################################################
def blackList():
    """Vrne vse tiste stevilke oseb, ki so v državi, ampak ne bi smeli biti """
    osebe = set()
    #Najprej preverimo tiste, ki so jim potekli dokumenti ali pa so lažni,
    #kar pomeni, da začnejo veljati šele po vstopu
    sql1 = """SELECT oseba.id
                FROM oseba
                    JOIN
                    dokument ON oseba.id = dokument.oseba
                    JOIN
                    prestop ON dokument.st_dokumenta = prestop.dokument
                WHERE dokument.datum_poteka < prestop.datum OR 
                    dokument.datum_izdaje > prestop.datum; """
    for st in con.execute(sql1):
        osebe.add(st[0])
    
    #Zdaj preverimo še tiste, ki nimajo veljavne vize 
    #bodi si jim je potekla pred dokumentom
    #ali pa jim je potekla ko so hoteli prestopiti

    sql2 = """ SELECT oseba.id
                FROM oseba
                    JOIN
                    dokument ON oseba.id = dokument.oseba
                    JOIN
                    vizum ON dokument.st_dokumenta = vizum.dokument
                    JOIN
                    prestop ON dokument.st_dokumenta = prestop.dokument
                WHERE vizum.datum_poteka < dokument.datum_poteka OR 
                    vizum.datum_izdaje > dokument.datum_izdaje OR 
                    vizum.datum_poteka < prestop.datum OR 
                    vizum.datum_izdaje > prestop.datum;"""
    for st in con.execute(sql2):
        osebe.add(st[0])
    
    return list(osebe)

########Funkcije za dodajanje v bazo################################################
def dodajOsebo(ime, priimek, spol, naslov = None, datum_rojstva = None):
  sql = "INSERT INTO oseba (ime, priimek, spol, naslov, datum_rojstva) VALUES (?, ?, ?, ?, ?)"
  con.execute(sql, (ime, priimek, spol, naslov, datum_rojstva))
  con.commit()

def dodajDokument(st_dokumenta, oseba, tip, datum_izdaje, datum_poteka, drzava):
    sql = "INSERT INTO dokument (st_dokumenta, oseba, tip, datum_izdaje, datum_poteka, drzava) VALUES (?, ?, ?, ?, ?, ?)"
    con.execute(sql, (st_dokumenta, oseba, tip, datum_izdaje, datum_poteka, drzava))
    con.commit()

def dodajVizum(dokument, tip, datum_izdaje, datum_poteka):
    sql = "INSERT INTO vizum (dokument, tip, datum_izdaje, datum_poteka) VALUES (?, ?, ?, ?)"
    con.execute(sql, (dokument, tip, datum_izdaje, datum_poteka))
    con.commit()

def dodajPrestop(dokument, namen, mejni_prehod, datum):
    sql = "INSERT INTO prestop (dokument, namen, mejni_prehod, datum) VALUES (?, ?, ?, ?)"
    con.execute(sql, (dokument, namen, mejni_prehod, datum))
    con.commit()

def izpisZaNaSpletno(niz):
    sez = niz.split(" ")
    return izpisVecih(sez)

                    
def rezultati(ime = "", priimek = "", spol = "", naslov = "", datumRojstva = "",
                    st_dokumenta = "", tipDokumenta = "", datumIzdajeDokument = "", datumPotekaDokument = "", kraticaDrzave = "",
                     vizaID = "", tipVize = "", datumIzdajeViza = "", datumPotekaViza = "",
                    prestopID = "", namen = "", mejniPrehod = "", datumPrestopa = ""):

                    #najprej izracunamo stevilke oseb
                    st_oseb = isci_parametri(ime, priimek, spol, naslov, datumRojstva,
                    st_dokumenta, tipDokumenta, datumIzdajeDokument, datumPotekaDokument, kraticaDrzave,
                     vizaID, tipVize, datumIzdajeViza, datumPotekaViza,
                    prestopID, namen, mejniPrehod, datumPrestopa)

                    return izpisVecih(st_oseb)

def dodajVse(ime, priimek, spol, naslov, datum_rojstva,
             st_dokumenta, tipDokumenta, datumIzdajeDokument, datumPotekaDokument, kraticaDrzava,
             tipVize, datumIzdajeViza, datumPotekaViza,
             namen, mejniPrehod, datumPrestopa):
             
             dodajOsebo(ime, priimek, spol, naslov, datum_rojstva)

             #osebaId = najdiOsebo(ime = ime, priimek = priimek, spol = spol, naslov = naslov, datumR = datum_rojstva)
            
             dodajDokument(st_dokumenta = st_dokumenta, oseba = najdiOsebo(ime = ime, priimek = priimek, spol = spol, naslov = naslov, datumR = datum_rojstva), tip = tipDokumenta, datum_izdaje = datumIzdajeDokument,
                            datum_poteka = datumPotekaDokument, drzava = kraticaDrzava)
             
             if tipVize != "Brez":
                 dodajVizum(dokument = st_dokumenta, tip = tipVize, datum_izdaje = datumIzdajeViza, 
                            datum_poteka = datumPotekaViza)
            
             dodajPrestop(dokument = st_dokumenta, namen = namen, mejni_prehod = mejniPrehod, datum = datumPrestopa)



if __name__ == "__main__":
    dodajVse("Elvis", "Muharemagic", "M", "Sela 14-Krmelj", "1990-13-07", "SV99525134", "Osebni dokument", "2015-07-11", "2025-07-11", "SVN", "Brez", "", "", "Izhod", "3", "2017-17-01")