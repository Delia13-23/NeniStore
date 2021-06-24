window.onload = function() {
    var canvas = document.getElementById("imagen-canvas");
    if(canvas && canvas.getContext){
       var ctx = canvas.getContext("2d");
       if(ctx){
           var srcImg = document.getElementById("resul");         
           ctx.drawImage(srcImg,0,0, ctx.canvas.width, ctx.canvas.height);
           var imgData = ctx.getImageData(0,0,ctx.canvas.width, ctx.canvas.height);
           var pixels = imgData.data;
           for(var i = 0; i <pixels.lenght; i+=4){
              // var luminosidad = parseInt((pixels[i]+pixels[i + 1]+pixels[i + 2])/3);
               pixels[i] = 255 - pixels[i]; // rojo
               pixels[i + 1] = 255 - pixels[i + 1]; // verde
               pixels[i + 2] = 255 - pixels[i + 2]; // azul
           }
           ctx.putImageData(imgData,0,0, 25, 25, 200, 182);
       }
    }

}