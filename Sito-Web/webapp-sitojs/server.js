//importo le classi
const utente = require("./Utente.js");
const utenti = require("./Utenti.js");
const Utente = require("./Utente.js");
const Utenti = require("./Utenti.js");
const nVittorie = require("./UtenteClassifica.js");
const Database = require("./database.js");
//importo i moduli
let express = require("express");
let app = express();
let bodyparser = require("body-parser");
let jsdom = require("jsdom");
let fs = require("fs");
const { json } = require("body-parser");
const { response } = require("express");
let mysql = require("mysql");

//creo le istanze per poter usare le classi
var giocatore = new Utente();
var giocatori = new Utenti();
var database = new Database();
var flag = false;

let { JSDOM } = jsdom;

//ascolto il server
app.listen("3000", function() {
    console.log("SERVER CONNESSO");
});

app.use(bodyparser.json());
app.use(bodyparser.urlencoded());

app.use(express.static("public"))

//end-point per la gestione di tutte le pagine del sito
//HOME
app.get("/", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "index.html");
    } else {
        res.sendFile(__dirname + "/html/index.html");
    }
});

//GIOCO
app.get("/regole", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "regole.html");
    } else {
        res.sendFile(__dirname + "/html/regole.html");
    }
});

//DOWNLOAD
app.get("/download", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "download.html");
    } else {
        res.sendFile(__dirname + "/html/download.html");
    }
});

//CLASSIFICA
app.get("/classifica", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        database.selectClassifica(function(giocatoriClassifica) {
            if (giocatoriClassifica.lenght == 0) {
                res.sendFile(__dirname + "/html/classifica.html");
            } else {
                let data = fs.readFileSync("./html/classifica.html");
                let mioJsdom = new JSDOM(data);
                let tagAccedi = mioJsdom.window.document.getElementById("Accedi");
                let messaggioAccedi = mioJsdom.window.document.getElementById("messaggioAccedi");
                messaggioAccedi.id = "";
                messaggioAccedi.innerHTML = "";
                tagAccedi.innerHTML = "Benvenuto " + giocatore.getUsername();
                let tagHumburger = mioJsdom.window.document.getElementById("AccediHumburger");
                tagHumburger.innerHTML = "Benvenuto " + giocatore.getUsername();
                let classifica = mioJsdom.window.document.getElementById("classifica");
                let i = 0;
                giocatoriClassifica.forEach(element => {
                    let tr = mioJsdom.window.document.createElement("tr");
                    if (i == 0) {
                        tr.style.backgroundColor = "yellow";
                    } else if (i == 1) {
                        tr.style.backgroundColor = "#c0c0c0";
                    } else if (i == 2) {
                        tr.style.backgroundColor = "#CD7F32";
                    }
                    let thPos = mioJsdom.window.document.createElement("th");
                    thPos.innerHTML = i + 1;
                    tr.appendChild(thPos);
                    let thUsername = mioJsdom.window.document.createElement("th");
                    thUsername.innerHTML = element.getNome();
                    tr.appendChild(thUsername);
                    let thVittorie = mioJsdom.window.document.createElement("th");
                    thVittorie.innerHTML = element.getnVittorie();
                    tr.appendChild(thVittorie);
                    classifica.appendChild(tr);
                    i += 1;
                });
                res.send(mioJsdom.window.document.documentElement.outerHTML);
            }
        });
    } else {
        let data = fs.readFileSync("./html/classifica.html");
        let mioJsdom = new JSDOM(data);
        let classifica = mioJsdom.window.document.getElementById("classifica");
        classifica.innerHTML = "";
        res.send(mioJsdom.window.document.documentElement.outerHTML);
    }
});

//STAFF
app.get("/staff", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "staff.html");
    } else {
        res.sendFile(__dirname + "/html/staff.html");
    }
});

//FAQ
app.get("/faq", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "faq.html");
    } else {
        res.sendFile(__dirname + "/html/faq.html");
    }
});

//WEBAPP
app.get("/webapp", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        let data = fs.readFileSync("./html/webapp.html");
        let mioJsdom = new JSDOM(data);
        let tagCrediti = mioJsdom.window.document.getElementById("nCreditiGiocatore");
        tagCrediti.innerHTML = giocatore.getnCrediti();
        res.send(mioJsdom.window.document.documentElement.outerHTML);
    } else {
        res.sendFile(__dirname + "/html/accedi.html");
    }
});

//FINE PARTITA
app.post("/terminaPartita", function(req, res, next) {
    let ngiocatori = req.body.ngiocatori;
    let nRound = req.body.nRound;
    let flagVinto = req.body.flagVinto;
    let nSchedine = req.body.nSchedine;
    let usernameUtente = req.body.usernameUtente;
    let crediti = req.body.creditiRimasti;
    database.insertFinePartita(nRound, ngiocatori, flagVinto, nSchedine, usernameUtente, giocatore, crediti, function(flag) {
        if (flag == true) {
            res.redirect("http://127.0.0.1:3000/webapp");
        } else {
            res.redirect("http://127.0.0.1:3000/");
        }
    });
});

//END-POINT PER SCARICARE GLI ZIP DELL'APP PYTHON
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

app.get("/zipGioco7", function(req, res, next) {
    res.sendFile(__dirname + "/zips/Tombolone_6.0.zip");
});

//FORM DI REGISTRAZIONE
app.get("/registrazione", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "index.html");
    } else {
        res.sendFile(__dirname + "/html/registrazione.html");
    }
});

