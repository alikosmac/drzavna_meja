% rebase('osnova.tpl')
 

<body bgcolor = "#dcedc8">
<h2 class="center">Dodajanje Prestopa</h2>


<form action = "/preusmeri3">
    <div class="row">
            <div class="input-field col s12">
            <h5>Podatki o osebi</h5>
            </div>

            <div class="input-field col s6">
                <i class="material-icons prefix">perm_identity</i>
                <input id="ime" name = "ime" type="text" class="validate">
                <label for="ime">Ime</label>
            </div>
            
            <div class="input-field col s6">
                <i class="material-icons prefix">perm_identity</i>
                <input id="priimek" name = "priimek" type="text" class="validate">
                <label for="priimek">Priimek</label>
            </div>

            <div class="input-field col s6">
                <i class="material-icons prefix">perm_contact_calendar</i>
                <input placeholder = "YYYY-DD-MM" maxlength = 10 id="datum_rojstva" name = "datumR" type="text" class="validate">
                <label for="datum_rojstva">Datum Rojstva</label>
            </div>

            <div class="input-field col s6">
                <i class="material-icons prefix">business</i>
                <input id="naslov" placeholder = "Ulica #-Mesto" name = "naslov" type="text" class="validate">
                <label for="naslov">Naslov</label>
            </div>

            <div class="input-field col s12">
            <h5>Spol</h5>
            </div>

            <div class="input-field col s12" style="margin-bottom:30px;">
                <input type="radio" id="moski" name = "spol" value = "M"/>
                <label for="moski">Moški</label>
                &nbsp;
                <input type="radio" id="zenska" name = "spol" value = "F"/>
                <label for="zenska">Ženska</label>

            </div>
        
        <div class="input-field col s12">
        <h5>Podatki o dokumentu</h5>
        </div>

        <div class="input-field col s6">
                <input placeholder = "XX00000000" maxlength = 10 id="st_dokumenta" name = "st_dokumenta" value = {{dokument}} type="text" class="validate">
                <label for="st_dokumenta">Številka Dokumenta</label>
         </div>

         <div class="input-field col s6">
                <select multiple name = "tip_dokumenta">
                <option value = "Potni list">Potni list</option>
                <option value = "Osebna izkaznica">Osebni dokument</option>
                </select>
                <label>Tip dokumenta</label>
        </div>


        <div class="input-field col s6">            
                <input placeholder = "YYYY-DD-MM" maxlength = 10 id="datum_izdajeD" name = "datum_izdajeD" type="text" class="validate">
                <label for="datum_izdajeD">Datum izdaje dokumenta</label>
        </div>

        <div class="input-field col s6">
                <input placeholder = "YYYY-DD-MM" maxlength = 10 id="datum_potekaD" name = "datum_potekaD" type="text" class="validate">
                <label for="datum_potekaD">Datum poteka dokumenta</label>
        </div>

        <div class="input-field col s12">
            <select name = "drzava">
            <option value = "ALB">Albanija</option>
            <option value = "AUS">Avstralija</option>
            <option value = "AUT">Avstrija</option>
            <option value = "BHR">Bahrain</option>
            <option value = "BIH">Bosna in Hercegovina</option>
            <option value = "CAN">Kanada</option>
            <option value = "CHF">Švica</option>
            <option value = "CRO">Hrvaška</option>
            <option value = "DEU">Nemčija</option>
            <option value = "DNK">Danska</option>
            <option value = "EGY">Egipt</option>
            <option value = "FIN">Finska</option>
            <option value = "GBR">Velika Britanija</option>
            <option value = "IRE">Irska</option>
            <option value = "ISR">Izrael</option>
            <option value = "MKD">Makedonija</option>
            <option value = "MTN">Črna Gora</option>
            <option value = "NOR">Norveška</option>
            <option value = "NZL">Nova Zelandija</option>
            <option value = "QAT">Katar</option>
            <option value = "SAU">Savdska Arabija</option>
            <option value = "SRB">Srbija</option>
            <option value = "SVN">Slovenija</option>
            <option value = "SWE">Švedska</option>
            <option value = "UAE">Združeni arabski Emirati</option>
            <option value = "UNK">Kosovo</option>
            <option value = "USA">Združene države Amerike</option>
            </select>
            <label>Država</label>
        </div>
        <h5>Podatki o vizumu</h5>

        <div class="input-field col s6">
                <input placeholder = "YYYY-DD-MM" maxlength = 10 id="datum_izdajeV" name = "datum_izdajeV" type="text" class="validate">
                <label for="datum_izdajeV">Datum izdaje vizuma</label>
        </div>

        <div class="input-field col s6">
                <input placeholder = "YYYY-DD-MM" maxlength = 10 id="datum_potekaV" name = "datum_potekaV" type="text" class="validate">
                <label for="datum_potekaV">Datum poteka vizuma</label>
        </div>

        <div class="input-field col s12">
                <select name = "vizumTip">
                <option value = "Brez">Vizum ni potreben</option>
                <option value = "Delavska">Delavska</option>
                <option value = "Diplomatska">Diplomatska</option>
                <option value = "Dolgorocna">Dolgoročna</option>
                <option value = "Druzinska">Družinska</option>
                <option value = "Turisticna">Turistična</option>
                <option value = "Studijska">Študijska</option>
                </select>
                <label>Tip vizuma</label>
        </div>

        <h5>Podatki o prestopu</h5>
        <div class="input-field col s6">
                <input id="namen" name = "namen" type="text" class="validate">
                <label for="namen">Namen</label>
            </div>
        
        <div class="input-field col s6">
                <input id="datumP" name = "datumP" placeholder = "YYYY-DD-MM" maxlength = 10 type="text" class="validate">
                <label for="datumP">Datum prestopa</label>
        </div>

        <div class="input-field col s6">
                <select name = "mejniPrehod">
                <option value = "0">Letališče ljubljana</option>
                <option value = "1">Dragonja</option>
                <option value = "2">Bregana</option>
                <option value = "3">Sečovlje</option>
                <option value = "4">Obrežje</option>
                <option value = "5">Luka Koper</option>
                <option value = "6">Letališče Portorož</option>
                <option value = "7">Letališče Maribor</option>
                <option value = "8">Babno Polje</option>
                <option value = "9">Ormož</option>
                <option value = "10">Metlika</option>
                <option value = "11">Sočerga</option>
                <option value = "12">Rigonce</option>
                </select>
                <label>Mejni prehod</label>
        </div>

        <div class="input-field col s12">
            <input type="submit" value="Dodaj" class="btn waves-effect waves-light" />
        </div>

        </div>
</form>


</body>
