import mongoose from "mongoose";
import Task from "./TaskModel.js";

export const createTask = async (req, res) => {
    var {title, description} = req.body;
    try{
        var task = new Task({title, description});
        await task.save();
        res.status(200).json(task);
    }catch(error){
        console.log(`Error: ${error.message}`)
        res.status(400).json({message: error.message})
    }
};

export const getTasks = async (req, res) => {
    try{
        const allTasks = await Task.find();
        res.status(201).json(allTasks);
    }catch(error){
        console.log(`Error: ${error.message}`)
        res.status(400).json({message: error.message})
    }
}

export const deleteOne = async (req, res) => {
    try{
        const {_id} = req.body;
        console.log({_id});
        const deletedTask = await Task.deleteOne({ _id: _id })
        if(!deletedTask.deletedCount){
            res.status(404).json({ message: "id not found" })
        }else{
            res.status(201).json(deletedTask)
        }   
    }catch(error){
        console.log(`Error: ${error.message}`)
        res.status(400).json({message: error.message})
    }
}

export const updateTask = async (req, res) => {
    const {id} = req.params;
    const {title, description} = req.body;
    try{
        const task = await Task.findById(id);
        if (!task) {
            return res.status(404).json({ message: "Task not found" });
        }
        task.title = title
        task.description = description
        const updatedTask = await task.save()
        res.status(201).json(updatedTask)     
    }catch(error){
        console.log(`Error: ${error.message}`)
        res.status(400).json({message: error.message})
    }
}