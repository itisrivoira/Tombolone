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
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value;
}

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

