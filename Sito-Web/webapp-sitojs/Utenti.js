const utente = require("./Utente.js");

class Utenti {

    constructor() {
        this.listaUtenti = Array();
    }

    aggiungi(Utente) {
        this.listaUtenti.push(Utente);
    }

    getListaUtenti() {
        return this.listaUtenti;
    }

    elimina(Utente) {
        this.listaUtenti.pop(Utente);
    }
}

module.exports = Utenti;