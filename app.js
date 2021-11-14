'use strict';

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const fs = require('fs');
const fileUpload = require('express-fileupload');
const bodyParser = require("body-parser");
const { PythonShell } = require('python-shell');

//static files
app.use(express.static('public'));
app.use('/css', express.static(__dirname + 'public/css'));
app.use('/js', express.static(__dirname + 'public/js'));
app.use('/images', express.static(__dirname + 'public/images'));
app.use(express.static('uploads'));
app.use(fileUpload());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));


//set editable pages for viewing 
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

//upload graph file from browser
app.post("/upload", (req, res) => {
        // if no file is selected display upload error 
        if (!req.files) {
            return res.render('demo', { alert: "Kindly select a file to upload" });
        }
    
        const file = req.files.file;
        const path = __dirname + "/uploads/" + file.name;

        // move file to uploads directory to pass to python script]
        file.mv(path, (err) => {
            if (err) {
                return res.render('demo', { alert: "File upload unsuccessful, kindly try again" });
            }
            return res.render('demo', { alertg: "File successfully uploaded! Run the algorithm" });
        });
});

//reset graph file to allow new one 
app.post("/reset", (req, res) => {
   // graph file location
    const fil = './uploads/graph.csv';
   // unlink graph from project
    fs.unlink(fil, (err) => {
        if (err) {
            return res.render('output', { reseterror:"file not found"});
        } else {
            return res.render('output', { reset: "file successfully deleted. Navigate to the 'Demo Page' to upload a new file" });
        }
    });
});
// python connection
app.post("/shortest", (req, res) => {

    const fil = './uploads/graph.csv';
    // collect user input from webpage
    var n1 = req.body.Snode;
    var n2 = req.body.Lnode;

    fs.exists(fil, (exists) => {
        if (!exists) {
            return res.render('output', { searcherr: "The graph file has been reset. Kindly navigate to the 'Demo Page' to upload another graph file" });
        } else if (!(n1, n2)) {
                return res.render('output', { searcherr: "Enter a Start node and End node to search for the shortest path" });
            } else {
                // var to store python result to send to webpage
                var dataToSend;

                // python option
                let options = {
                    scriptPath: './',
                    args: [n1, n2,],
                };

                // spawn python script
                var pyshell = new PythonShell('main.py', options);

                // collect data from script
                pyshell.stdout.on('data', function (data) {
                    console.log(data);
                    // convert script output to string for output
                    dataToSend = data.toString();
                });

                // in close event we are sure that stream from child process is closed
                pyshell.on('close', (code, err) => {
                    console.log(`child process close all stdio with code ${code}`);
                    // send data to browser
                    if (err) {
                        return res.render('output', { ans: err });
                    } else {
                       return res.render('output', { ans: dataToSend });
                    }
                });
            }
        
    });

   
});

app.post("/run", (req, res) => {
    // if no file is selected display upload error 
    const fil = './uploads/graph.csv';

    fs.exists(fil, (exists) => {
        if (exists) {
            return res.render('output');
        } else {
            return res.render('demo', { runerr: "Kindly upload a graph file to run the program" });
        }
    });
    
  

    
});

app.listen(port, () => console.info(`App listening on port ${port}`));










