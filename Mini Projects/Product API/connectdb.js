import mongoose from "mongoose";

const ConnectDB = async () => {
    try{
        const cdb = await mongoose.connect(process.env.DB_URL) 
        console.log(`connected at ${cdb.connection.host}`)
    }catch(error){
        console.log(`ERROR: ${error.message}`)
    }
}

export default ConnectDB;