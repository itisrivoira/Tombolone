const utente = require("./Utente.js");
const utenti = require("./Utenti.js");
let express = require("express");
let app = express();
let bodyparser = require("body-parser");
let jsdom = require("jsdom");
let fs = require("fs");
const Utente = require("./Utente.js");
const { json } = require("body-parser");
const { response } = require("express");

var giocatore = new Utente();
var listaGiocatori = Array();

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

app.get("/registrazione", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "index.html");
    } else {
        res.sendFile(__dirname + "/html/registrazione.html");
    }
});

app.get("/webapp", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "webapp.html");
    } else {
        res.sendFile(__dirname + "/html/webapp.html");
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
    res.sendFile(__dirname + "/zips/Tombolone_3.0.zip");
});

app.get("/accedi", function(req, res, next) {
    if (giocatore.getUsername() != null && giocatore.getPassword() != null) {
        jsdomEndpoint(req, res, "index.html");
    } else {
        res.sendFile(__dirname + "/html/accedi.html");
    }
});

app.post("/accessoEffettuato", function(req, res, next) {
    jsdomEndpointAccedi(req, res, "index.html");
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

function jsdomEndpoint(req, res, urlFile) {
    let data = fs.readFileSync("./html/" + urlFile);
    let mioJsdom = new JSDOM(data);
    let tagAccedi = mioJsdom.window.document.getElementById("Accedi");
    tagAccedi.innerHTML = "Benvenuto " + giocatore.getUsername();
    res.send(mioJsdom.window.document.documentElement.outerHTML);
}