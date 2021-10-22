'use strict';

const express = require('express')
const app = express()
const port = process.env.PORT || 1337;

//static files
app.use(express.static('public'))
app.use('/css', express.static(__dirname + 'public/css'))
app.use('/js', express.static(__dirname + 'public/js'))
app.use('/images', express.static(__dirname + 'public/images'))


//set editable files 
app.set('views', './views')
app.set('view engine', 'ejs')


app.get('', (req, res) => {
    res.render('home')
})


app.get('/home', (req, res) => {
    res.render('home')
})

app.get('/demo', (req, res) => {
    res.render('demo')
})

app.get('/output', (req, res) => {
    res.render('output')
})

app.listen(port, () => console.info(`App listening on port ${port}`))










