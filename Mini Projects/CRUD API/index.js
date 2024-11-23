import express from 'express';
import dotenv from 'dotenv';
import { ConnectDB } from './dbConfig.js';
import taskRoutes from './taskRoutes.js';

dotenv.config()
ConnectDB();

const app = express();
const port = process.env.port || 5000;

app.get('/', (req, res) =>{
    res.send('Hello, Kunal!');
});

app.use(express.json());
app.use('/', taskRoutes);

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
