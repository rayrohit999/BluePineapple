// const express = require('express');
import express from 'express';
import {createServer} from 'http';
import { Server } from 'socket.io';
import moment from 'moment-timezone';
import {
    readFromCSV,
    writeToCSV,
    editCSV,
    deleteFromCSV
} from "./data/index.js";
import cors from 'cors';
import multer from "multer";
import path from "path";
import fs from "fs";
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

//http server
const server = createServer(app);


// Initializing SOCKET.IO with CORS

const io = new Server(server,{
    cors: {
        origin: "*",
        mathods: ["GET", "POST"]
    }
});

io.on('connection', (socket) =>{
    console.log('client connected: ',socket.id);

    //sending time every second to this client
    const timeInterval = setInterval(() => {
        const time = moment().tz('Asia/Kolkata'); // 'America/New_York' 'Australia/Sydney' 'Asia/Kolkata'
        socket.emit('time-update', {
            success: true,
            time: time.format('h:mm:ss a')
        });
    },1000);

    socket.on('disconnect', () => {
        console.log('Client disconnected: ', socket.id);
        clearInterval(timeInterval);
    });
});

app.get('/', (req, res) => {
    res.send("hello world i am rohit kumar");
});

server.listen(port, () => {
    console.log("app is listening at port",port);
});
server.setTimeout(10 * 60 * 1000);

app.get('/teacher', async (req, res) => {
    try {
        const data = await readFromCSV('./data/teachers.csv');
        res.status(200).json({ success: true, data });
    } catch (err) {
        res.status(500).json({ success: false, error: err.message });
    }
});

app.post('/teacher', async (req, res) => {
    try {
        const teacher = req.body;

        if (!teacher.TeacherID || !teacher.Name) {
            return res.status(400).json({
                success: false,
                message: "TeacherID and Name are required"
            });
        }

        await writeToCSV([teacher], './data/teachers.csv');

        res.status(201).json({
            success: true,
            message: "Teacher added successfully"
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: "Failed to add teacher",
            error: err.message
        });
    }
});


app.patch('/teacher', async (req, res) => {
    try {
        const updatedTeacher = req.body;

        if (!updatedTeacher.TeacherID) {
            return res.status(400).json({
                success: false,
                message: "TeacherID is required"
            });
        }

        await editCSV(updatedTeacher, './data/teachers.csv');

        res.status(200).json({
            success: true,
            message: "Teacher updated successfully"
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: "Failed to update teacher",
            error: err.message
        });
    }
});


app.delete('/teacher', async (req, res) => {
    try {
        const { TeacherID } = req.body;

        if (!TeacherID) {
            return res.status(400).json({
                success: false,
                message: "TeacherID is required"
            });
        }

        await deleteFromCSV(TeacherID, './data/teachers.csv');

        res.status(200).json({
            success: true,
            message: "Teacher deleted successfully"
        });
    } catch (err) {
        console.log("Delete error: ", err);
        res.status(500).json({
            success: false,
            message: "Failed to delete teacher",
            error: err.message
        });
    }
});

app.delete('/teacher/bulk', async (req, res) => {
    try{
        const { TeacherIDs } = req.body;

        if (!TeacherIDs || !Array.isArray(TeacherIDs) || TeacherIDs.length === 0) {
            return res.status(400).json({
                success: false,
                message: "Teacher IDs array is required"
            });
        }
        
        for (const TeacherID of TeacherIDs) {
            await deleteFromCSV(TeacherID, './data/teachers.csv')
        }

        res.status(200).json({
            success: true,
            message: `${TeacherIDs.length} teacher(s) deleted successfully`
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: "Failed to delete teachers",
            error: err.message
        });
    }
});

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "uploads/");
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname); // 👈 keeps name + extension
    }
});

const upload = multer({
    storage,
    limits: {
        fileSize: 1024 * 1024 * 500 // 500 MB
    }
});


app.post('/upload', upload.single("file"), (req, res) => {
    try {
        res.status(200).json({
            success : true,
            filename : req.file.originalname
        })
    }catch(error) {

    }
});

app.get("/download/:filename", (req, res) => {
    const filePath = path.join("uploads", req.params.filename);
    const stat = fs.statSync(filePath);

    const range = req.headers.range;
    if (!range) {
        res.writeHead(200, {
            "Content-Length": stat.size,
            "Content-Type": "application/octet-stream"
        });
        fs.createReadStream(filePath).pipe(res);
        return;
    }

    const parts = range.replace(/bytes=/, "").split("-");
    const start = parseInt(parts[0], 10);
    const end = parts[1]
        ? parseInt(parts[1], 10)
        : stat.size - 1;

    res.writeHead(206, {
        "Content-Range": `bytes ${start}-${end}/${stat.size}`,
        "Accept-Ranges": "bytes",
        "Content-Length": end - start + 1,
        "Content-Type": "application/octet-stream"
    });

    fs.createReadStream(filePath, { start, end }).pipe(res);
});