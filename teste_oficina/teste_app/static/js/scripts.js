$(document).ready(function(){ /*ao abrir o documento(pagina) esta função sera executavel*/
        var searchBtn = $('#search-btn');   /*$ = atalho para jQuery = biblioteca de funções javascript que interagem com html*/
        var searchForm = $('#search-form'); /*$ = identificador valido de java script */

        

        $(searchBtn).on('click', function(){
            searchForm.submit();
        });

});