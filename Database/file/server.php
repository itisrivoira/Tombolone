<?php
$mysqli = new mysqli('localhost', 'root', '');//indirizzo server, utente, password
if($mysqli->connect_error){
	die('Errore connessione ('.$mysqli->connect_errno.') '.$mysqli->connect_error);
}//else{
	//echo "Connessione corretta";
//}

//cancello database
$mysqli->query("DROP DATABASE Tombolone");

//creo database
if(!$mysqli->query("CREATE DATABASE IF NOT EXISTS Tombolone")){
	echo "Errore creazione db: ".$mysqli->error."<BR>";
}

// Seleziono il database
$mysqli->query("USE Tombolone");

//Creazione tabella Utenti
if (!$mysqli->query("CREATE TABLE IF NOT EXISTS Utenti (
	mail VARCHAR(100) NOT NULL,
    PRIMARY KEY (mail),
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    dataNascita DATE NULL,
    nazionalita VARCHAR(50) NOT NULL,
    pswd VARCHAR(100) NOT NULL,
    usernameUtente CHAR(25) NOT NULL);")) {
    echo 'Errore di creazione tabella: '.$mysqli->error.'<BR>';
}

//Creazione tabella Giocatori
if (!$mysqli->query("CREATE TABLE IF NOT EXISTS Giocatori (
	usernameGiocatore VARCHAR(50) NOT NULL,
    PRIMARY KEY (username),
    puntiEsperienza INT(200) NOT NULL,
    nCrediti INT(200) NOT NULL,
    mailUtente VARCHAR(100) NOT NULL,
    FOREIGN KEY (mailUtente) REFERENCES Utenti (mail));")) {
    echo 'Errore di creazione tabella: '.$mysqli->error.'<BR>';
}

//Creazione tabella Partite
if (!$mysqli->query("CREATE TABLE IF NOT EXISTS Partite (
	codicePartita CHAR(10) NOT NULL,
    PRIMARY KEY (codicePartita),
    data DATE NULL,
    nRound INT(200) NOT NULL,
    nGiocatori INT(6) NOT NULL);")) {
    echo 'Errore di creazione tabella: '.$mysqli->error.'<BR>';
}

 // Normalmente questi valori sarebbero ottenuti tramite POST
$nome = '';
$cognome = '';
$mail = '';
$dataNascita = '';
$nazionalita = '';
$usernameU = '';
$password = hash('sha256', ''); //Creazione dell'hash
$query = "INSERT INTO Utenti (mail, nome, cognome, dataNascita, nazionalita, pswd, usernameUtente) VALUES ('$mail', '$nome', '$cognome', '$dataNascita', '$nazionalita', '$password', '$usernameU')";

// Esecuzione della query e controllo degli eventuali errori
if (!$mysqli->query($query)) {
    die('Errore di esecuzione insert into: '.$mysqli->error);
}

 // Normalmente questi valori sarebbero ottenuti tramite POST
$username = "";
$password = hash('sha256', "");
$rquery = $mysqli->query("SELECT * FROM Utenti WHERE Utenti.usernameUtente = '$username' AND Utenti.pswd = '$password'");

if($rquery->num_rows) {
    echo "<pre>"; // Il tag pre rende facilmente leggibile l'array
    print_r($rquery->fetch_all(MYSQLI_BOTH));
    echo "</pre>";
} else {
    echo "<pre>Accesso rifiutato</pre>";
}
?>
