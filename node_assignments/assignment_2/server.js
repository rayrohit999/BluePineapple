import { readFile, appendFile } from "fs/promises";
import fsSync from 'fs';
import http from 'http';

const PORT = 3000;


function readBlocking() {
    console.log("blocking read started....");
    const data = fsSync.readFileSync("log.txt", "utf-8");
    console.log(data);
    console.log("Blocking read finished....");
}

async function readNonBlocking() {
    console.log("Non Blocking reading started....");
    const data = await readFile("log.txt", "utf-8");
    console.log(data);
    console.log("Non Blocking reading finished.");
}

async function appendToFile(text) {
    try {
      // Append a timestamped log entry
      const logEntry = `${new Date().toISOString()}: ${text}\n`;
      await appendFile('log.txt', logEntry, 'utf8');
      console.log('Log entry added');
    } catch (err) {
      console.error('Error appending to file:', err);
    }
}

const server = http.createServer((req, res) => {
    res.writeHead(200,{'Content-Type' : 'text/plain'});
    //Event loop Demonstration can be seen in console when server get request
    console.log("strat");

    process.nextTick(() => {
        console.log("process.nextTick : Executed before the next event loop iteration");
    });

    setTimeout(() => {
        console.log("setTimeout : callback executed after a delay of 5ms");
    },5000);

    setImmediate(() => {
        console.log("setImmediate : Executed after the current event loop phase");
    });

    console.log("End");

    res.end("Go to terminal");
});

server.listen(PORT, 'localhost', () => {
    //Blocking and NonBlocking Demonstration can be seen in console when server stated
    readBlocking();
    readNonBlocking();
    appendToFile("application started");
    console.log("Application started at port: ",PORT);
});