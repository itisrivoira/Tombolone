class Utente {

    constructor(nome = null, cognome = null, dataNascita = null, nazionalita = null, mail = null, username = null, password = null) {
        this.nome = nome;
        this.cognome = cognome;
        this.dataNascita = dataNascita;
        this.nazionalita = nazionalita;
        this.mail = mail;
        this.username = username;
        this.password = password;
    }

    getNome() {
        return this.nome;
    }

    setNome(nome) {
        this.nome = nome;
    }

    getCognome() {
        return this.cognome;
    }

    setCognome(cognome) {
        this.cognome = cognome;
    }

    getDataNascita() {
        return this.dataNascita;
    }

    setDataNascita(dataNascita) {
        this.dataNascita = dataNascita;
    }

    getNazionalita() {
        return this.nazionalita;
    }

    setNazionalita(nazionalita) {
        this.nazionalita = nazionalita;
    }

    getMail() {
        return this.mail;
    }

    setMail(mail) {
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
}

module.exports = Utente;