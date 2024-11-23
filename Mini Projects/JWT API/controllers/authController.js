import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import User from '../models/userModel.js';

export const Signup = async (req, res) => {
    try{
        const { username, password, role } = req.body
        const encryptedPassword = await bcrypt.hash(password, 10)
        const newUser = User({username, password: encryptedPassword, role})
        await newUser.save();
        res.status(201).json('You have been registered!')
    }catch(error){
        console.log(`Error: ${error.message}`)
        res.status(401).json(`message: ${error.message}`)
    }
}

export const Login = async (req, res) => {
    try{
        const {username, password} = req.body
        const user = await User.findOne({username})
        if ( !user || !(await bcrypt.compare(password, user.password))){
            res.status(401).json({'message': 'Invalid Credentials'})
        }
        const token = jwt.sign({ userId: user._id, role: user.role }, process.env.jwt_secret, { expiresIn: '1h' });
        res.status(201).json({'token': token})
    }catch(error){
        console.log(`Error: ${error.message}`)
        res.status(401).json(`message: ${error.message}`)
    }
}