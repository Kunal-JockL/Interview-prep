import mongoose from "mongoose";

const task = mongoose.Schema({
    title: String,
    description: String,
    status: { type: String, enum: ['complete', 'incomplete'], default: 'incomplete'},
    assignedTo: { type: mongoose.Schema.Types.ObjectId, ref: 'User'}
})

const Task = mongoose.model('Task', task, 'tasks')
export default Task