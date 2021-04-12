const utente = require("./Utente.js");

class Utenti {

    constructor() {
        this.listaUtenti = Array();
    }

    aggiungi(tempUtente) {
        this.listaUtenti.push(tempUtente);
    }

    getStampa() {
        return this.listaUtenti;
    }
}

module.exports = Utenti;