import mongoose from 'mongoose';

export const ConnectDB = async() => {
    try{
        const conn = await mongoose.connect(process.env.DB_URL);
        console.log(`MongoDB Connected: ${conn.connection.host}`);
    }catch(error){
        console.log(`Error: ${error.message}`);
    }
};
