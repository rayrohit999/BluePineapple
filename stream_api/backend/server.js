import express from 'express';
import cors from "cors";
const app = express()
app.use(cors());

let clients = {};

app.get("/video-chunk", (req, res) => {
    const clientId = req.query.clientId;

    clients[clientId] = Date.now();

    res.writeHead(200, {
        "Content-Type": "text/plain",
        "Transfer-Encoding": "chunked",
        "Cache-Control": "no-cache",
    });

    let chunk = 0;
    const interval = setInterval(() => {
        chunk++;
        res.write(`Chunk ${chunk}\n`)

        //Simulate end
        if (chunk === 10) {
            clearInterval(interval);
            res.end("END");
        }
    }, 1000);

    req.on("close", () => {
        console.log("Client disconnected", clientId);
        clearInterval(interval);
    });
});



//Timeout checker
setInterval(() => {
    const now = Date.now();
    for (const id in clients) {
        if ((now - clients[id]) > 10000) {
            console.log(`Client ${id} timed out`);
            delete clients[id];
        }
    }
}, 5000);

app.listen(3000, () => console.log("Server running"));