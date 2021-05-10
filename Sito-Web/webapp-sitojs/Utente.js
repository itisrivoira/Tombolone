class Utente {

    constructor(nome, cognome, dataNascita, nazionalita, mail, username, password, confermaPassword) {
        this.nome = nome;
        this.cognome = cognome;
        this.dataNascita = dataNascita;
        this.nazionalita = nazionalita;
        this.mail = mail;
        this.username = username;
        this.password = password;
        this.confermaPassword = confermaPassword;
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

    getConfermaPassword() {
        return this.confermaPassword;
    }

    setConfermaPassword(confermaPassword) {
        this.confermaPassword = confermaPassword;
    }
}

module.exports = Utente;