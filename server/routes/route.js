import express from 'express';
import {getBmeData} from '../controllers/posts.js'

const router = express.Router();

router.get('/', getBmeData);

export default router;