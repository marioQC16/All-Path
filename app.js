'use strict';

// dependancies
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const fs = require('fs');
const fileUpload = require('express-fileupload');
const bodyParser = require("body-parser");
const { PythonShell } = require('python-shell');
const path = require('path');
const glob = require('glob');
const http = require('http');
const typeis = require('type-is');


// static files
app.use(express.static('public'));
app.use('/css', express.static(__dirname + 'public/css'));
app.use('/js', express.static(__dirname + 'public/js'));
app.use('/download', express.static(__dirname + 'public/download'));
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

// ---------------------- demo page --------------------------------------
// upload graph file from browser
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
        } else {
            return res.render('demo', { alertg: file.name + " file successfully uploaded!", partii: " Step 2", fil: file.name });

        }
    });

});

// Run the program
app.post("/run", (req, res) => {
    // if no file is selected display upload error 
    const fil = glob.sync('./uploads/*.csv')
        .map(name => ({ name, ctime: fs.statSync(name).ctime }))
        .sort((a, b) => b.ctime - a.ctime)[0].name;
    
    fs.exists(fil, (exists) => {
        if (exists) {
            var fname = path.basename(fil);
                return res.render('output', { fil2: fname })
        } else {
            return res.render('demo', { runerr: "Kindly upload a graph file to run the program" });
        }
    });

});

// ---------------------- output page --------------------------------------
// python script execution
app.post("/shortest", (req, res) => {

    const fil = glob.sync('./uploads/*.csv')
        .map(name => ({ name, ctime: fs.statSync(name).ctime }))
        .sort((a, b) => b.ctime - a.ctime)[0].name;
    var fname = path.basename(fil);
    // collect user input from webpage
    var n1 = req.body.Snode;
    var n2 = req.body.Lnode;

    fs.exists(fil, (exists) => {
        if (!exists) {
            return res.render('output', { fil2: fname, searcherr: "The graph file has been reset. Kindly navigate to the 'Demo Page' to upload a graph file" });
        } else if (!(n1, n2)) {
            return res.render('output', { fil2: fname, searcherr: "Enter a Start node and End node to search for the shortest path"});
        } else {
            // var to store python result to send to webpage
            var dataToSend;

            // pyshell options
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

                console.log(`pyshell process done close all stdio with code ${code}`);
                // send data to browser
                return res.render('output', { fil2: fname, ans: dataToSend});

            });
        }
    });
});

//reset graph file to allow new one 
app.post("/reset", (req, res) => {
   // graph file location
    const directory = './uploads/';

    fs.readdir(directory, (err, files) => {
        // if directory is empty
        if (!files.length) {
            return res.render('output', { reseterr: "No file in system to reset."});
        } else {
            // unlink graph from project
            for (const file of files) {
                fs.unlink(path.join(directory, file), (err) => {
                    if (err) {
                        return res.render('output', {reseterror: "Reset error. Kindly try again " });
                    } else {
                        return res.render('output', { reset: "File has been successfully reset. Navigate to the 'Demo Page' to upload a new file"  });
                    }
                });
            }
        } 
    });    
});

// ---------------------- help page--------------------------------------
// download test graph file
app.get("/download", (req, res) => {
    var filePath = './download/'; // Or format the path using the `id` rest param
    var fileName = 'graph.csv'; // The default name the browser will use
    res.download(filePath, fileName);
})


app.listen(port, () => console.info(`App listening on port ${port}`));





/*
 * const fileType = typeis(req, ['csv'])
        if (fileType) {

            return res.render('demo', { alert: " Invalid file type. Upload a '.csv' file" });
        }
        */



