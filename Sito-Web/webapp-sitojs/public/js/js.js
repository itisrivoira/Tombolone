var classeSchedina = "schedinaChiara";
numeriDisponibili = [];
for (let i = 1; i <= 90; i++) {
    numeriDisponibili[i - 1] = i;
}
class PremioRiscattato {
    constructor() {
        this.riscattato = false;
        this.schedina;
        this.riga;
    }
    setRiscattato(val) {
        this.riscattato = val;
    }

    getRiscattato() {
        return this.riscattato;
    }
    getSchedina() {
        return this.schedina;
    }
    getRiga() {
        return this.riga;
    }
    setSchedina(nSchedina) {
        this.schedina = nSchedina;
    }
    setRiga(nRiga) {
        this.riga = nRiga;
    }
}
class Giocatori {
    constructor() {
        this.giocatori = [];
        this.arrayTombola = []; //array che tengono gli indici dei vincitori del determinato premio
        this.arrayCinquina = [];
        this.arrayQuaterna = [];
        this.arrayTerna = [];
        this.arrayAmbo = [];
    }

    aggiungiArrayTombola() {
        this.arrayTombola.push(posizione);
    }
    aggiungiArrayCinquina() {
        this.arrayCinquina.push(posizione);
    }
    aggiungiArrayQuaterna() {
        this.arrayQuaterna.push(posizione);
    }
    aggiungiArrayTerna(posizione) {
        this.arrayTerna.push(posizione);
    }
    aggiungiArrayAmbo() {
        this.arrayAmbo.push(posizione);
    }

    getArrayAmbo() {
        return this.arrayAmbo;
    }
    getArrayTerna() {
        return this.arrayTerna;
    }
    getArrayQuaterna() {
        return this.arrayQuaterna;
    }
    getArrayCinquina() {
        return this.arrayCinquina;
    }
    getArrayTombola() {
        return this.arrayTombola;
    }

    getGiocatori() {
        return this.giocatori;
    }

    riscattaPremi() { //fa impostare alle CPU i premi che potrebbero vincere
        for (let i = 1; i < this.giocatori.length; i++) {
            this.giocatori[i].riscattaPremiCPU()
        }
    }
    mostraPremiRiscattati() { //imposta nell'array di tutti i giocatori le posizioni di chi ha vinto determinati premi
        if (this.arrayTombola.length == 0) {
            for (let i = 0; i < this.giocatori.length; i++) {
                if (this.giocatori[i].getTombola().getRiscattato() == true) {
                    this.arrayTombola.push(i);
                }
            }
        }
        if (this.arrayCinquina.length == 0) {
            for (let i = 0; i < this.giocatori.length; i++) {
                if (this.giocatori[i].getCinquina().getRiscattato() == true) {
                    this.arrayCinquina.push(i);
                }
            }
        }
        if (this.arrayQuaterna.length == 0) {
            for (let i = 0; i < this.giocatori.length; i++) {
                if (this.giocatori[i].getQuaterna().getRiscattato() == true) {
                    this.arrayQuaterna.push(i);
                }
            }
        }
        if (this.arrayTerna.length == 0) {
            for (let i = 0; i < this.giocatori.length; i++) {
                if (this.giocatori[i].getTerna().getRiscattato() == true) {
                    this.arrayTerna.push(i);
                }
            }
        }
        if (this.arrayAmbo.length == 0) {
            for (let i = 0; i < this.giocatori.length; i++) {
                if (this.giocatori[i].getAmbo().getRiscattato() == true) {
                    this.arrayAmbo.push(i);
                }
            }
        }

    }

    aggiungiGiocatore(giocatore) {
        this.giocatori.push(giocatore);
    }
}
class Giocatore {
    /*
    nome
    nSchedine
    array schedine
    */
    constructor(nome, numeroSchedine) {
        this.nome = nome;
        this.numeroSchedine = numeroSchedine;
        this.schedine = [];
        this.flagEsistenzaPremio = false;
        this.ambo = new PremioRiscattato();
        this.terna = new PremioRiscattato();
        this.quaterna = new PremioRiscattato();
        this.cinquina = new PremioRiscattato();
        this.tombola = new PremioRiscattato();
        this.punti = 0;
    }
    setPunti(puntiAddizionali) {
        this.punti += puntiAddizionali;
    }
    getPunti() {
        return this.punti;
    }
    getNome() {
        return this.nome;
    }
    getNumeroSchedine() {
        return this.numeroSchedine;
    }
    getSchedine() {
        return this.schedine;
    }
    getTombola() {
        return this.tombola;
    }
    getAmbo() {
        return this.ambo;
    }
    getTerna() {
        return this.terna;
    }
    getQuaterna() {
        return this.quaterna;
    }
    getCinquina() {
        return this.cinquina;
    }

