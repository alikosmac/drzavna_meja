% rebase('osnova.tpl')

<body bgcolor = "#dcedc8">
<h2 class="center">Dodajanje Prestopa</h2>

<div class="container">          
    <table class="table table-hover">
      <thead>
        <tr>
          <th>Ime</th>
          <th>Primek</th>
          <th>Spol</th>
          <th>Naslov</th>
          <th>Država</th>
          <th>Datum rojstva</th>
          <th>Potni list</th>
        </tr>
      </thead>
      <tbody>
          %i = 0
          %for j in range(int(len(podatkiOseba.split("_"))) // 7):
              <tr>
                  %for x in range(7):
                      %y = podatkiOseba.split("_")[i]
                      <td>{{y}}</td>
                      %i+=1
                  %end
              </tr>

          %end
        
        
      </tbody>
    </table>
    
  </div>


<form action = "/preusmeri2">
    
        <h5>Podatki o prestopu</h5>
        <div class="input-field col s6">
                <input id="dokument" name = "dokument" type="text" value = {{dokument}} class="validate">
                <label for="dokument">Dokument</label>
        </div>

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
