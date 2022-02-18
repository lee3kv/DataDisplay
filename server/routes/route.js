import express from 'express';
import {getData} from '../controllers/posts.js'

const router = express.Router();

route.get('/', getData);

export default route;