    aggiungiSchedina(schedina) {
        this.schedine.push(schedina);

    }
    riscattaPremiCPU() {
        //metodo riservato alle CPU
        let contaflagRighe = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ];
        for (let i = 0; i < this.getSchedine().length; i++) {
            let schedina = this.getSchedine()[i];
            let RigheColonne = schedina.getRigheColonne();
            for (let iColonna = 0; iColonna < RigheColonne[0].length; iColonna++) {
                if (RigheColonne[0][iColonna].getStato() == true && !(numeriDisponibili.includes(RigheColonne[0][iColonna].getNumero()))) {
                    contaflagRighe[i][0] += 1;
                }
            }
            for (let iColonna = 0; iColonna < RigheColonne[1].length; iColonna++) {
                if (RigheColonne[1][iColonna].getStato() == true && !(numeriDisponibili.includes(RigheColonne[1][iColonna].getNumero()))) {
                    contaflagRighe[i][1] += 1;
                }
            }
            for (let iColonna = 0; iColonna < RigheColonne[2].length; iColonna++) {
                if (RigheColonne[2][iColonna].getStato() == true && !(numeriDisponibili.includes(RigheColonne[2][iColonna].getNumero()))) {
                    contaflagRighe[i][2] += 1;
                }
            }
        }
        for (let iPremio = 0; iPremio < contaflagRighe.length; iPremio++) {
            if (contaflagRighe[iPremio][0] == 5 && contaflagRighe[iPremio][1] == 5 && contaflagRighe[iPremio][2] == 5) {
                this.tombola.setRiscattato(true);
            }
            for (let iRigaPremio = 0; iRigaPremio < contaflagRighe[iPremio].length; iRigaPremio++) {
                switch (contaflagRighe[iPremio][iRigaPremio]) {
                    case 2:
                        this.ambo.setRiscattato(true);
                        this.ambo.setSchedina(iPremio);
                        this.ambo.setRiga(iRigaPremio);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 3:
                        this.terna.setRiscattato(true);
                        this.terna.setSchedina(iPremio);
                        this.terna.setRiga(iRigaPremio);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 4:
                        this.quaterna.setRiscattato(true);
                        this.quaterna.setSchedina(iPremio);
                        this.quaterna.setRiga(iRigaPremio);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 5:
                        this.cinquina.setRiscattato(true);
                        this.cinquina.setSchedina(iPremio);
                        this.cinquina.setRiga(iRigaPremio);
                        this.flagEsistenzaPremio = true;
                        break;
                }
            }
        }
    }
    controllaPremi() {
        this.flagEsistenzaPremio = false;
        //metodo riservato al giocatore singolo
        this.ambo = new PremioRiscattato();
        this.terna = new PremioRiscattato();
        this.quaterna = new PremioRiscattato();
        this.cinquina = new PremioRiscattato();
        this.tombola = new PremioRiscattato();
        let contaflagRighe = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ];
        for (let i = 0; i < this.getSchedine().length; i++) {
            let schedina = this.getSchedine()[i];
            let RigheColonne = schedina.getRigheColonne();
            for (let iColonna = 0; iColonna < RigheColonne[0].length; iColonna++) {
                if (RigheColonne[0][iColonna].getStato() == true && !(numeriDisponibili.includes(RigheColonne[0][iColonna].getNumero()))) {
                    contaflagRighe[i][0] += 1;
                }
            }
            for (let iColonna = 0; iColonna < RigheColonne[1].length; iColonna++) {
                if (RigheColonne[1][iColonna].getStato() == true && !(numeriDisponibili.includes(RigheColonne[1][iColonna].getNumero()))) {
                    contaflagRighe[i][1] += 1;
                }
            }
            for (let iColonna = 0; iColonna < RigheColonne[2].length; iColonna++) {
                if (RigheColonne[2][iColonna].getStato() == true && !(numeriDisponibili.includes(RigheColonne[2][iColonna].getNumero()))) {
                    contaflagRighe[i][2] += 1;
                }
            }
        }
        for (let iPremio = 0; iPremio < contaflagRighe.length; iPremio++) {
            if (contaflagRighe[iPremio][0] == 5 && contaflagRighe[iPremio][1] == 5 && contaflagRighe[iPremio][2] == 5) {
                document.getElementById("tombola").className = "blink_me premioCentro";
                document.getElementById("ambo").className = "premioSinistra";
                document.getElementById("terna").className = "premioSinistra";
                document.getElementById("quaterna").className = "premioDestra";
                document.getElementById("cinquina").className = "premioDestra";
                document.getElementById("tombola").removeEventListener("click", function() { RiscattaPremioNuovo() });
                document.getElementById("ambo").removeEventListener("click", function() { RiscattaPremioNuovo() });
                document.getElementById("terna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                document.getElementById("quaterna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                document.getElementById("cinquina").removeEventListener("click", function() { RiscattaPremioNuovo() });
                document.getElementById("tombola").addEventListener("click", function() { RiscattaPremioNuovo(15) });
                //this.ambo.setRiscattato(true);
                this.tombola.setSchedina(iPremio);
                this.tombola.setRiga(iRigaPremio);
                this.flagEsistenzaPremio = true;
            }
            for (let iRigaPremio = 0; iRigaPremio < contaflagRighe[iPremio].length; iRigaPremio++) {
                switch (contaflagRighe[iPremio][iRigaPremio]) {
                    case 2:
                        if (amboGlobale == true) {
                            document.getElementById("ambo").className = "blink_me premioSinistra";
                            document.getElementById("terna").className = "premioSinistra";
                            document.getElementById("quaterna").className = "premioDestra";
                            document.getElementById("cinquina").className = "premioDestra";
                            document.getElementById("ambo").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("terna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("quaterna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("cinquina").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("ambo").addEventListener("click", function() { RiscattaPremioNuovo(2) });
                            //this.ambo.setRiscattato(true);
                            this.ambo.setSchedina(iPremio);
                            this.ambo.setRiga(iRigaPremio);
                            this.flagEsistenzaPremio = true;
                        }
                        break;
                    case 3:
                        if (ternaGlobale == true) {
                            document.getElementById("ambo").className = "premioSinistra";
                            document.getElementById("terna").className = "blink_me premioSinistra";
                            document.getElementById("quaterna").className = "premioDestra";
                            document.getElementById("cinquina").className = "premioDestra";
                            document.getElementById("ambo").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("terna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("quaterna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("cinquina").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("terna").addEventListener("click", function() { RiscattaPremioNuovo(3) });
                            //this.terna.setRiscattato(true);
                            this.terna.setSchedina(iPremio);
                            this.terna.setRiga(iRigaPremio);
                            this.flagEsistenzaPremio = true;
                        }
                        break;
                    case 4:
                        if (quaternaGlobale == true) {
                            document.getElementById("ambo").className = "premioSinistra";
                            document.getElementById("terna").className = "premioSinistra";
                            document.getElementById("quaterna").className = " blink_me premioDestra";
                            document.getElementById("cinquina").className = "premioDestra";
                            document.getElementById("ambo").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("terna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("quaterna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("cinquina").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("quaterna").addEventListener("click", function() { RiscattaPremioNuovo(4) });
                            //this.quaterna.setRiscattato(true);
                            this.quaterna.setSchedina(iPremio);
                            this.quaterna.setRiga(iRigaPremio);
                            this.flagEsistenzaPremio = true;
                        }
                        break;
                    case 5:
                        if (cinquinaGlobale == true) {
                            document.getElementById("ambo").className = "premioSinistra";
                            document.getElementById("terna").className = "premioSinistra";
                            document.getElementById("quaterna").className = "premioDestra";
                            document.getElementById("cinquina").className = "blink_me premioDestra";
                            document.getElementById("ambo").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("terna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("quaterna").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("cinquina").removeEventListener("click", function() { RiscattaPremioNuovo() });
                            document.getElementById("cinquina").addEventListener("click", function() { RiscattaPremioNuovo(5) });
                            //this.cinquina.setRiscattato(true);
                            this.cinquina.setSchedina(iPremio);
                            this.cinquina.setRiga(iRigaPremio);
                            this.flagEsistenzaPremio = true;
                        }
                        break;
                }
            }
        }
        if (this.flagEsistenzaPremio != true) {
            document.getElementById("ambo").className = "premioSinistra";
            document.getElementById("terna").className = "premioSinistra";
            document.getElementById("quaterna").className = "premioDestra";
            document.getElementById("cinquina").className = "premioDestra";
            // let pulsante = document.getElementById("cerchioRiscatta");
            // pulsante.removeEventListener("click", RiscattaPremioNuovo);
            // pulsante.addEventListener("click", RiscattaPremioNuovo);
        }
    }
}
class Schedina {

    constructor(codice, righe) {
        this.codice = codice;
        this.righe = righe;
    }

    getCodice() {
        return this.codice;
    }

    getRigheColonne() {
        return this.righe;
    }
}
class Numero {
    constructor(numero, stato) {
        this.numero = numero;
        this.stato = stato;
    }
    getNumero() {
        return this.numero;
    }
    getStato() {
        return this.stato;
    }
    setNumero(newNumero) {
        this.numero = newNumero;
    }

    setStato(newStato) {
        this.stato = newStato;
    }
}


tombolaGlobale = true;
amboGlobale = true;
ternaGlobale = true;
quaternaGlobale = true;
cinquinaGlobale = true;
var nGiocatoreAttuale = 0;
var ambo = true;
var nSchedine;
var nGiocatori = null;
var username = "Giocatore 1";
var giocatori = new Giocatori();

function cambiaGiocatore(movimento) {
    document.getElementById(nGiocatoreAttuale + "_0").style.display = "none";
    document.getElementById("contenitore_" + nGiocatoreAttuale + "_1").style.display = "none";
    document.getElementById((nGiocatoreAttuale + movimento) + "_0").style.display = "inline-block";
    document.getElementById("contenitore_" + (nGiocatoreAttuale + movimento) + "_1").style.display = "inline-block";
    document.getElementById("usernameSchedaGiocatore").innerHTML = giocatori.getGiocatori()[(nGiocatoreAttuale + movimento)].getNome();
    nGiocatoreAttuale += movimento;
    if (nGiocatoreAttuale == 0) {
        document.getElementById("frecciaIndietro").style.display = "none";
    } else {
        document.getElementById("frecciaIndietro").style.display = "inline-block";
    }
    if (nGiocatoreAttuale == (nGiocatori - 1)) {
        document.getElementById("frecciaAvanti").style.display = "none";
    } else {
        document.getElementById("frecciaAvanti").style.display = "inline-block";
    }
}

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

function avviaGioco() {
    document.getElementById("ambo").style.backgroundColor = "greenyellow";
    document.getElementById("ambo").style.color = "black";
    document.getElementById("terna").style.backgroundColor = "greenyellow";
    document.getElementById("terna").style.color = "black";
    document.getElementById("quaterna").style.backgroundColor = "greenyellow";
    document.getElementById("quaterna").style.color = "black";
    document.getElementById("cinquina").style.backgroundColor = "greenyellow";
    document.getElementById("cinquina").style.color = "black";
    document.getElementById("tombola").style.backgroundColor = "greenyellow";
    document.getElementById("tombola").style.color = "black";
    console.log(document.getElementById("tavoloSchedine"));
    document.getElementById("pulsanteEstrai").style.backgroundColor = "orange";
    giocatori = new Giocatori();
    let nomiDisponibili = ["Giulio", "Alberto", "Morena", "Mattia", "Daniele", "Eric", "Francesco", "Riccardo", "Lorenzo", "Alessandro", "Andrea", "Gabriele", "Simone", "Kledi", "Flavian", "Qiyan", "Kevin", "Lorenzo", "Alessandro", "Stefano", "Francesco"];
    document.getElementById("nGiocatoriPronti").innerHTML = "Giocatori pronti:0/" + nGiocatori;
    document.getElementById("log").innerHTML = "Partita iniziata: <br>";
    document.getElementById("pulsanteEstrai").removeEventListener("click", estraiNumero);
    document.getElementById("pulsanteEstrai").addEventListener("click", estraiNumero);


    var tabellone = document.getElementById("tabellone");
    while (tabellone.firstChild) {
        tabellone.removeChild(tabellone.firstChild);
    }
    var tavoloSchedine = document.getElementById("tavoloSchedine");
    var contenitoreSchedine = document.getElementById("0_0");
    document.getElementById("usernameSchedaGiocatore").innerHTML = username;
    while (contenitoreSchedine.firstChild) {
        contenitoreSchedine.removeChild(contenitoreSchedine.firstChild);
    }
    var contenitoreSchedine2 = document.getElementById("contenitore_0_1");
    while (contenitoreSchedine2.firstChild) {
        contenitoreSchedine2.removeChild(contenitoreSchedine2.firstChild);
    }

    for (let i = 1; i < nGiocatori; i++) {
        if (document.getElementById(i + "_0") != null && document.getElementById(i + "_1") != null) {
            let element = document.getElementById(i + "_0");
            element.remove();
            element = document.getElementById("contenitore_" + i + "_1");
            element.remove();
            // let cont1 = document.getElementById(i + "_0");
            // while (cont1.firstChild) {
            //     cont1.removeChild(cont1.firstChild);
            // }
            // let cont2 = document.getElementById("contenitore_" + i + "_1");
            // while (cont2.firstChild) {
            //     alert("fatto");
            //     cont2.removeChild(cont2.firstChild);
            // }
        }
    }
    for (let i = 0; i < nGiocatori; i++) {
        let giocatoreTemp;
        if (i == 0) {
            giocatoreTemp = new Giocatore(username, nSchedine);
        } else {
            let nome = nomiDisponibili[Math.floor(Math.random() * nomiDisponibili.length)];
            giocatoreTemp = new Giocatore(nome, Math.ceil(Math.random() * 5 + 1));
            let index = nomiDisponibili.indexOf(nome);
            nomiDisponibili.splice(index, 1);
        }
        for (let iSchedine = 0; iSchedine < giocatoreTemp.getNumeroSchedine(); iSchedine++) {
            let schedinaTemp = generaNumeriSchedina();
            oggettoScedina = new Schedina(iSchedine, schedinaTemp);
            giocatoreTemp.aggiungiSchedina(oggettoScedina);
        }
        giocatori.aggiungiGiocatore(giocatoreTemp);
        //----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------

    }
    for (let i = 0; i < 1; i++) {
        let schedineGiocatore = giocatori.getGiocatori()[i].getSchedine();
        for (let i2 = 0; i2 < (giocatori.getGiocatori()[i].getNumeroSchedine() - Math.floor(giocatori.getGiocatori()[i].getNumeroSchedine() / 2)); i2++) {
            let schedina = document.createElement("div");
            schedina.className = classeSchedina + " col";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                coperchio.addEventListener("click", function() {
                    posizioneCoperchioCoperto(this);
                });
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);

                });
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                coperchio.addEventListener("click", function() {
                    posizioneCoperchioCoperto(this);
                });
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                coperchio.addEventListener("click", function() {
                    posizioneCoperchioCoperto(this);
                });
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);

            contenitoreSchedine.appendChild(schedina);
        }

        /////////////////////////////////////////////////////////////////////////////////////////

        for (let i2 = (giocatori.getGiocatori()[i].getNumeroSchedine() - Math.floor(giocatori.getGiocatori()[i].getNumeroSchedine() / 2)); i2 < giocatori.getGiocatori()[i].getNumeroSchedine(); i2++) {
            let schedina = document.createElement("div");
            schedina.className = classeSchedina + " col";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                coperchio.addEventListener("click", function() {
                    posizioneCoperchioCoperto(this);
                });
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);

                });
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                coperchio.addEventListener("click", function() {
                    posizioneCoperchioCoperto(this);
                });
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                coperchio.addEventListener("click", function() {
                    posizioneCoperchioCoperto(this);
                });
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            contenitoreSchedine2.appendChild(schedina);
        }

    }
    for (let i = 1; i < nGiocatori; i++) {
        let contenitoreSchedine1Giocatore = document.createElement("div");
        contenitoreSchedine1Giocatore.id = i + "_0";
        contenitoreSchedine1Giocatore.className = "contenitoreSchedine col-6";
        let contenitoreSchedine2Giocatore = document.createElement("div");
        contenitoreSchedine2Giocatore.id = "contenitore_" + i + "_1";
        contenitoreSchedine2Giocatore.className = "contenitoreSchedineDestra col-6";
        let schedineGiocatore = giocatori.getGiocatori()[i].getSchedine();
        for (let i2 = 0; i2 < (giocatori.getGiocatori()[i].getNumeroSchedine() - Math.floor(giocatori.getGiocatori()[i].getNumeroSchedine() / 2)); i2++) {
            let schedina = document.createElement("div");
            schedina.className = classeSchedina + " col";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);

            contenitoreSchedine1Giocatore.appendChild(schedina);

        }

        /////////////////////////////////////////////////////////////////////////////////////////

        for (let i2 = (giocatori.getGiocatori()[i].getNumeroSchedine() - Math.floor(giocatori.getGiocatori()[i].getNumeroSchedine() / 2)); i2 < giocatori.getGiocatori()[i].getNumeroSchedine(); i2++) {
            let schedina = document.createElement("div");
            schedina.className = classeSchedina + " col";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            riga.className = "rigaCoperchio";
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = null;
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                if (giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);

            contenitoreSchedine2Giocatore.appendChild(schedina);
        }
        contenitoreSchedine1Giocatore.style.display = "none";
        contenitoreSchedine2Giocatore.style.display = "none";
        tavoloSchedine.appendChild(contenitoreSchedine1Giocatore);
        tavoloSchedine.appendChild(contenitoreSchedine2Giocatore);
    }



    //INIZIO TABELLONE
    var tabellone = document.getElementById("tabellone");
    var rigaTabellone = document.createElement("div");
    rigaTabellone.className = "rigaTabellone";
    for (let i2 = 1; i2 < 10; i2++) {
        let cellaTab = document.createElement("div");
        cellaTab.id = "cella_" + 0 + "_" + i2;
        cellaTab.className = "cellaTabellone";
        cellaTab.innerHTML = i2;
        rigaTabellone.appendChild(cellaTab);
    }
    let cellaTab = document.createElement("div");
    cellaTab.id = "cella_0_10";
    cellaTab.className = "cellaTabellone";
    cellaTab.innerHTML = 10;
    rigaTabellone.appendChild(cellaTab);
    tabellone.appendChild(rigaTabellone);
    for (let i = 1; i < 8; i++) {
        rigaTabellone = document.createElement("div");
        rigaTabellone.className = "rigaTabellone";
        for (let i2 = 1; i2 <= 10; i2++) {
            let cellaTab = document.createElement("div");
            cellaTab.id = "cella_" + i + "_" + i2;
            cellaTab.className = "cellaTabellone";
            cellaTab.innerHTML = ((i * 10) + i2);
            rigaTabellone.appendChild(cellaTab);
        }
        tabellone.appendChild(rigaTabellone);
    }
    var rigaTabellone = document.createElement("div");
    rigaTabellone.className = "rigaTabellone";
    for (let i2 = 1; i2 <= 10; i2++) {
        let cellaTab = document.createElement("div");
        cellaTab.id = "cella_" + 8 + "_" + i2;
        cellaTab.className = "cellaTabellone";
        cellaTab.innerHTML = ((8 * 10) + i2);
        rigaTabellone.appendChild(cellaTab);
    }
    tabellone.appendChild(rigaTabellone);

    creaClassifica();
}
//----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------

