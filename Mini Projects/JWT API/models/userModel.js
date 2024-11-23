import mongoose from "mongoose";

const user = mongoose.Schema({
    username: String,
    password: String,
    role: { type: String, enum: ['admin', 'user']}
})

const User = mongoose.model('User', user, 'users')
export default User