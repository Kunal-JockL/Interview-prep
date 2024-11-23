import express from "express";
import dotenv from "dotenv";
import ConnectDB from "./connectdb.js";
import taskRoutes from "./taskRoutes.js";

dotenv.config()
ConnectDB();

const app = express();
app.use(express.json())

const port = process.env.port || 5000

app.get('/', (req, res) => {
    res.send('Hello Products!')
})

app.use('/', taskRoutes)

app.listen(port, () => {
    console.log(`API is running on http://localhost:${port}`);
})