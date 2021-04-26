const utente = require("./Utente.js");

class Utenti {

    constructor() {
        this.listaUtenti = Array();
    }

    aggiungi(Utente) {
        this.listaUtenti.push(Utente);
    }

    getStampa() {
        return this.listaUtenti;
    }
}

module.exports = Utenti;