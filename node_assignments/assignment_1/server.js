const http = require('http');

const getMessage = require('./helper.js');
const PORT = 3000;

const server = http.createServer((req, res) => {
    console.log(getMessage());
    res.end("Welcome to Node.js!");
});


server.listen(PORT, 'localhost', () => {
    console.log("Server is listening at port :",PORT);
});