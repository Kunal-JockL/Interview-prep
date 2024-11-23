import Task from "../models/taskModel.js"

export const createTask = async (req, res) => {
    try{
        const {title, description} = req.body
        const user = req.user
        const newTask = Task({title, description, assignedTo: user.userId})
        const st = await newTask.save()
        res.status(201).json(st)
    }catch(error){
        console.log(`Error: ${error.message}`)
        res.status(401).json(`message: ${error.message}`)
    }
}