function terminaTurno() {

    console.log(giocatori);
    document.getElementById("pulsanteEstrai").removeEventListener("click", function() { estraiNumero() });
    document.getElementById("pulsanteEstrai").addEventListener("click", estraiNumero);
    document.getElementById("pulsanteEstrai").style.backgroundColor = "orange";
    giocatori.mostraPremiRiscattati();
    let arrayTombola = giocatori.getArrayTombola();
    let schermataLog = document.getElementById("log");
    if (tombolaGlobale == true && giocatori.getArrayTombola().length > 0) {
        for (let i = 0; i < giocatori.getArrayTombola().length; i++) {
            giocatori.getGiocatori()[arrayTombola[i]].setPunti(15);
        }
        finePartita(giocatori.getArrayTombola());
    } else {
        if (amboGlobale == true) {
            let arrayAmboTemp = giocatori.getArrayAmbo();
            if (arrayAmboTemp.length > 0) {
                for (let i = 0; i < arrayAmboTemp.length; i++) {
                    schermataLog.innerHTML = schermataLog.innerHTML + giocatori.getGiocatori()[arrayAmboTemp[i]].getNome() + " ha fatto ambo " + " <br> "
                    amboGlobale = false;
                    giocatori.getGiocatori()[arrayAmboTemp[i]].setPunti(2);
                    document.getElementById("ambo").className = "premioSinistra";
                    document.getElementById("ambo").style.backgroundColor = "black";
                    document.getElementById("ambo").style.color = "grey";
                }
            }
        }
        if (ternaGlobale == true) {
            let arrayTernaTemp = giocatori.getArrayTerna();
            if (arrayTernaTemp.length > 0) {
                for (let i = 0; i < arrayTernaTemp.length; i++) {
                    schermataLog.innerHTML = schermataLog.innerHTML + giocatori.getGiocatori()[arrayTernaTemp[i]].getNome() + " ha fatto terna " + " <br> "
                    ternaGlobale = false;
                    giocatori.getGiocatori()[arrayTernaTemp[i]].setPunti(3);
                    document.getElementById("terna").className = "premioSinistra";
                    document.getElementById("terna").style.backgroundColor = "black";
                    document.getElementById("terna").style.color = "grey";
                }
            }
        }
        if (quaternaGlobale == true) {
            let arrayQuaternaTemp = giocatori.getArrayQuaterna();
            if (arrayQuaternaTemp.length > 0) {
                for (let i = 0; i < arrayQuaternaTemp.length; i++) {
                    schermataLog.innerHTML = schermataLog.innerHTML + giocatori.getGiocatori()[arrayQuaternaTemp[i]].getNome() + " ha fatto quaterna " + " <br> "
                    quaternaGlobale = false;
                    giocatori.getGiocatori()[arrayQuaternaTemp[i]].setPunti(4);
                    document.getElementById("quaterna").className = "premioDestra";
                    document.getElementById("quaterna").style.backgroundColor = "black";
                    document.getElementById("quaterna").style.color = "grey";
                }
            }
        }
        if (cinquinaGlobale == true) {
            let arrayCinquinaTemp = giocatori.getArrayCinquina();
            if (arrayCinquinaTemp.length > 0) {
                for (let i = 0; i < arrayCinquinaTemp.length; i++) {
                    schermataLog.innerHTML = schermataLog.innerHTML + giocatori.getGiocatori()[arrayCinquinaTemp[i]].getNome() + " ha fatto cinquina " + " <br>"
                    cinquinaGlobale = false;
                    giocatori.getGiocatori()[arrayCinquinaTemp[i]].setPunti(5);
                    document.getElementById("cinquina").className = "premioDestra";
                    document.getElementById("cinquina").style.backgroundColor = "black";
                    document.getElementById("cinquina").style.color = "grey";
                }
            }
        }
        aggiornaTabellaTempoReale();
    }
}


