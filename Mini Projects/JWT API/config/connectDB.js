import mongoose from "mongoose";

export const ConnectDB = async () => {
    try{
        const conn = await mongoose.connect(process.env.URL)
        console.log(`MongoDB connected to host ${(conn.connection.host)}`)
    }catch(error){
        console.log(`Cannot connect to MongoDB: ${error.message}`)
    }
}