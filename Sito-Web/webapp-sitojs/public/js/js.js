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
        //----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------
    controllaPremi() {
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
        if (this.flagEsistenzaPremio == true) {
            let pulsante = document.getElementById("cerchioRiscatta");
            pulsante.removeEventListener("click", RiscattaPremioNuovo);
            pulsante.addEventListener("click", RiscattaPremioNuovo);
        }
        /*this.ambo = false;
        this.terna = false;
        this.quaterna = false;
        this.cinquina = false;
        this.tombola = false;
        this.premi = [
            [],
            [],
            []
        ];
        let contaflagRighe = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ];
        let schedine = this.getSchedine();
        for (let iPremio = 0; iPremio < schedine.length; iPremio++) {

            let RigheColonne = schedine[iPremio].getRigheColonne();
            for (let iColonna = 0; iColonna < RigheColonne[0].length; iColonna++) {
                if (RigheColonne[0][iColonna].getStato() == true) {
                    contaflagRighe[iPremio][0] += 1;
                }
            }
            for (let iColonna = 0; iColonna < RigheColonne[1].length; iColonna++) {
                if (RigheColonne[1][iColonna].getStato() == true) {
                    contaflagRighe[iPremio][1] += 1;
                }
            }
            for (let iColonna = 0; iColonna < RigheColonne[2].length; iColonna++) {
                if (RigheColonne[2][iColonna].getStato() == true) {
                    contaflagRighe[iPremio][2] += 1;
                }
            }
        }
        for (let iPremio = 0; iPremio < contaflagRighe.length; iPremio++) {
            for (let iRigaPremio = 0; iRigaPremio < contaflagRighe[iPremio].length; iRigaPremio++) {
                switch (contaflagRighe[iPremio][iRigaPremio]) {
                    case 2:
                        this.ambo = true;
                        this.premi[iPremio][iRigaPremio] = "Ambo nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 3:
                        this.terna = true;
                        this.premi[iPremio][iRigaPremio] = "Terna nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 4:
                        this.quaterna = true;
                        this.premi[iPremio][iRigaPremio] = "Quaterna nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 5:
                        this.cinquina = true;
                        this.premi[iPremio][iRigaPremio] = "Cinquina nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                }
            }
        }
        if (this.flagEsistenzaPremio == true) {
            let pulsante = document.getElementById("cerchioRiscatta");
            pulsante.style.display = "block";
        }
        */
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
// let pulsante = document.getElementById("cerchioRiscatta");
// pulsante.addEventListener("click", function() {
//     giocatori.forEach(giocatoreTemporaneo => {
//         if (giocatoreTemporaneo.getPremi() != null) {
//             giocatoreTemporaneo.getPremi().forEach(premio => {
//                 if (premio != "") {
//                     alert(premio);
//                 }
//             })
//         }
//     })
// });
tombolaGlobale = true;
amboGlobale = true;
ternaGlobale = true;
quaternaGlobale = true;
cinquinaGlobale = true;
var nGiocatoreAttuale = 0;
var ambo = true;
var nSchedine = 6;
var nGiocatori = 4;
var username = "Giocatore 1";
var giocatori = [];

function cambiaGiocatore(movimento) {
    document.getElementById(nGiocatoreAttuale + "_0").style.display = "none";
    document.getElementById("contenitore_" + nGiocatoreAttuale + "_1").style.display = "none";
    document.getElementById((nGiocatoreAttuale + movimento) + "_0").style.display = "inline-block";
    document.getElementById("contenitore_" + (nGiocatoreAttuale + movimento) + "_1").style.display = "inline-block";
    document.getElementById("usernameSchedaGiocatore").innerHTML = giocatori[(nGiocatoreAttuale + movimento)].getNome();
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


function avviaGioco() {
    var tavoloSchedine = document.getElementById("tavoloSchedine");
    var contenitoreSchedine = document.getElementById("0_0");
    giocatori = [];
    document.getElementById("usernameSchedaGiocatore").innerHTML = username;
    while (contenitoreSchedine.firstChild) {
        contenitoreSchedine.removeChild(contenitoreSchedine.firstChild);
    }
    var contenitoreSchedine2 = document.getElementById("contenitore_0_1");
    while (contenitoreSchedine2.firstChild) {
        contenitoreSchedine2.removeChild(contenitoreSchedine2.firstChild);
    }

    for (let i = 0; i < nGiocatori; i++) {
        let giocatoreTemp;
        if (i == 0) {
            giocatoreTemp = new Giocatore(username, nSchedine);
        } else {
            giocatoreTemp = new Giocatore("CPU_" + i, nSchedine);
        }
        for (let iSchedine = 0; iSchedine < nSchedine; iSchedine++) {
            let schedinaTemp = generaNumeriSchedina();
            oggettoScedina = new Schedina(iSchedine, schedinaTemp);
            giocatoreTemp.aggiungiSchedina(oggettoScedina);
        }
        giocatori.push(giocatoreTemp);
        //----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------

    }
    for (let i = 0; i < 1; i++) {
        let schedineGiocatore = giocatori[i].getSchedine();
        for (let i2 = 0; i2 < (giocatori[i].getNumeroSchedine() - Math.floor(giocatori[i].getNumeroSchedine() / 2)); i2++) {
            let schedina = document.createElement("div");
            schedina.className = "schedina";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);

                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);

            contenitoreSchedine.appendChild(schedina);
        }

        /////////////////////////////////////////////////////////////////////////////////////////

        for (let i2 = (giocatori[i].getNumeroSchedine() - Math.floor(giocatori[i].getNumeroSchedine() / 2)); i2 < giocatori[i].getNumeroSchedine(); i2++) {
            let schedina = document.createElement("div");
            schedina.className = "schedina";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
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
        contenitoreSchedine1Giocatore.className = "contenitoreSchedine";
        let contenitoreSchedine2Giocatore = document.createElement("div");
        contenitoreSchedine2Giocatore.id = "contenitore_" + i + "_1";
        contenitoreSchedine2Giocatore.className = "contenitoreSchedine contenitoreSchedineDestra";
        let schedineGiocatore = giocatori[i].getSchedine();
        for (let i2 = 0; i2 < (giocatori[i].getNumeroSchedine() - Math.floor(giocatori[i].getNumeroSchedine() / 2)); i2++) {
            let schedina = document.createElement("div");
            schedina.className = "schedina";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);

            contenitoreSchedine1Giocatore.appendChild(schedina);
        }

        /////////////////////////////////////////////////////////////////////////////////////////

        for (let i2 = (giocatori[i].getNumeroSchedine() - Math.floor(giocatori[i].getNumeroSchedine() / 2)); i2 < giocatori[i].getNumeroSchedine(); i2++) {
            let schedina = document.createElement("div");
            schedina.className = "schedina";
            schedina.id = i + "_" + i2;
            let riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_0_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_0_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[0][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_1_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[1][i3].getNumero();
                } else {
                    cella.innerHTML = "&nbsp";
                }
                riga.appendChild(cella);
            }
            schedina.appendChild(riga);
            riga = document.createElement("div");
            for (i3 = 0; i3 < 9; i3++) {
                let coperchio = document.createElement("div");
                coperchio.className = "coperchio";
                coperchio.id = "coperchio_" + i + "_" + i2 + "_2_" + i3;
                coperchio.innerHTML = "&nbsp";
                riga.appendChild(coperchio);
            }
            schedina.appendChild(riga);
            for (i3 = 0; i3 < 9; i3++) {
                let cella = document.createElement("div");
                cella.className = "cellaSchedina";
                cella.id = i + "_" + i2 + "_2_" + i3;
                cella.addEventListener("click", function() {
                    posizioneCoperchio(this);
                });
                if (giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero() != "") {
                    cella.innerHTML = giocatori[i].getSchedine()[i2].getRigheColonne()[2][i3].getNumero();
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






    var tabellone = document.getElementById("tabellone");
    if (tabellone.className != "creato") {
        //INIZIO TABELLONE
        var tabellone = document.getElementById("tabellone");
        tabellone.className = "creato";
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
    }
}
//----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------


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

function posizioneCoperchio(div) {
    //----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------
    //----------------------coperchio.id = "coperchio_" + i + "_" + i2 + "_1_" + i3;-----------------------------------------------
    if (div.innerHTML != "&nbsp;") {
        let idCoperchio = "coperchio_" + div.id;
        let coperchio = document.getElementById(idCoperchio);
        var posizioni = div.id.split("_"); //posizioni tiene conto di tutte le posizioni rappresentate dall'ID

        coperchio.style.transform = "translateY(24px)";
        coperchio.style.transition = "250ms";
        giocatori[posizioni[0]].getSchedine()[posizioni[1]].getRigheColonne()[posizioni[2]][posizioni[3]].setStato(true);
    }

    console.log(giocatori[0]);
    giocatori[0].controllaPremi();
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

function RiscattaPremioNuovo() {
    if (giocatori[0].getTombola().getRiscattato() == true && tombolaGlobale == true) {
        tombolaGlobale = false;
        let schermataLog = document.getElementById("log");
        schermataLog.innerHTML = schermataLog.innerHTML + "TOMBOLA nella schedina " + giocatori[0].getCinquina().getSchedina() + "<br>";
        finePartita(0);
    } else if (tombolaGlobale == true) {
        if (giocatori[0].getCinquina().getRiscattato() == true && cinquinaGlobale == true) {
            cinquinaGlobale = false;
            let schermataLog = document.getElementById("log");
            schermataLog.innerHTML = schermataLog.innerHTML + "Cinquina nella schedina " + giocatori[0].getCinquina().getSchedina() + " in riga " + giocatori[0].getCinquina().getRiga() + "<br>";
        } else if (giocatori[0].getQuaterna().getRiscattato() == true && quaternaGlobale == true) {
            quaternaGlobale = false;
            let schermataLog = document.getElementById("log");
            schermataLog.innerHTML = schermataLog.innerHTML + "Quaterna nella schedina " + giocatori[0].getQuaterna().getSchedina() + " in riga " + giocatori[0].getQuaterna().getRiga() + "<br>";
        } else if (giocatori[0].getTerna().getRiscattato() == true && ternaGlobale == true) {
            ternaGlobale = false;
            let schermataLog = document.getElementById("log");
            schermataLog.innerHTML = schermataLog.innerHTML + "Terna nella schedina " + giocatori[0].getTerna().getSchedina() + " in riga " + giocatori[0].getTerna().getRiga() + "<br>";
        } else if (giocatori[0].getAmbo().getRiscattato() == true && amboGlobale == true) {
            amboGlobale = false;
            let schermataLog = document.getElementById("log");
            schermataLog.innerHTML = schermataLog.innerHTML + "Ambo nella schedina " + giocatori[0].getAmbo().getSchedina() + " in riga " + giocatori[0].getAmbo().getRiga() + "<br>";
        }
    }







}
function finePartita(nGiocatore){
    if(nGiocatore == 0){
        let finestraFinePartita = document.getElementById("finePartita");
        document.getElementById("esito").innerHTML = "VITTORIA";
        document.getElementById("stringaVincitore").innerHTML = giocatori[nGiocatore].getNome() + " ha vinto!";
        finestraFinePartita.style.display="block";
    }else{
        let finestraFinePartita = document.getElementById("finePartita");
        document.getElementById("esito").innerHTML = "SCONFITTA";
        finestraFinePartita.style.display="block";
    }
}

//script menu iniziali

function apriGioco() {
    salvaImpostazioni();
    document.getElementById("blockmenu").style.display = "none";
    document.getElementById("tombolone").style.display = "block";
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

function chiudiMenu() {
    document.getElementById("mainMenu").style.display = "block";
    document.getElementById("menuImpostazioni").style.display = "none";
}
function chiudiMenuESalva() {
    document.getElementById("mainMenu").style.display = "block";
    document.getElementById("menuImpostazioni").style.display = "none";
}

function chiudiPrePartita() {
    document.getElementById("menuPrePartita").style.display = "none";
    document.getElementById("mainMenu").style.display = "block";
}