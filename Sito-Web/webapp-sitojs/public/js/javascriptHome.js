/*Codice javascript necessario solamente per i collapsible, crea un array "coll" con tutti i collapsible a cui vengono aggiungti una funzione callback che mostra e nasconde i diversi testi*/
var coll = document.getElementsByClassName("collapsible");
var i;


for (i = 0; i < coll.length; i++) {
    /*Qui aggiunge il listener*/
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}

//inizio slides

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

//codice hamburger

//Codice js per il funzionamento della barra del volume
//var slider = document.getElementById("myRange");
//var output = document.getElementById("demo");
//output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
//slider.oninput = function() {
//    output.innerHTML = this.value;
//}

function mostraTitoliHamburger() {
    var x = document.getElementById("menuTendina");
    if (x.style.display == "none") {
        x.style.display = "inline-block";
        flagHamburger = true;
    } else {
        x.style.display = "none";
        flagHamburger = false;
    }
}

function apriMenu() {
    document.getElementById("mainMenu").style.display = "none";
    document.getElementById("menuImpostazioni").style.display = "block";
}

function chiudiMenu() {
    document.getElementById("mainMenu").style.display = "block";
    document.getElementById("menuImpostazioni").style.display = "none";
}

function validaCampi() {
    let mioForm = document.getElementById("mioForm");
    let flagCampiPieni = true;
    let tagInput = document.getElementsByTagName("input");
    let flagCampiUguali = false;
    let tagConfermaPassword = document.getElementById("confermaPassword1");
    let tagPassword = document.getElementById("password1");
    tagMail = document.getElementById("mail1");

    let flagChiocciola = false;
    let flagPunto = false;
    let flagOk = true;
    for (let i = 0; i < tagMail.length; i++) {
        if (tagMail[i] == "@" && flagChiocciola == false) {
            flagChiocciola = true;
        } else if (tagMail[i] == "@") {
            flagOk = false;
        }
        if (tagMail[i] == "." && flagChiocciola == true) {
            flagPunto = true;
        }
        if (flagPunto == false) {
            flagOk = false;
        }
    }
    if (flagChiocciola == true && flagPunto == true) {
        tagMail.style.border = " solid black 2px";
    } else {
        tagMail.style.border = " solid red 2px";
    }

    if (tagPassword.value == tagConfermaPassword.value) {
        flagCampiUguali = true;
    } else {
        flagCampiUguali = false;
        tagConfermaPassword.style.border = " solid red 2px";
        tagPassword.style.border = " solid red 2px";
    }

    for (let i = 0; i < (tagInput.length); i++) {
        if (tagInput[i].value == "") {
            flagCampiPieni = false;
            tagInput[i].style.border = " solid red 2px";
        } else {
            tagInput[i].style.border = " solid black 2px";
        }
    }
    if (tagInput[6].value != tagInput[7].value) {
        flagCampiPieni = false;
    }
    if (flagCampiPieni == true && flagCampiUguali == true && flagOk != false) {
        mioForm.submit();
    } else {}
}

function valida() {
    let mioForm = document.getElementsByClassName("myform")[0];
    let flagCampiPieni = true;
    let nome = document.getElementById("username");
    let password = document.getElementById("password");
    if (nome.value == "") {
        flagCampiPieni = false;
        nome.style.border = " solid red 2px";
    } else {
        nome.style.border = " solid black 2px";
    }
    if (password.value == "") {
        flagCampiPieni = false;
        password.style.border = " solid red 2px";
    } else {
        password.style.border = " solid black 2px";
    }
    if (flagCampiPieni == true) {
        mioForm.submit();
    } else {}
}