var flagRighe = [0, 0, 0];
var celle = document.getElementsByClassName("cellaSchedina");
var coperchi = document.getElementsByClassName("coperchio");

globalThis.numeriSchedina = [];
for (var i = 0; i < 27; i++) {
    numeriSchedina[i] = false;
}
/*var numeri = [
    [2, 23, 35, 56, 88],
    [11, 37, 51, 67, 71],
    [29, 42, 50, 70, 83]
];
*/
for (var i = 0; i < celle.length; i++) {
    celle[i].addEventListener("click", function() {
        posizioneCoperchio(this);
    });
}

function posizioneCoperchio(div) {
    for (var i = 0; i < celle.length; i++) {
        if ((celle[i].innerHTML == div.innerHTML) && (div.innerHTML != "&nbsp;")) {
            if (numeriSchedina[i] == false) {

                coperchi[i].style.transform = "translateY(19px)";
                coperchi[i].style.transition = "250ms";

                numeriSchedina[i] = true;
            }
        }
    }

    controllaPremi();
}

function controllaPremi() {
    /*
        for (let i = 0; i < 3; i++) {
            for (let i2 = 0; i2 < 9; i2++) {
                if (numeriSchedina[i][i2] == true) {
                    flagRighe[i] += 1;
                }
            }
        }

        let esistenzaPremio = false;
        for (var i = 0; i < flagRighe.length; i++) {
            switch (flagRighe[i]) {
                case 2:
                    alert("ambo");
                    break;
                case 3:
                    alert("terna");
                    break;
                case 4:
                    alert("quaterna");
                    break;
                case 5:
                    alert("cinquina");
                    break;
            }
            var flagRighe = [0, 0, 0];
        }*/
    let i3 = 0;
    var flagRighe = [0, 0, 0];
    var numeri = [];
    numeriSchedina.forEach(temp => {
        numeri[i3] = temp;
        i3 += 1;
    });
    for (var i2 = 0; i2 < 9; i2++) {
        if (numeri[i2] == true) {
            flagRighe[0] += 1;
        }
    }
    for (var i2 = 9; i2 < 18; i2++) {
        if (numeri[i2] == true) {
            flagRighe[1] += 1;
        }
    }
    for (var i2 = 18; i2 < 27; i2++) {
        if (numeri[i2] == true) {
            flagRighe[2] += 1;
        }
    }


    let esistenzaPremio = false;
    for (var i = 0; i <= 2; i++) {
        if (flagRighe[i] >= 2) {
            esistenzaPremio = true;
        }
    }
    if (esistenzaPremio == true) {
        pulsante = document.getElementById("bottonePremi");
        pulsante.style.display = "inline-block";
        pulsante.addEventListener("click", function() {
            for (var i2 = 0; i2 < flagRighe.length; i2++) {
                switch (flagRighe[i2]) {
                    case 2:
                        alert("ambo in riga " + (i2 + 1));
                        break;
                    case 3:
                        alert("Terna in riga " + (i2 + 1));
                        break;
                    case 4:
                        alert("Quaterna in riga " + (i2 + 1));
                        break;
                    case 5:
                        alert("Cinquina in riga " + (i2 + 1));
                        break;
                }
            }
        })
    } else {
        pulsante = document.getElementById("bottonePremi");
        pulsante.style.display = "none";
    }

    /*
    if (flagRiga1 == true) {
        for (var i = 0; i < 9; i++) {
            if (numeriSchedina[i] == true) {
                nCoperture = nCoperture + 1;
            }
        }
        flagRiga1 = nomePremi(nCoperture, 1);
    }

    nCoperture = 0;
    if (flagRiga2 == true) {
        for (var i = 9; i < 18; i++) {
            if (numeriSchedina[i] == true) {
                nCoperture = nCoperture + 1;
            }
        }
        flagRiga2 = nomePremi(nCoperture, 2);
    }

    nCoperture = 0;
    if (flagRiga3 == true) {
        for (var i = 18; i < 27; i++) {
            if (numeriSchedina[i] == true) {
                nCoperture = nCoperture + 1;
            }
        }
        flagRiga3 = nomePremi(nCoperture, 3);
    }*/

}
/*
let pulsante;

function nomePremi() {
    for (let i = 0; i < flagRighe.length; i++) {
        switch (n) {
            case 2:
                alert(flagRighe[i] + "2");
                pulsante = document.getElementById("bottonePremi");
                pulsante.style.display = "inline-block";
                break;
            case 3:
                alert(flagRighe[i] + "3");
                pulsante = document.getElementById("bottonePremi");
                pulsante.style.display = "inline-block";
                flag = false;
                break;
            case 4:
                alert(flagRighe[i] + "4");
                pulsante = document.getElementById("bottonePremi");
                pulsante.style.display = "inline-block";
                flag = false;
                break;
            case 5:
                alert(flagRighe[i] + "5");
                pulsante = document.getElementById("bottonePremi");
                pulsante.style.display = "inline-block";
                flag = false;
                break;
        }
    }*/
/*
    switch (n) {
        case 2:
            mostraPulsantePremio(riga, "Ambo");
            break;
        case 3:
            mostraPulsantePremio(riga, "Terna");
            flag = false;
            break;
        case 4:
            mostraPulsantePremio(riga, "Quaterna");
            flag = false;
            break;
        case 5:
            mostraPulsantePremio(riga, "Cinquina");
            flag = false;
            break;
    }
}*/
/*
function mostraPulsantePremio(riga, nomePremio) {
    let pulsante = document.getElementById("bottonePremi");
    pulsante.style.display = "inline-block";
    premiRiga[riga - 1] = nomePremio;
    if (premiRiga[0] != "") {
        stringa1 = ""
    }
    if (premiRiga[1] != "") {
        stringa2 =
    }
    if (premiRiga[2] != "") {
        stringa3 =
    }

    pulsante.addEventListener("click", function() {

    });
}*/
var numeriDisponibili = [];
for (let i = 1; i < 91; i++) {
    numeriDisponibili.push(i);
}

function estraiNumero() {
    var nuovoNum = [Math.floor(Math.random() * numeriDisponibili.length)];
    let index = numeriDisponibili.indexOf(parseInt(nuovoNum));
    numeriDisponibili.splice(index, 1);
    var testo = document.getElementById("numeroEstratto").innerHTML = nuovoNum;
}