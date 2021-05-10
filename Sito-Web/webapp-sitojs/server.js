const utente = require("./Utente.js");
const utenti = require("./Utenti.js");
let express = require("express");
let app = express();
let bodyparser = require("body-parser");
let jsdom = require("jsdom");
let fs = require("fs");
const Utente = require("./Utente.js");
const Utenti = require("./Utenti.js");
const { json } = require("body-parser");
const { response } = require("express");
let mysql = require("mysql");
//classe per il database = con metodi: per la connessione, un metodo per giascuna query di interrogazione

var giocatore = new Utente();
var giocatori = new Utenti();
var flag = false;

let { JSDOM } = jsdom;

app.listen("3000", function() {
    console.log("SERVER CONNESSO");
});

app.use(bodyparser.json());
app.use(bodyparser.urlencoded());

app.use(express.static("public"))

app.get("/", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "index.html");
    } else {
        res.sendFile(__dirname + "/html/index.html");
    }
});

app.get("/regole", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "regole.html");
    } else {
        res.sendFile(__dirname + "/html/regole.html");
    }
});

app.get("/download", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "download.html");
    } else {
        res.sendFile(__dirname + "/html/download.html");
    }
});

app.get("/classifica", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "classifica.html");
    } else {
        res.sendFile(__dirname + "/html/classifica.html");
    }
});

app.get("/staff", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "staff.html");
    } else {
        res.sendFile(__dirname + "/html/staff.html");
    }
});

app.get("/faq", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "faq.html");
    } else {
        res.sendFile(__dirname + "/html/faq.html");
    }
});

app.get("/webapp", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        res.sendFile(__dirname + "/html/webapp.html");
    } else {
        res.sendFile(__dirname + "/html/accedi.html");
    }
});

app.get("/zipGioco1", function(req, res, next) {
    res.sendFile(__dirname + "/zips/Tombolone_0.1.zip");
});

app.get("/zipGioco2", function(req, res, next) {
    res.sendFile(__dirname + "/zips/Tombolone_1.1.zip");
});

app.get("/zipGioco3", function(req, res, next) {
    res.sendFile(__dirname + "/zips/Tombolone_2.1.zip");
});

app.get("/zipGioco4", function(req, res, next) {
    res.sendFile(__dirname + "/zips/Tombolone_3.1.zip");
});

app.get("/zipGioco5", function(req, res, next) {
    res.sendFile(__dirname + "/zips/Tombolone_4.0.zip");
});

app.get("/zipGioco6", function(req, res, next) {
    res.sendFile(__dirname + "/zips/Tombolone_5.0.zip");
});

app.get("/registrazione", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "index.html");
    } else {
        res.sendFile(__dirname + "/html/registrazione.html");
    }
});

app.post("/registrazioneEffettuata", function(req, res, next) {
    jsdomEndpointRegistrazione(req, res, "index.html");
    next();
});

app.get("/accedi", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        res.sendFile(__dirname + "/html/areaPersonale.html");
    } else {
        res.sendFile(__dirname + "/html/accedi.html");
    }
});

app.post("/accessoEffettuato", function(req, res, next) {
    let nome = req.body.username;
    let password = req.body.password;
    giocatore.setUsername();
    giocatore.setPassword();
    /*let trovato = false;
    for (let i = 0; i < giocatori.getListaUtenti().length; i++) {
        if (giocatori.getListaUtenti()[i].getUsername() == nome && giocatori.getListaUtenti()[i].getPassword() == password) {
            trovato = true;
        }
    }
    if (trovato == true) {*/
    jsdomEndpointAccedi(req, res, "index.html");
    /*} else {
        res.sendFile(__dirname + "/html/accedi.html");
    }*/
    next();
});

app.get("/logout", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpointLogout(req, res, "areaPersonale.html");
    } else {
        res.sendFile(__dirname + "index.html");
    }
});

app.get("/salvaModifiche", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpointSalvaModifiche(req, res, "areaPersonale.html");
    } else {
        res.sendFile(__dirname + "index.html");
    }
});

function jsdomEndpointAccedi(req, res, urlFile) {
    let nome = req.body.username;
    let password = req.body.password;
    giocatore.setUsername(nome);
    giocatore.setPassword(password);
    let data = fs.readFileSync("./html/" + urlFile);
    let mioJsdom = new JSDOM(data);
    let tagAccedi = mioJsdom.window.document.getElementById("Accedi");
    tagAccedi.innerHTML = "Benvenuto " + giocatore.getUsername();
    res.send(mioJsdom.window.document.documentElement.outerHTML);
}

