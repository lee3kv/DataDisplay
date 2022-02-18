import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import mongoose from 'mongoose'
import route from './routes/route.js'

const app = express();

app.use('/', route)

app.use(bodyParser.json({ limit: "30mb", extended: true}));
app.use(bodyParser.urlencoded({ limit: "30mb", extended: true}));
app.use(cors()); 

const CONNECTION_URL = 'mongodb+srv://Senior:Senior2022@cluster0.o1ezz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority';
const PORT = process.env.PORT || 3000;

mongoose.connect(CONNECTION_URL, { useNewUrlParser: true, useUnifiedTopology: true})
    .then(()=> app.listen(PORT, ()=> console.log(`connected: ${PORT}`)))
    .catch((error)=> console.log(`not connected:  ${error}`));