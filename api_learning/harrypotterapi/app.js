const url = "https://api.potterdb.com/";

async function getBookList(){
    try{
        const endPoint = "/v1/books"
        const result = await fetch(url + endPoint);
        const readAbleResult = await result.json();
        return readAbleResult.data;
    } catch(err){
        console.log("Error: ",err)
        return [];
    }
}

async function renderBooks() {
    const books = await getBookList();
    const table = document.querySelector("#bookTable");

    books.forEach((book, index) => {
        const row = document.createElement("tr");
        //sr. no
        const srCell = document.createElement("td");
        srCell.textContent = index + 1;
        //title
        const titleCell = document.createElement("td");
        titleCell.textContent = book.attributes.title;
        //author
        const authorCell = document.createElement("td");
        authorCell.textContent = book.attributes.author
        //details link
        const detailsCell = document.createElement("td");
        const link = document.createElement("a");
        link.textContent = "View details";
        link.href = url + book.links.self;
        link.target = "_blank";
        detailsCell.appendChild(link);
        //append cells to row
        row.appendChild(srCell);
        row.appendChild(titleCell);
        row.appendChild(authorCell);
        row.appendChild(detailsCell);
        //Append row to table
        table.appendChild(row);
    });
}

renderBooks();