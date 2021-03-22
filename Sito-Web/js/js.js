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
        this.premi = [];
        this.flagEsistenzaPremio = false;
    }

    getPremi() {
        return this.premi;
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

    aggiungiSchedina(schedina) {
            this.schedine.push(schedina);

        }
        //----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------
    controllaPremi() {
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
                        this.premi[iPremio][iRigaPremio] = "Ambo nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 3:
                        this.premi[iPremio][iRigaPremio] = "Terna nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 4:
                        this.premi[iPremio][iRigaPremio] = "Quaterna nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                    case 5:
                        this.premi[iPremio][iRigaPremio] = "Cinquina nella scheda " + (iPremio + 1) + ", in riga " + (iRigaPremio + 1);
                        this.flagEsistenzaPremio = true;
                        break;
                }
            }
        }
        if (this.flagEsistenzaPremio == true) {
            let pulsante = document.getElementById("bottonePremi");
            pulsante.style.display = "block";
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
let pulsante = document.getElementById("bottonePremi");
pulsante.addEventListener("click", function() {
    giocatori.forEach(giocatoreTemporaneo => {
        if (giocatoreTemporaneo.getPremi() != null) {
            giocatoreTemporaneo.getPremi().forEach(premio => {
                if (premio != "") {
                    alert(premio);
                }
            })
        }
    })
});





var nSchedine = 3;
var nGiocatori = 1;
var giocatori = [];
for (let i = 0; i < nGiocatori; i++) {
    let giocatoreTemp = new Giocatore("Gino", nSchedine);
    for (let iSchedine = 0; iSchedine < nSchedine; iSchedine++) {
        let schedinaTemp = generaNumeriSchedina();
        /*schedinaTemp[0] = [];
        schedinaTemp[1] = [];
        schedinaTemp[2] = [];
        for (let i2 = 1; i2 <= 9; i2++) {
            let n = new Numero(i2, false);
            schedinaTemp[0].push(n);
        }
        for (let i2 = 1; i2 <= 9; i2++) {
            let n = new Numero(i2, false);
            schedinaTemp[1].push(n);
        }
        for (let i2 = 1; i2 <= 9; i2++) {
            let n = new Numero(i2, false);
            schedinaTemp[2].push(n);

        }*/
        oggettoScedina = new Schedina("fdsfd", schedinaTemp);
        giocatoreTemp.aggiungiSchedina(oggettoScedina);
    }
    giocatori.push(giocatoreTemp);
    //----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------

}
for (let i = 0; i < 1; i++) {
    var contenitoreSchedine = document.getElementById("contenitoreSchedine");
    let schedineGiocatore = giocatori[i].getSchedine();
    for (let i2 = 0; i2 < giocatori[i].getNumeroSchedine(); i2++) {
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

}


function posizioneCoperchio(div) {
    console.log(div.innerHTML);
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


    giocatori[0].controllaPremi();
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


//----------------------console.log(giocatori[0].getSchedine()[1].getRighe()[1][3].getNumero());-------------------------------


function generaNumeriSchedina() {
    var numeriDisponibili = []; //array da dove estrarre
    for (let i = 1; i <= 90; i++) {

        numeriDisponibili.push(i);
    }
    var numeriSicuri = [];
    let numeri = []; //array con tutti i numeri non ancora sotto forma di matrice
    /*
        var schedina = [];
        
        var row0 = [];
        var row1 = [];
        var row2 = [];
        let numeroCasuale;

        for (let i = 1; i <= 9; i++) {
            numeroCasuale = Math.round(Math.random() * ((i * 10) + (i * 10 - 10)));
            while (numeroCasuale < 1 || numeroCasuale > 90) {
                numeroCasuale = Math.round(Math.random() * ((i * 10) - (i * 10 - 10)));
            }
            numeriSicuri[i - 1] = numeroCasuale;
        }
        var numMaxCol = Array(9); //contatore con massimo 2 numeri che conta le 9 colonne
        var numeriSupplementari = [];
        let duplicato = true;
        for (let i = 0; i < 6; i++) {
            numeroCasuale = Math.round(Math.random() * (90 - 1) + 1);
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
            while ((numeroCasuale >= 1 || numeroCasuale <= 90) && numMaxCol[Math.floor(numeroCasuale / 10)] != 2 && duplicato == false) {
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
        }*/
    for (let i = 0; i <= 15; i++) {
        var numcas = numeriDisponibili[Math.floor(Math.random() * numeriDisponibili.length)];
        numeriSicuri.push(numcas);
    }
    numeriSicuri.sort();
    let matriceSchedina = [];
    for (let i2 = 0; i2 < 3; i2++) {
        matriceSchedina[i2] = new Array(9);
        for (let i3 = 0; i3 < 9; i3++) {
            matriceSchedina[i2][i3] = new Numero("", false); //completa tutte le celle con un carattere vuoto in modo che riempa anche quelle bianche
        }
    }
    for (let i2 = 0; i2 < numeriSicuri.length; i2++) {
        array3 = [0, 1, 2];
        let posizioneCasuale = array3[Math.trunc(Math.random() * array3.length)];
        if (numeriSicuri[i2] != 90) {
            matriceSchedina[posizioneCasuale][Math.trunc(numeriSicuri[i2] / 10)].setNumero(numeriSicuri[i2]);
        } else {
            matriceSchedina[posizioneCasuale][8].setNumero(numeriSicuri[i2]);
        }
    }
    return matriceSchedina;
}
numeriDisponibili = [];
for (let i = 1; i <= 90; i++) {
    numeriDisponibili[i - 1] = i;
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