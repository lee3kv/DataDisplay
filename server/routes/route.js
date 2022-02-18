import express from 'express';
// import {getPosts} from '../controllers/data_c.js'

const router = express.Router();

router.get('/', (req, res) => {
    res.send('THIS WORKS!')
});

export default router;