function aggiornaTabellaTempoReale() {
    let listaPunti = [];
    let punteggi = [];
    for (let i = 0; i < nGiocatori; i++) {
        listaPunti[i] = [giocatori.getGiocatori()[i].getNome(), giocatori.getGiocatori()[i].getPunti()];
        punteggi.push(giocatori.getGiocatori()[i].getPunti());

    }
    punteggi = punteggi.filter(function(item, pos) {
        return punteggi.indexOf(item) == pos;
    })
    punteggi.sort(function(a, b) { return b - a });
    let utentiOrdinatiPunti = [];
    for (let i = 0; i < punteggi.length; i++) {
        for (let i2 = 0; i2 < listaPunti.length; i2++) {
            if (listaPunti[i2][1] == punteggi[i]) {
                utentiOrdinatiPunti.push(listaPunti[i2]);
            }
        }
    }
    for (let i = 0; i < utentiOrdinatiPunti.length; i++) {
        document.getElementById("classifica_nome_" + i).innerHTML = utentiOrdinatiPunti[i][0];
        document.getElementById("classifica_punti_" + i).innerHTML = utentiOrdinatiPunti[i][1];
    }
}


function creaClassifica() {


    let clasificaDinamica = document.getElementById("classificaTempoReale");
    // for (var i = 0; i < clasificaDinamica.rows.length; i++) {
    //     clasificaDinamica.removeChild(i);
    // }

    while (clasificaDinamica.firstChild) {
        clasificaDinamica.removeChild(clasificaDinamica.firstChild);
    }

    let rigaClassifica = document.createElement("tr");
    //aggiungo posizione
    let cellaClassifica = document.createElement("th");
    cellaClassifica.innerHTML = "POSIZIONE";
    rigaClassifica.appendChild(cellaClassifica);
    //aggiungo nome
    cellaClassifica = document.createElement("th");
    cellaClassifica.innerHTML = "NOME";
    rigaClassifica.appendChild(cellaClassifica);
    //aggiungo punti
    cellaClassifica = document.createElement("th");
    cellaClassifica.innerHTML = "PUNTI";
    rigaClassifica.appendChild(cellaClassifica);
    clasificaDinamica.appendChild(rigaClassifica);
    //creazione classifica dinamica
    for (let i = 0; i < giocatori.getGiocatori().length; i++) {
        let rigaClassifica = document.createElement("tr");
        //aggiungo posizione
        let cellaClassifica = document.createElement("th");
        cellaClassifica.id = "classifica_posizione_" + i;
        cellaClassifica.innerHTML = (i + 1);
        rigaClassifica.appendChild(cellaClassifica);
        //aggiungo nome
        cellaClassifica = document.createElement("th");
        cellaClassifica.id = "classifica_nome_" + i;
        cellaClassifica.innerHTML = giocatori.getGiocatori()[i].getNome();
        rigaClassifica.appendChild(cellaClassifica);
        //aggiungo punti
        cellaClassifica = document.createElement("th");
        cellaClassifica.id = "classifica_punti_" + i;
        cellaClassifica.innerHTML = 0;
        rigaClassifica.appendChild(cellaClassifica);
        clasificaDinamica.appendChild(rigaClassifica);
    }
    //fine creazione classifica dinamica
}

