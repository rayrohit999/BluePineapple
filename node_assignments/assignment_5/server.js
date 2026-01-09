import express from 'express';
import axios from 'axios';
const PORT = 3000;

const app = express();

// builtin middleware to parse incomming json request
app.use(express.json());

//Custom logging middleware it logs incomming http request and url
app.use((req, res, next) => {
    console.log(`[${req.method}] ${req.url}`);
    next();
});

//Home route
app.get("/", (req, res) => {
    res.send("Welcome to express");
})

//   POST /data
app.post('/data', (req, res) => {
    const data = req.body;

    if(!data) {
        return res.status(400).json({
            success: false,
            message: "Data not recived"
        });
    }

    console.log(data);

    res.status(200).json({
        success : true,
        message : "Data recived successfully"
    });
});

// GET /users
app.get('/users', (req, res) => {
    res.status(200).json({
        success : true,
        users : [
        {
            id : "001",
            name : "Rohit Kumar"
        },
        {
            id : "002",
            name : "Mohit Kumar"
        }]
    })
});

//route for checking error
app.get("/error", (req, res, next) => {
    const error = new Error("Something went wrong");
    next(error); //passing error to handling middleware
});


//route for extrnal-posts
app.get("/external-posts", async (req, res, next) => {
    try {
        const url = "https://jsonplaceholder.typicode.com/posts";
        const response = await axios.get(url);
        const posts = response.data;
        res.status(200).json(posts);
    }catch(error) {
        next(error);
    }
});

//middleware for handling 404 error
app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: "Route not found"
    });
});

//Error handling middleware
app.use((err, req, res, next) => {
    console.log("Error: ",err.message);
    res.status(500).json({
        success : false,
        message : "Something went wrong"
    });
});


//starting server
app.listen(PORT, () => {
    console.log("App is listening at port: ",PORT);
});
