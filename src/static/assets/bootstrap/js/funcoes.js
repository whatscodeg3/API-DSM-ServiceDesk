function Avaliar(estrela) {
    var url = window.location;
    url = url.toString()
    url = url.split("../../../../templates/usuario-historico.html");
    url = url[0];
   
    var s1 = document.getElementById("s1").src;
    var s2 = document.getElementById("s2").src;
    var s3 = document.getElementById("s3").src;
    var s4 = document.getElementById("s4").src;
    var s5 = document.getElementById("s5").src;
   
   if (estrela == 5){ 
    if (s5 == url + "../static/img/star0.png") {
    document.getElementById("s1").src = "../static/img/star0.png";
    document.getElementById("s2").src = "../static/img/star0.png";
    document.getElementById("s3").src = "../static/img/star1.png";
    document.getElementById("s4").src = "../static/img/star1.png";
    document.getElementById("s5").src = "../static/img/star1.png";

    } else {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star1.png";
    document.getElementById("s3").src = "../static/img/star1.png";
    document.getElementById("s4").src = "../static/img/star1.png";
    document.getElementById("s5").src = "../static/img/star1.png";
   }}
    
    //ESTRELA 4
   if (estrela == 4){ 
    if (s4 == url + "img/star0.png") {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star1.png";
    document.getElementById("s3").src = "../static/img/star1.png";
    document.getElementById("s4").src = "../static/img/star1.png";
    document.getElementById("s5").src = "../static/img/star0.png";

    } else {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star1.png";
    document.getElementById("s3").src = "../static/img/star1.png";
    document.getElementById("s4").src = "../static/img/star1.png";
    document.getElementById("s5").src = "../static/img/star0.png";
   }}
   
   //ESTRELA 3
   if (estrela == 3){ 
    if (s3 == url + "img/star0.png") {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star1.png";
    document.getElementById("s3").src = "../static/img/star1.png";
    document.getElementById("s4").src = "../static/img/star0.png";
    document.getElementById("s5").src = "../static/img/star0.png";

    } else {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star1.png";
    document.getElementById("s3").src = "../static/img/star1.png";
    document.getElementById("s4").src = "../static/img/star0.png";
    document.getElementById("s5").src = "../static/img/star0.png";
   }}
    
   //ESTRELA 2
   if (estrela == 2){ 
    if (s2 == url + "img/star0.png") {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star1.png";
    document.getElementById("s3").src = "../static/img/star0.png";
    document.getElementById("s4").src = "../static/img/star0.png";
    document.getElementById("s5").src = "../static/img/star0.png";

    } else {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star1.png";
    document.getElementById("s3").src = "../static/img/star0.png";
    document.getElementById("s4").src = "../static/img/star0.png";
    document.getElementById("s5").src = "../static/img/star0.png";
   }}
    
    //ESTRELA 1
   if (estrela == 1){ 
    if (s1 == url + "img/star0.png") {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star0.png";
    document.getElementById("s3").src = "../static/img/star0.png";
    document.getElementById("s4").src = "../static/img/star0.png";
    document.getElementById("s5").src = "../static/img/star0.png";

    } else {
    document.getElementById("s1").src = "../static/img/star1.png";
    document.getElementById("s2").src = "../static/img/star0.png";
    document.getElementById("s3").src = "../static/img/star0.png";
    document.getElementById("s4").src = "../static/img/star0.png";
    document.getElementById("s5").src = "../static/img/star0.png";
   }}
    
    document.getElementById('rating').innerHTML;
    
   }