function generaNumeriSchedina() {
    let matriceSchedina = [];
    let flagSchedinaOk = false;
    while (flagSchedinaOk == false) {
        var numeriDisponibili = []; //array da dove estrarre
        for (let i = 1; i <= 90; i++) {

            numeriDisponibili.push(i);
        }
        var numeriSicuri = [];
        let numeri = []; //array con tutti i numeri non ancora sotto forma di matrice

        var row0 = [];
        var row1 = [];
        var row2 = [];
        let numeroCasuale;

        for (let i = 1; i <= 9; i++) {
            numeroCasuale = Math.round(Math.random() * (i * 10) + (i * 10 - 10));
            while (numeroCasuale < (i * 10 - 10) || numeroCasuale > (i * 10)) {
                numeroCasuale = Math.round(Math.random() * (i * 10) + (i * 10 - 10));
            }
            numeriSicuri[i - 1] = numeroCasuale;
        }
        var numMaxCol = Array(9); //contatore con massimo 2 numeri che conta le 9 colonne
        var numeriSupplementari = [];
        let duplicato = true;
        for (let i = 0; i < 6; i++) {
            numeroCasuale = Math.round(Math.random() * 89 + 1);
            for (let iduplicato = 0; iduplicato < numeriSicuri.length; iduplicato++) {
                if (numeriSicuri[iduplicato] == numeroCasuale) {
                    duplicato = false;
                }
            }
            for (let iduplicato = 0; iduplicato < numeriSupplementari.length; iduplicato++) {
                if (numeriSupplementari[iduplicato] == numeroCasuale) {
                    duplicato = false;
                }
            }
            while (numMaxCol[Math.floor(numeroCasuale / 10)] >= 2 || duplicato == false) {
                duplicato = true;
                numeroCasuale = Math.round(Math.random() * ((i * 10) - (i * 10 - 10)));
                for (let iduplicato = 0; iduplicato < numeriSicuri.length; iduplicato++) {
                    if (numeriSicuri[iduplicato] == numeroCasuale) {
                        duplicato = false;
                    }
                }
                for (let iduplicato = 0; iduplicato < numeriSupplementari.length; iduplicato++) {
                    if (numeriSupplementari[iduplicato] == numeroCasuale) {
                        duplicato = false;
                    }
                }
            }
            numeriSupplementari[i] = numeroCasuale;
            numMaxCol[Math.floor(numeroCasuale / 10)] += 1;
        }
        numeriSicuri = numeriSicuri.concat(numeriSupplementari);
        numeriSicuri.sort();
        // for (let i = 0; i <= 15; i++) {
        //     var numcas = numeriDisponibili[Math.floor(Math.random() * numeriDisponibili.length)];
        //     numeriSicuri.push(numcas);
        // }
        // numeriSicuri.sort();

        for (let i2 = 0; i2 < 3; i2++) {
            matriceSchedina[i2] = new Array(9);
            for (let i3 = 0; i3 < 9; i3++) {
                matriceSchedina[i2][i3] = new Numero("", false); //completa tutte le celle con un carattere vuoto in modo che riempa anche quelle bianche
            }
        }


        matriceSchedina = [];
        for (let i2 = 0; i2 < 3; i2++) {
            matriceSchedina[i2] = new Array(9);
            for (let i3 = 0; i3 < 9; i3++) {
                matriceSchedina[i2][i3] = new Numero("", false); //completa tutte le celle con un carattere vuoto in modo che riempa anche quelle bianche
            }
        }
        flagSchedinaOk = true;
        contatoriNumeriMaxRighe = [0, 0, 0];
        for (let i2 = 0; i2 < numeriSicuri.length; i2++) {
            array3 = [0, 1, 2]; //array con le posizioni da 
            // devono essere minori di 5
            let posizioneCasuale = array3[Math.trunc(Math.random() * array3.length)];
            while (contatoriNumeriMaxRighe[posizioneCasuale] == 5) {
                posizioneCasuale = array3[Math.trunc(Math.random() * array3.length)];
            }
            if (numeriSicuri[i2] != 90 && matriceSchedina[posizioneCasuale][Math.trunc(numeriSicuri[i2] / 10)].getNumero() == "") {
                matriceSchedina[posizioneCasuale][Math.trunc(numeriSicuri[i2] / 10)].setNumero(numeriSicuri[i2]);
                contatoriNumeriMaxRighe[posizioneCasuale] += 1;
            } else if (matriceSchedina[posizioneCasuale][8].getNumero() >= 80) {
                matriceSchedina[posizioneCasuale][8].setNumero(numeriSicuri[i2]);
                contatoriNumeriMaxRighe[posizioneCasuale] += 1;
            }
        }
        contaNumSchedina = 0;
        for (let i = 0; i < 3; i++) {
            for (let i2 = 0; i2 < 9; i2++) {
                if (matriceSchedina[i][i2].getNumero() != "") {
                    contaNumSchedina += 1;
                }
            }
            //alert(contaNumRiga);

        }
        if (contaNumSchedina != 15) {
            flagSchedinaOk = false;
        }
    }
    for (let i = 0; i < 9; i++) {
        let flagcolonnaOrdinata = false
        while (flagcolonnaOrdinata == false) {
            flagcolonnaOrdinata = true;
            for (let z = 2; z > 0; z--) {
                if (matriceSchedina[z][i].getNumero() < matriceSchedina[z - 1][i].getNumero() && matriceSchedina[z][i].getNumero() != "" && matriceSchedina[z - 1][i].getNumero() != "") {
                    let tempCella = matriceSchedina[z][i];
                    matriceSchedina[z][i] = matriceSchedina[z - 1][i];
                    matriceSchedina[z - 1][i] = tempCella;
                    flagcolonnaOrdinata = false;
                }
            }
        }
        if (matriceSchedina[2][i].getNumero() < matriceSchedina[0][i].getNumero() && matriceSchedina[2][i].getNumero() != "" && matriceSchedina[0][i].getNumero() != "") {
            let tempCella = matriceSchedina[2][i];
            matriceSchedina[2][i] = matriceSchedina[0][i];
            matriceSchedina[0][i] = tempCella;
        }
    }
    return matriceSchedina;
}


