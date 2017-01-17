% rebase('osnova.tpl')



<body bgcolor = "#dcedc8">
  <div class="container">
    <h2>Rezultati iskanja</h2>           
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
          %for j in range(int(len(podatki.split("_"))) // 7):
              <tr>
                  %for x in range(7):
                      %y = podatki.split("_")[i]
                      <td>{{y}}</td>
                      %i+=1
                  %end
              </tr>

          %end
        
        
      </tbody>
    </table>
    
  </div>

</body>