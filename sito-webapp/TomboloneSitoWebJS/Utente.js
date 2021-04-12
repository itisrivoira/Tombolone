class Utente {

    constructor(username = null, password = null, nome = null, cognome = null, dataNscita = null, nazionalita = null, mail = null) {
        this.username = username;
        this.password = password;
        this.nome = nome;
        this.cognome = cognome;
        this.dataNscita = dataNscita;
        this.nazionalita = nazionalita;
        this.mail = mail;
    }

    getUsername() {
        return this.username;
    }

    setUsername(username) {
        this.username = username;
    }

    getPassword() {
        return this.password;
    }

    setPassword(password) {
        this.password = password;
    }

    getNome() {
        return this.nome;
    }

    getCognome() {
        return this.cognome;
    }

    getDataNascita() {
        return this.dataNscita;
    }

    getNazionalita() {
        return this.nazionalita;
    }

    getMail() {
        return this.mail;
    }
}

module.exports = Utente;