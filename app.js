'use strict';

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const path = require('path');
const formidable = require('formidable');
const fs = require('fs');
const fileUpload = require('express-fileupload');
const multer = require('multer');
const bodyParser = require("body-parser");
const router = express.Router();
const { PythonShell } = require('python-shell');
const { spawn } = require('child_process');
const gutil = require('gulp-util');

//static files
app.use(express.static('public'));
app.use('/css', express.static(__dirname + 'public/css'));
app.use('/js', express.static(__dirname + 'public/js'));
app.use('/images', express.static(__dirname + 'public/images'));
app.use(express.static('uploads'));
app.use(fileUpload());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));


//set editable files 
app.set('views', './views');
app.set('view engine', 'ejs');

app.get('', (req, res) => {
    res.render('home')
});
app.get('/home', (req, res) => {
    res.render('home')
});
app.get('/help', (req, res) => {
    res.render('help')
});
app.get('/output', (req, res) => {
    res.render('output')
});
app.get('/demo', (req, res) => {
    res.render('demo')
});
app.get('/demo', (req, res) => {
    res.sendFile('demo')
});
app.post("/upload", (req, res) => {
    
        if (!req.files) {

            return res.render('demo', { alert: "File upload unsuccessful, kindly try again" });
        }
        const file = req.files.file;
        const path = __dirname + "/uploads/" + file.name;

        file.mv(path, (err) => {
            if (err) {
                return res.status(500).send(err);
            }
            return res.render('demo', { alert: "File successfully uploaded! Run the algorithm" });

        });

    
    
});
app.post("/reset", (req, res) => {
   
    const fil = './uploads/graph.csv';
   
    fs.unlink(fil, (err) => {
        if (err) {
            //Show in green
            
            return res.render('output', { reset:"file not found"});
            
        } else {
            //Show in red
            return res.render('output', { reset: "file successfully deleted. Navigate to the Demo page to upload a new file" });
        }
    });


});
// python

app.post("/shortest", (req, res) => {

    var n1 = req.body.Snode;
    var n2 = req.body.Lnode;
   

    var dataToSend;
    // spawn new child process to call the python script


    //const python = spawn('python', ['test.py', n1, n2]);

    let options = {
        scriptPath: './',
        args: [n1, n2,],
    };


    var pyshell = new PythonShell('main.py', options);

    // collect data from script
    pyshell.stdout.on('data', function (data) {
        console.log(data);
        dataToSend = data.toString();
    });



    // in close event we are sure that stream from child process is closed
    pyshell.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.render('output', { ans: dataToSend });
    });
});


app.listen(port, () => console.info(`App listening on port ${port}`));










