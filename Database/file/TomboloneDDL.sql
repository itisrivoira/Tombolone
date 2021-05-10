CREATE DATABASE Tombolone;
SHOW DATABASES;
USE Tombolone;
CREATE TABLE IF NOT EXISTS Utenti (
    mail VARCHAR(100) NOT NULL,
    PRIMARY KEY (mail),
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    dataNascita DATE NULL,
    nazionalita VARCHAR(50) NOT NULL,
    pswd VARCHAR(100) NOT NULL,
    usernameUtente CHAR(25) NOT NULL);
DESC Utenti;
CREATE TABLE IF NOT EXISTS Giocatori (
    usernameGiocatore VARCHAR(50) NOT NULL,
    PRIMARY KEY (username),
    puntiEsperienza INT(200) NOT NULL,
    nCrediti INT(200) NOT NULL,
    mailUtente VARCHAR(100) NOT NULL,
    FOREIGN KEY (mailUtente) REFERENCES Utenti (mail));
DESC Giocatori;
CREATE TABLE IF NOT EXISTS Partite (
    codicePartita CHAR(10) NOT NULL,
    PRIMARY KEY (codicePartita),
    data DATE NULL,
    nRound INT(200) NOT NULL,
    nGiocatori INT(6) NOT NULL);
DESC Partite;
SHOW TABLES;
exit;