function estraiNumero() {
    document.getElementById("pulsanteEstrai").style.backgroundColor = "grey";
    document.getElementById("pulsanteEstrai").removeEventListener("click", estraiNumero);
    if (numeriDisponibili.length != 0) {
        let num = numeriDisponibili[Math.floor(Math.random() * numeriDisponibili.length)];
        document.getElementById("numeroEstratto").innerHTML = num;
        let index = numeriDisponibili.indexOf(num);
        numeriDisponibili.splice(index, 1);
        if (num % 10 == 0) {
            if (num != 10) {
                let cella = document.getElementById("cella_" + (Math.trunc(num / 10) - 1) + "_10");
                cella.style.backgroundColor = "red";
            } else {
                let cella = document.getElementById("cella_0_10");
                cella.style.backgroundColor = "red";
            }
        } else if (num != 10) {
            let cella = document.getElementById("cella_" + (Math.trunc(num / 10)) + "_" + (num - (Math.trunc(num / 10) * 10)));
            cella.style.backgroundColor = "red";
        }
    }
}

function controllaNumeriCPU() {
    for (let i = 1; i < nGiocatori; i++) {
        let tempoCPUSingola = Math.random() * 1000 + 250;
        //sleep(tempoCPUSingola / i);
        for (let i2 = 0; i2 < giocatori.getGiocatori()[i].getNumeroSchedine(); i2++) {
            for (let iColonna = 0; iColonna < 9; iColonna++) {
                for (let iRiga = 0; iRiga < 3; iRiga++) {
                    if (!numeriDisponibili.includes(giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[iRiga][iColonna].getNumero()) && giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[iRiga][iColonna].getNumero() != "") {
                        let idCoperchio = "coperchio_" + i + "_" + i2 + "_" + iRiga + "_" + iColonna;
                        let coperchio = document.getElementById(idCoperchio);
                        coperchio.style.transform = "translateY(1.5vw)";
                        coperchio.style.transition = "250ms";
                        giocatori.getGiocatori()[i].getSchedine()[i2].getRigheColonne()[iRiga][iColonna].setStato(true);
                    }
                }
            }
        }
        document.getElementById("nGiocatoriPronti").innerHTML = "Giocatori pronti:" + (i + 1) + "/" + nGiocatori;
    }
    giocatori.riscattaPremi();
    giocatori.mostraPremiRiscattati();
}