//REGISTRAZIONE EFFETTUATA
app.post("/registrazioneEffettuata", function(req, res, next) {
    let tagPassword = req.body.password;
    let tagNome = req.body.nome;
    let tagCognome = req.body.cognome;
    let tagDataNascita = req.body.dataNascita;
    let tagNazionalita = req.body.nazionalita;
    let tagMail = req.body.indirizzoMail;
    let tagUsername = req.body.username;
    jsdomEndpointRegistrazione(req, res, "index.html", tagMail, tagNome, tagCognome, tagDataNascita, tagNazionalita, tagPassword, tagUsername);
});

//FORM DI ACCESSO
app.get("/accedi", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpointAreaPersonale(req, res, "areaPersonale.html");
    } else {
        res.sendFile(__dirname + "/html/accedi.html");
    }
});

//ACCESSO EFFETTUATO
app.post("/accessoEffettuato", function(req, res, next) {
    let mail = req.body.indirizzoMail;
    let password = req.body.password;
    jsdomEndpointAccedi(req, res, "index.html", mail, password);
});

//LOGOUT UTENTE
app.get("/logout", function(req, res, next) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
        jsdomEndpointLogout(req, res, "areaPersonale.html");
    } else {
        res.sendFile(__dirname + "index.html");
    }
});

//funzioni con database e jsdom
//per l'accesso
function jsdomEndpointAccedi(req, res, urlFile, mail, password) {
    database.selectUtente(mail, password, function(giocatoreTemp) {
        if (giocatoreTemp != null) {
            giocatore = giocatoreTemp;
            database.terminaConnessione();
            let data = fs.readFileSync("./html/" + urlFile);
            let mioJsdom = new JSDOM(data);
            let tagAccedi = mioJsdom.window.document.getElementById("Accedi");
            tagAccedi.innerHTML = "Benvenuto " + giocatore.getUsername();
            let tagHumburger = mioJsdom.window.document.getElementById("AccediHumburger");
            tagHumburger.innerHTML = "Benvenuto " + giocatore.getUsername();
            res.send(mioJsdom.window.document.documentElement.outerHTML);
        } else {
            let ritorno = fs.readFileSync("./html/accedi.html");
            res.send(ritorno.toString());
        }
    });
}

//per la registrazione
function jsdomEndpointRegistrazione(req, res, urlFile, tagMail, tagNome, tagCognome, tagDataNascita, tagNazionalita, tagPassword, tagUsername) {
    database.insertRegistrazione(tagMail, tagNome, tagCognome, tagDataNascita, tagNazionalita, tagPassword, tagUsername, function(flag) {
        if (flag == true) {
            database.terminaConnessione();
            giocatore = new Utente(tagMail, tagNome, tagCognome, tagDataNascita, tagNazionalita, tagPassword, tagUsername);
            jsdomEndpoint(req, res, "index.html");
        } else {
            res.sendFile(__dirname + "/html/registrazione.html");
        }
    });
}

//per il profilo utente
function jsdomEndpointAreaPersonale(req, res, urlFile) {
    let nome = giocatore.getNome();
    let cognome = giocatore.getCognome();
    let dataNascita = giocatore.getDataNascita();
    let nazionalita = giocatore.getNazionalita();
    let mail = giocatore.getMail();
    let username = giocatore.getUsername();
    let password = giocatore.getPassword();
    let data = fs.readFileSync("./html/" + urlFile);
    let mioJsdom = new JSDOM(data);
    let tagNome = mioJsdom.window.document.getElementById("nome1");
    let tagCognome = mioJsdom.window.document.getElementById("cognome1");
    let tagDataNascita = mioJsdom.window.document.getElementById("dataNascita1");
    let tagNazionalita = mioJsdom.window.document.getElementById("nazionalita1");
    let tagMail = mioJsdom.window.document.getElementById("mail1");
    let tagUsername = mioJsdom.window.document.getElementById("username1");
    let tagPassword = mioJsdom.window.document.getElementById("password1");
    let tagConfermaPassword = mioJsdom.window.document.getElementById("confermaPassword1");
    tagNome.innerHTML = nome;
    tagCognome.innerHTML = cognome;
    tagDataNascita.innerHTML = dataNascita.toDateString();
    tagNazionalita.innerHTML = nazionalita;
    tagMail.innerHTML = mail;
    tagUsername.innerHTML = username;
    tagPassword.innerHTML = "******"; //per maggiore sicurezza
    tagConfermaPassword.innerHTML = "******"; //per maggiore sicurezza
    res.send(mioJsdom.window.document.documentElement.outerHTML);
}

//funzione semplice con jsdom per una singola pagina
function jsdomEndpoint(req, res, urlFile) {
    let data = fs.readFileSync("./html/" + urlFile);
    let mioJsdom = new JSDOM(data);
    let tagAccedi = mioJsdom.window.document.getElementById("Accedi");
    tagAccedi.innerHTML = "Benvenuto " + giocatore.getUsername();
    let tagHumburger = mioJsdom.window.document.getElementById("AccediHumburger");
    tagHumburger.innerHTML = "Benvenuto " + giocatore.getUsername();
    res.send(mioJsdom.window.document.documentElement.outerHTML);
}


//per il logout dell'utente dal sito
function jsdomEndpointLogout(req, res, urlFile) {
    if (giocatore.getMail() != null && giocatore.getPassword() != null) {
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
        giocatore.setUsername(null);
        giocatore.setPassword(null);
        giocatore.setNome(null);
        giocatore.setCognome(null);
        giocatore.setDataNascita(null);
        giocatore.setNazionalita(null);
        giocatore.setMail(null);
        res.sendFile(__dirname + "/html/index.html");
    } else {
        res.sendFile(__dirname + "/html/index.html");
    }
}