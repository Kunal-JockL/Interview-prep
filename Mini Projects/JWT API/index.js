import express from "express";
import dotenv from "dotenv";
import { ConnectDB } from "./config/connectDB.js";
import authRoutes from "./routes/authRoutes.js";
import taskRoutes from "./routes/taskRoutes.js"

dotenv.config()
const app = express();
ConnectDB();
const port = process.env.PORT || 5000;

app.use(express.json())
app.use('/auth', authRoutes)
app.use('/task', taskRoutes)

app.get('/', (req, res) => {
    res.send("Hello JWT!")
})

app.listen(port, () => {
    console.log(`API running on port ${port}`)
})