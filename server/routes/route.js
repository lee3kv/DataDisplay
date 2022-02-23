import express from 'express';
import {getBmeData} from '../controllers/posts.js'

const router = express.Router();

router.get('/api/bme', getBmeData);
//router.get('/api/gps', getGpsData);

export default router;