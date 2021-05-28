//importo le classi
const Utente = require("./Utente.js");
const utente = require("./Utente.js");
//importo il modulo mysql per effettuare la connessione al database
let mysql = require("mysql");
var conn;

//classe database
class Database {

    //costruttore
    constructor(conn) {
        this.conn = conn;
    }

    //metodo per effettuare le insert all'interno del database
    insertRegistrazione(email, nome, cognome, dataNascita, nazionalita, pswd, username, callback) { //funzione callback
        conn = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: '',
            database: 'Tombolone'
        });
        conn.connect(() => {
            conn.query("insert into Utenti values(\"" + email + "\",\"" + username + "\",\"" + nome + "\",\"" + cognome + "\",\"" + dataNascita + "\",\"" + nazionalita + "\",\"" + pswd + "\",\"" + '500' + "\");", (err, result) => {
                if (err != null) {
                    callback(false);
                } else {
                    callback(true);
                }
            });
        });
    }

    //metodo per effettuare le interrogazioni al database alla fine della partita
    insertFinePartita(nRound, nGiocatori, flagVinto, nSchedine, usernameUtente, giocatore, nuoviCrediti, callback) {
        conn = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: '',
            database: 'Tombolone'
        });
        conn.connect(() => {
            conn.query("UPDATE Utenti SET nCrediti = '" + nuoviCrediti + "' WHERE Utenti.mail = '" + giocatore.getMail() + "' AND Utenti.usernameUtente = '" + giocatore.getUsername() + "';", (err, result) => {
                if (err != null) {
                    console.log("UPDATE Utenti: errore di inserimento");
                } else {
                    console.log("UPDATE Utenti: operazione completata");
                }
            });
        });
        conn.connect(() => {
            conn.query("insert into Partite values(\"" + Date.now() + "\",\"" + '2018-05-03' + "\",\"" + nRound + "\",\"" + nGiocatori + "\");", (err, result) => {
                if (err != null) {
                    console.log("INSERT Partite: errore di inserimento");
                } else {
                    console.log("INSERT Partite: operazione completata");
                }
            });
        });
        conn.connect(() => {
            conn.query("insert into Giocare values(\"" + flagVinto + "\",\"" + nSchedine + "\",\"" + giocatore.getUsername() + "\",\"" + Date.now() + "\");", (err, result) => {
                if (err != null) {
                    console.log("INSERT Giocare: errore di inserimento");
                    callback(false);
                } else {
                    console.log("INSERT Giocare: operazione completata");
                    callback(true);
                }
            });
        });
    }

    //metodo per selezionare un determinato Utente nel database
    selectUtente(mail, password, callback) {
        let giocatoreLoggato = null;
        let nome;
        let cognome;
        let dataNascita;
        let nazionalita;
        let username;
        let nCrediti;
        conn = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: '',
            database: 'Tombolone'
        });
        conn.connect(() => {
            let risultato = "select Utenti.* from Utenti where Utenti.mail ='" + mail + "' and Utenti.pswd ='" + password + "';";
            conn.query(risultato, (err, result) => {
                if (result.length == 0) {
                    callback(null);
                } else {
                    result.forEach(element => {
                        mail = element.mail;
                        password = element.pswd;
                        nome = element.nome;
                        cognome = element.cognome;
                        dataNascita = element.dataNascita;
                        nazionalita = element.nazionalita;
                        username = element.usernameUtente;
                        nCrediti = element.nCrediti;
                    });
                    giocatoreLoggato = new Utente(mail, nome, cognome, dataNascita, nazionalita, password, username, nCrediti);
                    callback(giocatoreLoggato);
                }
            });
        });
    }

    //metodo per temrinare la connessione
    terminaConnessione() {
        conn.end;
    }
}

//importo la classe
module.exports = Database;