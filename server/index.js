import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import mongoose from 'mongoose'

import post_routes from './routes/posts.js'

const app = express();

app.use('/', post_routes)

//BME Data
const bme = require('./api/bme_a')
app.use('/api/bme', )

app.use(bodyParser.json({ limit: "30mb", extended: true}));
app.use(bodyParser.urlencoded({ limit: "30mb", extended: true}));
app.use(cors()); 

const CONNECTION_URL = 'mongodb://localhost/database';
const PORT = process.env.PORT || 3000;

mongoose.connect(CONNECTION_URL, { useNewUrlParser: true, useUnifiedTopology: true})
    .then(()=> app.listen(PORT, ()=> console.log(`connected: ${PORT}`)))
    .catch((error)=> console.log(`not connected:  ${error}`));