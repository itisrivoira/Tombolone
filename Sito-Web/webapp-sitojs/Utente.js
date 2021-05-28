//classe singolo Utente
class Utente {

    //costruttore
    constructor(mail, nome, cognome, dataNascita, nazionalita, password, username, nCrediti) {
        this.nome = nome;
        this.cognome = cognome;
        this.dataNascita = dataNascita;
        this.nazionalita = nazionalita;
        this.mail = mail;
        this.username = username;
        this.password = password;
        this.nCrediti = nCrediti;
    }

    //getter e setter
    setnCrediti(nCrediti) {
        this.nCrediti = nCrediti;
    }

    getnCrediti() {
        return this.nCrediti;
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

    getPassword() {
        return this.password;
    }

    setPassword(password) {
        this.password = password;
    }

    getUsername() {
        return this.username;
    }

    setUsername(username) {
        this.username = username;
    }
}

//esportare la classe
module.exports = Utente;