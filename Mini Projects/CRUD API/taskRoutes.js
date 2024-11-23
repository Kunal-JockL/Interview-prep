import express from "express";
import { createTask, deleteOne, getTasks, updateTask } from "./taskController.js";

const router = express.Router();

router.post('/tasks', createTask);
router.get('/tasks', getTasks);
router.delete('/tasks', deleteOne);
router.put('/tasks/:id', updateTask);

export default router;