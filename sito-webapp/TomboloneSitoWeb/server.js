let express = require("express");
let app = express();
let bodyparser = require("body-parser");
let jsdom = require("jsdom");
let fs = require("fs");
const { response } = require("express");

let { JSDOM } = jsdom; //destrutturazione


app.use(bodyparser.json());
app.use(bodyparser.urlencoded());
app.listen("3000", function() {
    console.log("SERVER CONNESSO");
})

app.get("/", function(req, res, next) {

    res.sendFile(__dirname + "/index.html");
})

app.get("/accedi", function(req, res, next) {
    res.sendFile(__dirname + "/html/accedi.html");
});
app.post("/accessoEffettuato", function(req, res, next) {
    res.send(req.body.username);
})