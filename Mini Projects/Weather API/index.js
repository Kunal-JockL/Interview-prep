import express from "express";
import dotenv from "dotenv";
import { getWeather } from "./getWeather.js";

dotenv.config()
const port = process.env.PORT || 5000

const app = express();

app.use(express.json())

app.get('/', (req, res) => {
    res.send("Nice Weather!");
})

app.get('/weather/:city', getWeather);

app.listen(port, () => {
    console.log(`Api running on http://localhost:${port}`)
})