% rebase('osnova.tpl')
 

<body bgcolor = "#dcedc8">
<h2 class="center">Vpiši število dokumenta</h2>

<form action = '/preusmeri1'>
    
        <div class="input-field col s6">
                <input id="dokument" placeholder = "XX00000000" maxlength = 10 name = "dokument" type="text" class="validate">
                <label for="dokument">Številka dokumenta</label>
            </div>
        
        <div class="input-field col s12">
            <input type="submit" value="preveri" class="btn waves-effect waves-light" />
        </div>

        </div>
</form>


</body>
