async function fetchData() {
    try {
        const result = await new Promise((resolve, reject) => {
            const success = true; // can be toggled to see errror and success

            setTimeout(() => {
                if(success) {
                    resolve("Data fetched successfully");
                }else {
                    reject(new Error("Failed to fetch data"));
                }
            },3000);
        })

        return result;
    } catch(error) {
        throw error;
    }
}


async function run() {
    try{
        console.log("Fetching data .....");
        const result = await fetchData();
        console.log(result);
    } catch(error) {
        console.log(error.message);
    }
}

run();

//fetching data from public API
const axios = require('axios');

async function getPosts() {
    const url = 'https://jsonplaceholder.typicode.com/posts';

    try {
        const response = await axios.get(url);
        const posts = response.data;

        for(let i=0; i< Math.min(5, posts.length); i++) {
            console.log(`Post: ${i + 1}`);
            console.log("Title:", posts[i].title);
            console.log("Body:", posts[i].body);
            console.log(" ");
        }
    }catch(error) {
        console.log(error.message);
    }
    
}
getPosts();

//Fetching multiple APIs
function fetchMultipleApi() {
    const postsUrl = 'https://jsonplaceholder.typicode.com/posts';
    const commentsUrl = 'https://jsonplaceholder.typicode.com/comments';

    Promise.all([
        axios.get(postsUrl),
        axios.get(commentsUrl)
    ])
    .then(([postsResponse, commentsResponse]) => {
        const posts = postsResponse.data;
        const comments = commentsResponse.data;

        console.log("Posts fetched: ",posts.length);
        console.log("comments fetched: ",comments.length);

        console.log("\nFirst Post: ");
        console.log(posts[0]);

        console.log("\nFirst Comment: ");
        console.log(comments[0]);
    })
    .catch((error) => {
        console.log(error.message);
    });
}

fetchMultipleApi();