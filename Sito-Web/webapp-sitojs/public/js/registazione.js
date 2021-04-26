function controllaRegistrazione() {
    let mioForm = document.getElementsByClassName("myform");
    let flagCampiPieni = true;
    let tagInput = document.getElementsByTagName("input");
    let flagCampiUguali = false;
    let tagConfermaPassword = document.getElementById("confermaPassword");
    let tagPassword = document.getElementById("password");
    tagMail = document.getElementById("indirizzoMail");

    let flagChiocciola = false;
    let flagPunto = false;
    let flagOk = true;
    for (let i = 0; i < tagMail.length; i++) {
        if (tagMail[i] == "@" && flagChiocciola == false) {
            flagChiocciola = true;
        } else if (tagMail[i] == "@") {
            flagOk = false;
        }
        if (tagMail[i] == "." && flagChiocciola == true) {
            flagPunto = true;
        }
        if (flagPunto == false) {
            flagOk = false;
        }
    }
    if (flagChiocciola == true && flagPunto == true) {
        tagMail.style.border = " solid black 2px";
    } else {
        tagMail.style.border = " solid red 2px";
    }

    if (tagPassword.value == tagConfermaPassword.value) {
        flagCampiUguali = true;
    } else {
        flagCampiUguali = false;
        tagConfermaPassword.style.border = " solid red 2px";
        tagPassword.style.border = " solid red 2px";
    }

    for (let i = 0; i < (tagInput.length); i++) {
        if (tagInput[i].value == "") {
            flagCampiPieni = false;
            tagInput[i].style.border = " solid red 2px";
        } else {
            tagInput[i].style.border = " solid black 2px";
        }
    }
    if (tagInput[6].value != tagInput[7].value) {
        flagCampiPieni = false;
    }
    if (flagCampiPieni == true && flagCampiUguali == true && flagOk != false) {
        mioForm.submit();
    } else {}
}