function posizioneCoperchioCoperto(div) {
    var posizioni = div.id.split("_");
    numGiocatore = posizioni[1];
    numSchedina = posizioni[2];
    numRigaSchedina = posizioni[3];
    numColonna = posizioni[4];
    posizioneNumeroSchedina = 0;
    if (giocatori.getGiocatori()[0].getSchedine()[numSchedina].getRigheColonne()[numRigaSchedina][numColonna].getStato() == true) {
        giocatori.getGiocatori()[0].getSchedine()[numSchedina].getRigheColonne()[numRigaSchedina][numColonna].setStato(false);
        div.style.transform = "translateY(0px)";
        div.style.transition = "250ms";
        giocatori.getGiocatori()[0].controllaPremi();
    }
}

function posizioneCoperchio(div) {
    //----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------
    //----------------------coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;-----------------------------------------------
    if (div.innerHTML != "&nbsp;") {

        let idCoperchio = "coperchio_" + div.id;
        let coperchio = document.getElementById(idCoperchio);
        var posizioni = div.id.split("_"); //posizioni tiene conto di tutte le posizioni rappresentate dall'ID

        coperchio.style.transform = "translateY(1.5vw)";
        coperchio.style.transition = "250ms";
        giocatori.getGiocatori()[posizioni[0]].getSchedine()[posizioni[1]].getRigheColonne()[posizioni[2]][posizioni[3]].setStato(true);
    }
    giocatori.getGiocatori()[0].controllaPremi();
}

function salvaImpostazioni() {

    nSchedine = parseInt(document.getElementById("Nschedine").value);
    nGiocatori = parseInt(document.getElementById("Ngiocatori").value);
    if (document.getElementById("username").value != "") {
        username = document.getElementById("username").value;
    } else {
        username = "Giocatore 1";
    }

}

function salvaImpostazioniSecondarie() {
    if (document.getElementById("chiaro").checked == true) {
        classeSchedina = "schedinaChiara";
    } else {
        classeSchedina = "schedinaScura";
    }
    audioGlobale = document.getElementById("volumeSiNo").checked;
    x.volume = (document.getElementById("myRange").value / 100);
}

