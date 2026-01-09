import http from 'http';

const port = 3001;

const server = http.createServer((req, res) => {

    if (req.method === 'GET' && req.url === '/time') {
        res.writeHead(200, { 'Content-Type': 'application/json' });

        const time = new Date();

        res.end(JSON.stringify({
            success: true,
            time: time.toLocaleTimeString()
        }));
        return;
    }

    // fallback route
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
        success: false,
        message: 'Route not found'
    }));
});

server.listen(port, 'localhost', () => {
    console.log(`Server running at http://localhost:${port}/`);
});
