import express from 'express';
import {home, getBmeData} from '../controllers/posts.js'

const router = express.Router();

router.get('/', home)
router.get('/api/bme', getBmeData);
//router.get('/api/gps', getGpsData);

export default router;