function RiscattaPremioNuovo(num) {

    let pulsante = document.getElementById("cerchioRiscatta");
    pulsante.style.backgroundColor = "orange";
    pulsante.removeEventListener("click", inserisciPremioGiocatore);
    switch (num) {
        case 2:
            giocatori.getGiocatori()[0].getAmbo().setRiscattato(true);
            document.getElementById("cerchioRiscatta").className = "col-4 blink_me";
            document.getElementById("ambo").className = "premioSinistra";
            pulsante.addEventListener("click", function() {
                inserisciPremioGiocatore(2);
            })
            break;
        case 3:
            giocatori.getGiocatori()[0].getTerna().setRiscattato(true);
            document.getElementById("cerchioRiscatta").className = "col-4 blink_me";
            document.getElementById("terna").className = "premioSinistra";
            pulsante.addEventListener("click", function() {
                inserisciPremioGiocatore(3);
            })
            break;
        case 4:
            giocatori.getGiocatori()[0].getQuaterna().setRiscattato(true);
            document.getElementById("cerchioRiscatta").className = "col-4 blink_me";
            document.getElementById("quaterna").className = "premioDestra";
            pulsante.addEventListener("click", function() {
                inserisciPremioGiocatore(4);
            })
            break;
        case 5:
            giocatori.getGiocatori()[0].getCinquina().setRiscattato(true);
            document.getElementById("cerchioRiscatta").className = "col-4 blink_me";
            document.getElementById("cinquina").className = "premioDestra";
            pulsante.addEventListener("click", function() {
                inserisciPremioGiocatore(5);
            })
            break;
        case 15:
            giocatori.getGiocatori()[0].getTombola().setRiscattato(true);
            document.getElementById("cerchioRiscatta").className = "col-4 blink_me";
            document.getElementById("tombola").className = "premioCentro";
            pulsante.addEventListener("click", function() {
                inserisciPremioGiocatore(15);
            })

            break;
    }

}

function inserisciPremioGiocatore(premio) {
    document.getElementById("cerchioRiscatta").className = "col-4";
    switch (premio) {
        case 2:
            giocatori.aggiungiArrayAmbo(0);
            break;
        case 3:
            giocatori.aggiungiArrayTerna(0);
            break;
        case 4:
            giocatori.aggiungiArrayQuaterna(0);
            break;
        case 5:
            giocatori.aggiungiArrayCinquina(0);
            break;
        case 15:
            giocatori.aggiungiArrayTombola(0);
            break;
    }
}

function finePartita(arrayGiocatori) {
    document.getElementById("pulsantePronto").removeEventListener("click", function() { terminaTurno });
    document.getElementById("pulsanteEstrai").removeEventListener("click", function() { estraiNumero });
    if (arrayGiocatori.includes(0)) {
        let finestraFinePartita = document.getElementById("finePartita");
        document.getElementById("esito").innerHTML = "VITTORIA";
        finestraFinePartita.style.display = "block";
    } else {
        let finestraFinePartita = document.getElementById("finePartita");
        document.getElementById("esito").innerHTML = "SCONFITTA";
        finestraFinePartita.style.display = "block";
    }
    if (arrayGiocatori.length == 1) {
        document.getElementById("stringaVincitore").innerHTML = giocatori.getGiocatori()[arrayGiocatori[0]].getNome() + " ha vinto!";
    } else {
        for (let i = 0; i < arrayGiocatori.length; i++) {
            document.getElementById("stringaVincitore").innerHTML = document.getElementById("stringaVincitore").innerHTML + giocatori.getGiocatori()[arrayGiocatori[i]].getNome() + " ha vinto!  <br> ";
        }
    }
    let tabellaRisultati = document.getElementById("tabellaRisulatatiFinali");
    let listaPunti = [];
    let punteggi = [];
    for (let i = 0; i < nGiocatori; i++) {
        listaPunti[i] = [giocatori.getGiocatori()[i].getNome(), giocatori.getGiocatori()[i].getPunti()];
        punteggi.push(giocatori.getGiocatori()[i].getPunti());

    }
    punteggi = punteggi.filter(function(item, pos) {
        return punteggi.indexOf(item) == pos;
    })
    punteggi.sort(function(a, b) { return b - a });
    let utentiOrdinatiPunti = [];
    for (let i = 0; i < punteggi.length; i++) {
        for (let i2 = 0; i2 < listaPunti.length; i2++) {
            if (listaPunti[i2][1] == punteggi[i]) {
                utentiOrdinatiPunti.push(listaPunti[i2]);
            }
        }
    }
    for (let i = 0; i < utentiOrdinatiPunti.length; i++) {
        let newRiga = document.createElement("tr");
        let newPosizione = document.createElement("th");
        newPosizione.innerHTML = (i + 1) + "°";
        let newNome = document.createElement("th");
        newNome.innerHTML = utentiOrdinatiPunti[i][0];
        let newPunti = document.createElement("th");
        newPunti.innerHTML = utentiOrdinatiPunti[i][1];
        newRiga.appendChild(newPosizione);
        newRiga.appendChild(newNome);
        newRiga.appendChild(newPunti);
        tabellaRisultati.appendChild(newRiga);
    }
}

//script menu iniziali

function apriGioco() {
    salvaImpostazioni();
    document.getElementById("blockmenu").style.display = "none";
    document.getElementById("tombolone").style.display = "block";
    document.getElementById("log").style.display = "block";
    avviaGioco();
}

function apriPrePartita() {
    document.getElementById("menuPrePartita").style.display = "inline-block";
    document.getElementById("tombolone").style.display = "none";
    document.getElementById("mainMenu").style.display = "none";
}

function chiudiGioco() {
    document.getElementById("blockmenu").style.display = "block";
    document.getElementById("mainMenu").style.display = "block";
    document.getElementById("tombolone").style.display = "none";
    document.getElementById("menuPrePartita").style.display = "none";
    document.getElementById("finePartita").style.display = "none";
    //IMPLEMENTARE SALVATAGGIO IMPOSTAZIONI

}

function apriMenu() {
    document.getElementById("mainMenu").style.display = "none";
    document.getElementById("menuImpostazioni").style.display = "block";
}


function chiudiMenuESalva() {
    document.getElementById("mainMenu").style.display = "block";
    document.getElementById("menuImpostazioni").style.display = "none";
}

function chiudiPrePartita() {
    document.getElementById("menuPrePartita").style.display = "none";
    document.getElementById("mainMenu").style.display = "block";
}