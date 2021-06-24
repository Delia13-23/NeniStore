var can1;
var ctx1;
function inicio(){
	can1 = document.getElementById("imagen-canvas");
	ctx1 = can1.getContext("2d");
	imagen();
}
function imagen(){
  // Crear objeto imagen y cargar una fotografía
  var foto = new Image();
  foto.src = './img/pixeles.jpg';
  // Desplegar la foto
	foto.addEventListener('load', function() {
    ctx1.drawImage(foto, 0, 0);

    var imagenData = ctx1.getImageData(0, 0, 400, 400); 
		for (var i = 0; i < imagenData.data.length; i += 4) {
      var iluminacion = parseInt((imagenData.data[i]+imagenData.data[i+1]+imagenData.data[i+2])/3)
      imagenData.data[i]     = iluminacion;     // red
      imagenData.data[i + 1] = iluminacion; // green
      imagenData.data[i + 2] = iluminacion; // blue
    
    }
    ctx1.putImageData(imagenData, 400, 0);
		
	}, false);
}
	
addEventListener("DOMContentLoaded", inicio, false);