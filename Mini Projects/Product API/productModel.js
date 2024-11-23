import mongoose from "mongoose";

const productSchema = new mongoose.Schema({
    name: String,
    category: String,
    price: Number,
    stock: Number
})

const product = mongoose.model('product', productSchema)

export default product