//importo la classe Utente per poter utilizzare i metodi e gli attributi
const utente = require("./Utente.js");

//classe Utenti
class Utenti {

    //coastruttore
    constructor() {
        this.listaUtenti = Array();
    }

    //metodi
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

//esportare la classe
module.exports = Utenti;