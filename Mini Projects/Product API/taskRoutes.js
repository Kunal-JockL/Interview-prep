import express from "express";
import { productsUpload, getProducts } from "./taskController.js";

const router = express.Router();

router.get("/Products", getProducts)
router.post("/Products", productsUpload);

export default router;