function jsdomEndpointRegistrazione(req, res, urlFile) {
    let tagConfermaPassword = req.body.confermaPassword;
    let tagPassword = req.body.password;
    let tagNome = req.body.nome;
    let tagCognome = req.body.cognome;
    let tagDataNascita = req.body.dataNascita;
    let tagNazionalita = req.body.nazionalita;
    let tagMail = req.body.indirizzoMail;
    let tagUsername = req.body.username;
    giocatore = new Utente(tagNome, tagCognome, tagDataNascita, tagNazionalita, tagMail, tagUsername, tagPassword, tagConfermaPassword);
    giocatori.aggiungi(giocatore);
    jsdomEndpoint(req, res, "index.html");
}

function jsdomEndpoint(req, res, urlFile) {
    let data = fs.readFileSync("./html/" + urlFile);
    let mioJsdom = new JSDOM(data);
    let tagAccedi = mioJsdom.window.document.getElementById("Accedi");
    tagAccedi.innerHTML = "Benvenuto " + giocatore.getUsername();
    res.send(mioJsdom.window.document.documentElement.outerHTML);
}

function jsdomEndpointLogout(req, res, urlFile) {
    let data = fs.readFileSync("./html/" + urlFile);
    let mioJsdom = new JSDOM(data);
    let tagMail = mioJsdom.window.document.getElementById("mail1");
    let tagUsername = mioJsdom.window.document.getElementById("username1");
    let tagNome = mioJsdom.window.document.getElementById("nome1");
    let tagCognome = mioJsdom.window.document.getElementById("cognome1");
    let tagDataNascita = mioJsdom.window.document.getElementById("dataNascita1");
    let tagNazionalita = mioJsdom.window.document.getElementById("nazionalita1");
    let tagPassword = mioJsdom.window.document.getElementById("password1");
    let tagConfermaPassword = mioJsdom.window.document.getElementById("confermaPassword1");
    tagMail.innerHTML = "";
    tagUsername.innerHTML = "";
    tagNome.innerHTML = "";
    tagCognome.innerHTML = "";
    tagDataNascita.innerHTML = "";
    tagNazionalita.innerHTML = "";
    tagPassword.innerHTML = "";
    tagConfermaPassword.innerHTML = "";
    let flag = false;
    for (let i = 0; i < giocatori.getListaUtenti().length; i++) {
        if (giocatori.getListaUtenti()[i].getUsername() == tagUsername && giocatori.getListaUtenti()[i].getPassword() == tagPassword) {
            flag = true
        }
    }
    if (flag == true) {
        giocatore.setUsername(null);
        giocatore.setPassword(null);
        giocatore.getNome();
        giocatore.setCognome();
        giocatore.setDataNascita();
        giocatore.setNazionalita();
        giocatore.setMail();
        giocatore.setConfermaPassword();
    }
    res.send(mioJsdom.window.document.documentElement.outerHTML);
    alert("Logout effettuato con successo");
    res.sendFile(__dirname + "/html/index.html");
}

function jsdomEndpointSalvaModifiche(req, res, urlFile) {
    let data = fs.readFileSync("./html/" + urlFile);
    let mioJsdom = new JSDOM(data);
    let tagMail = mioJsdom.window.document.getElementById("mail1");
    let tagUsername = mioJsdom.window.document.getElementById("username1");
    let tagNome = mioJsdom.window.document.getElementById("nome1");
    let tagCognome = mioJsdom.window.document.getElementById("cognome1");
    let tagDataNascita = mioJsdom.window.document.getElementById("dataNascita1");
    let tagNazionalita = mioJsdom.window.document.getElementById("nazionalita1");
    let tagPassword = mioJsdom.window.document.getElementById("password1");
    let tagConfermaPassword = mioJsdom.window.document.getElementById("confermaPassword1");
    giocatore.setMail(tagMail);
    giocatore.setUsername(tagUsername);
    giocatore.setNome(tagNome);
    giocatore.setCognome(tagCognome);
    giocatore.setDataNascita(tagDataNascita);
    giocatore.setNazionalita(tagNazionalita);
    giocatore.setPassword(tagPassword);
    giocatore.setConfermaPassword(tagConfermaPassword);
    tagMail.innerHTML = tagMail;
    tagUsername.innerHTML = tagUsername;
    tagNome.innerHTML = tagNome;
    tagCognome.innerHTML = tagCognome;
    tagDataNascita.innerHTML = tagDataNascita;
    tagNazionalita.innerHTML = tagNazionalita;
    tagPassword.innerHTML = tagPassword;
    tagConfermaPassword.innerHTML = tagConfermaPassword;
    res.send(mioJsdom.window.document.documentElement.outerHTML);
    alert("Modifiche salvate con successo");
    res.sendFile(__dirname + "/html/index.html");
}