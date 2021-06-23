function comenzar(){
    var elemento=document.getElementById('lienzo');
    lienzo=elemento.getContext("2d");
    lienzo.shadowColor="rgba(0,0,0,0.5)"
    lienzo.shadowOffsetX=3;
    lienzo.shadowOffsetY=3;
    lienzo.shadwoBlur=5;
    lienzo.font="bold 36px verdana";
    lienzo.textAling="start";
    lienzo.textBaseline="top";
    lienzo.fillText("Novedades",300,150);
}

window.addEventListener("load",comenzar,false);
