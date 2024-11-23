import { Router } from "express";
import { createTask } from "../controllers/taskController.js";
import { authenticateToken } from "../middlewares/authMiddleware.js";

const router = Router()

router.post('/', authenticateToken, createTask)

export default router