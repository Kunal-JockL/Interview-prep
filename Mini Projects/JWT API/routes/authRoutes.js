import { Router } from "express";
import { Signup, Login } from "../controllers/authController.js";

const router = Router()

router.post('/signup', Signup)
router.post('/login', Login)

export default router