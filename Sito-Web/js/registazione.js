function controllaRegistrazione() {
    let mioForm = document.getElementById("myform");
    let flagCampiPieni = true;
    let tagInput = document.getElementsByTagName("input");
    for (let i = 0; i < (tagInput.length); i++) {
        if (tagInput[i].value == "") {
            flagCampiPieni = false;
            tagInput[i].style.border = " solid red 2px";
            //tagInput[i].style.color = "red ";
        } else {
            tagInput[i].style.border = " solid black 2px";
            //tagInput[i].style.color = "black ";
        }
    }
    if (tagInput[6].value != tagInput[7].value) {
        flagCampiPieni = false;
    }
    if (flagCampiPieni == true) {
        mioForm.submit();
    } else {}
}
