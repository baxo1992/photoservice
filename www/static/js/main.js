var numer = 1;

var timer1 = 0;
var timer2 = 0;

function ustawslajd(nrslajdu)
{
    clearTimeout(timer1);
    clearTimeout(timer2);
    schowaj();
    numer = nrslajdu;
    setTimeout("zmienslajd()",500);
}

function schowaj()
{
    $("#slajder").fadeOut(500);
}

function zmienslajd()
{
    numer++; if (numer>5)numer=1;
    var plik = "<img src=\"/www/static/img/0"+numer+".jpg\"/>";
    document.getElementById("slajder").innerHTML = plik;
    $("#slajder").fadeIn(500);

    timer1 = setTimeout("zmienslajd()",5000);
    timer2 = setTimeout("schowaj()",4500);
}