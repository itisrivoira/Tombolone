//classe singolo Utente
class UtenteClassifica {

    //costruttore
    constructor(nome, nVittorie) {
        this.nome = nome;
        this.nVittorie = nVittorie;
    }

    //getter e setter
    setnVittorie(nVittorie) {
        this.nVittorie = nVittorie;
    }

    getnVittorie() {
        return this.nVittorie;
    }

    getNome() {
        return this.nome;
    }

    setNome(nome) {
        this.nome = nome;
    }
}

//esportare la classe
module.exports = UtenteClassifica;