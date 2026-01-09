
const serverTime = document.querySelector('#serverTime');

function getTime() {
    const url = 'http://localhost:3001/time';

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            serverTime.textContent = 'Server Time: ' + data.time;
        })
        .catch(error => {
            console.error('Error fetching time:', error);
            serverTime.textContent = 'Unable to fetch time';
        });
}

setInterval(getTime, 1000);

let isEditMode = false;

function showTeachers() {
    const teacherTable = document.querySelector("#teacherTable");
    const url = "http://localhost:3000/teacher";

    // Clear table & add header
    teacherTable.innerHTML = `
        <tr>
            <th>Teacher ID</th>
            <th>Name</th>
            <th>Subject</th>
            <th>Phone</th>
            <th>Action</th>
        </tr>
    `;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            const teachers = data.data;

            teachers.forEach(teacher => {
                const row = document.createElement("tr");

                const teacherIdCell = document.createElement("td");
                teacherIdCell.textContent = teacher.TeacherID;

                const nameCell = document.createElement("td");
                nameCell.textContent = teacher.Name;

                const subjectCell = document.createElement("td");
                subjectCell.textContent = teacher.Subject;

                const phoneCell = document.createElement("td");
                phoneCell.textContent = teacher.Phone;

                const actionCell = document.createElement("td");

                // EDIT LINK
                const editLink = document.createElement("button");
                editLink.textContent = "Edit";
                editLink.style.marginRight = "10px";
                editLink.classList.add("btn", "btn-warning");
                editLink.setAttribute("data-bs-toggle", "modal");
                editLink.setAttribute("data-bs-target", "#teacherModal");
                editLink.addEventListener("click", (e) => {
                    e.preventDefault();

                    document.querySelector("#TeacherID").value = teacher.TeacherID;
                    document.querySelector("#Name").value = teacher.Name;
                    document.querySelector("#Subject").value = teacher.Subject;
                    document.querySelector("#Phone").value = teacher.Phone;

                    document.querySelector("#TeacherID").disabled = true;

                    isEditMode = true;
                    message.textContent = "Editing Teacher: " + teacher.TeacherID;
                });

                // DELETE LINK
                const deleteLink = document.createElement("button");
                deleteLink.textContent = "Delete";
                deleteLink.classList.add("btn", "btn-danger")
                deleteLink.addEventListener("click", async (e) => {
                    e.preventDefault();

                    if (!confirm("Are you sure you want to delete this teacher?")) return;

                    try {
                        const response = await fetch("http://localhost:3000/teacher", {
                            method: "DELETE",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({ TeacherID: teacher.TeacherID })
                        });

                        const result = await response.json();

                        if (!response.ok) {
                            throw new Error(result.message || "Delete failed");
                        }

                        message.textContent = "Teacher deleted successfully";
                        showTeachers();

                    } catch (error) {
                        console.error(error);
                        message.textContent = error.message || "Error deleting teacher";
                    }
                });

                actionCell.appendChild(editLink);
                actionCell.appendChild(deleteLink);

                row.appendChild(teacherIdCell);
                row.appendChild(nameCell);
                row.appendChild(subjectCell);
                row.appendChild(phoneCell);
                row.appendChild(actionCell);

                teacherTable.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching teachers:', error);
            const errorRow = document.createElement("tr");
            const errorCell = document.createElement("td");
            errorCell.textContent = "Unable to fetch records";
            errorCell.colSpan = 5;
            errorRow.appendChild(errorCell);
            teacherTable.appendChild(errorRow);
        });
}

showTeachers();


// teacher form handling

const form = document.querySelector("#teacherForm");
const message = document.querySelector("#message");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const teacherData = {
        TeacherID: document.querySelector("#TeacherID").value.trim(),
        Name: document.querySelector("#Name").value.trim(),
        Subject: document.querySelector("#Subject").value.trim(),
        Phone: document.querySelector("#Phone").value.trim()
    };

    const method = isEditMode ? "PATCH" : "POST";

    try {
        const response = await fetch("http://localhost:3000/teacher", {
            method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(teacherData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message || "Operation failed");
        }

        message.textContent = isEditMode
            ? "Teacher updated successfully"
            : "Teacher added successfully";

        form.reset();
        document.querySelector("#TeacherID").disabled = false;
        isEditMode = false;

        showTeachers();

    } catch (error) {
        console.error(error);
        message.textContent = error.message || "Error saving teacher";
    }
});

//upload button 


const uploadBtn = document.querySelector("#uploadBtn");
const progressBar = document.querySelector("#uploadProgress");
const statusText = document.querySelector("#uploadStatus");

uploadBtn.addEventListener("click", () => {
    const file = document.querySelector("#fileInput").files[0];
    if (!file) return alert("Select a file");

    const formData = new FormData();
    formData.append("file", file);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:3000/upload");

    xhr.upload.onprogress = (e) => {
        if (e.lengthComputable) {
            progressBar.value = (e.loaded / e.total) * 100;
        }
    };

    xhr.onload = () => {
        alert("upload complete");
        statusText.textContent = "Upload complete";
    };

    xhr.onerror = () => {
        alert("Upload failed");
        statusText.textContent = "Upload failed";
    };

    xhr.onabort = () => {
        alert("Upload aborted");
        statusText.textContent = "Upload aborted";
    };

    xhr.send(formData);

});


// Download button 

let controller;
let downloadedBytes = 0;

const downloadBtn = document.querySelector("#downloadBtn");
const pauseBtn = document.querySelector("#pauseBtn");
const resumeBtn = document.querySelector("#resumeBtn");
const downloadProgressBar = document.querySelector("#downloadProgress");

downloadBtn.addEventListener("click", async () => {
    downloadBtn.disabled=true;
    startDownload();
});

async function startDownload() {
    controller = new AbortController();

    const response = await fetch("http://localhost:3000/download/samplevideo.mkv", {
        headers: {
            Range: `bytes=${downloadedBytes}-`
        },
        signal: controller.signal
    });

    const reader = response.body.getReader();
    const contentLength = +response.headers.get("Content-Length");

    let received = 0;
    const chunks = [];

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        chunks.push(value);
        received += value.length;
        downloadedBytes += value.length;

        downloadProgressBar.value =
            (downloadedBytes / (downloadedBytes + contentLength)) * 100;
    }

    const blob = new Blob(chunks);
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "file";
    a.click();
}

pauseBtn.addEventListener("click", () => {
    if (controller) controller.abort();
});
resumeBtn.addEventListener("click", () => {
    startDownload();
});

bootstrap.Modal.getInstance(document.getElementById('teacherModal')).hide();