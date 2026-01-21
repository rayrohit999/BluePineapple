const serverTime = document.querySelector('#serverTime');

 const socket = io('http://localhost:3000');
 socket.on('connect', () => {
    document.getElementById('status').textContent = "Connected";
 });

 socket.on('disconnect', () => {
    document.getElementById('status').textContent = "Disconnected";
 });

 socket.on('time-update', (data) => {
    if (data.success) {
        document.getElementById('time').textContent = data.time;
    }
 });

let isEditMode = false;
let currentEditRow = null;

const message = document.querySelector('#message');
const addTeacherBtn = document.querySelector('#addTeacher');
const editTeacherBtn = document.querySelector('#editTeacher');
const deleteTeacherBtn = document.querySelector('#deleteTeacher');
const selectAllCheckbox = document.querySelector('#selectAll');



function showTeachers() {
    const tbody = document.querySelector("#teacherTable tbody");
    const url = "http://localhost:3000/teacher";
    tbody.innerHTML = ""

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            const teachers = data.data;

            if (!teachers || teachers.length === 0) {
                tbody.innerHTML = ""; // Clear any existing rows
                selectAllCheckbox.checked = false;
                updateButtonStates();
                return;
            }

            teachers.forEach(teacher => {
                const row = createTeacherRow(teacher);
                tbody.appendChild(row);
            });
            selectAllCheckbox.checked = false;
            updateButtonStates();
        })
        .catch(error => {
            console.error("Error fetching teachers: ", error);
            tbody.innerHTML = "";
            const errorRow = document.createElement('tr');
            const errorCell = document.createElement('td');
            errorCell.textContent = "Unable to fetch records";
            errorCell.colSpan = 6;
            errorCell.className = "text-center text-danger";
            errorRow.appendChild(errorCell);
            tbody.appendChild(errorRow);
            
            selectAllCheckbox.checked = false;
            updateButtonStates();
        })
}

function createTeacherRow(teacher, isNew = false) {
    const row = document.createElement('tr');

    const checkboxCell = document.createElement('td');
    const checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.className = "teacher-checkbox";
    checkbox.value = teacher.TeacherID;
    checkbox.addEventListener("change", updateButtonStates);
    checkboxCell.appendChild(checkbox);

    const teacherIdCell = document.createElement("td");
    teacherIdCell.textContent = teacher.TeacherID;

    const nameCell = document.createElement("td");
    nameCell.textContent = teacher.Name;

    const subjectCell = document.createElement("td");
    subjectCell.textContent = teacher.Subject || "";

    const phoneCell = document.createElement("td");
    phoneCell.textContent = teacher.Phone || "";

    const actionCell = document.createElement("td");
    actionCell.innerHTML = isNew ? "" : "-";

    row.appendChild(checkboxCell);
    row.appendChild(teacherIdCell);
    row.appendChild(nameCell);
    row.appendChild(subjectCell);
    row.appendChild(phoneCell);
    row.appendChild(actionCell);

    return row;
}

function createEditableRow(teacher = null) {
    const row = document.createElement("tr");
    row.className = "editable-row";

    const checkboxCell = document.createElement("td");
    checkboxCell.innerHTML = "-";

    const teacherIdCell = document.createElement("td");
    const teacherIdInput = document.createElement("input");
    teacherIdInput.type = "text";
    teacherIdInput.className = "form-control form-control-sm";
    teacherIdInput.name = "TeacherID";
    teacherIdInput.value = teacher?.TeacherID || "";
    teacherIdInput.disabled = teacher !== null; //Disable if editing
    teacherIdInput.required = true;
    teacherIdCell.appendChild(teacherIdInput);

    const nameCell = document.createElement("td");
    const nameInput = document.createElement("input");
    nameInput.type = "text";
    nameInput.className = "form-control form-control-sm";
    nameInput.name = "Name";
    nameInput.value = teacher?.Name || "";
    nameInput.required = true;
    nameCell.appendChild(nameInput);

    const subjectCell = document.createElement("td")
    const subjectInput = document.createElement("input");
    subjectInput.type = "text";
    subjectInput.className = "form-control form-control-sm";
    subjectInput.name = "Subject";
    subjectInput.value = teacher?.Subject || "";
    subjectCell.appendChild(subjectInput);

    const phoneCell = document.createElement("td");
    const phoneInput = document.createElement("input");
    phoneInput.type = "tel";
    phoneInput.className = "form-control form-control-sm";
    phoneInput.name = "Phone";
    phoneInput.value = teacher?.Phone || "";
    phoneCell.appendChild(phoneInput);

    const actionCell = document.createElement("td");
    const saveBtn = document.createElement("button");
    saveBtn.textContent = "Save";
    saveBtn.className = "btn btn-sm btn-success me-1";
    saveBtn.addEventListener("click", () => saveTeacher(row, teacher !== null));

    const cancelBtn = document.createElement("button");
    cancelBtn.textContent = "Cancel";
    cancelBtn.className = "btn btn-sm btn-secondary";
    cancelBtn.addEventListener("click", () => {
        if (teacher) {
            const normalRow = createTeacherRow(teacher);
            row.replaceWith(normalRow);
            currentEditRow = null;
        } else {
            row.remove();
        }
        updateButtonStates();
        message.textContent = "";
    });

    actionCell.appendChild(saveBtn);
    actionCell.appendChild(cancelBtn);

    row.appendChild(checkboxCell);
    row.appendChild(teacherIdCell);
    row.appendChild(nameCell);
    row.appendChild(subjectCell);
    row.appendChild(phoneCell);
    row.appendChild(actionCell);

    return row;
}

async function saveTeacher(row, isEdit) {
    const inputs = row.querySelectorAll("input");
    const teacherData = {
        TeacherID: inputs[0].value.trim(),
        Name: inputs[1].value.trim(),
        Subject: inputs[2].value.trim(),
        Phone: inputs[3].value.trim()
    };
    
    if (!teacherData.TeacherID || !teacherData.Name) {
        message.textContent = "TeacherID and Name are required";
        return;
    }

    const method = isEdit ? "PATCH" : "POST";

    try {
        const response = await fetch("http://localhost:3000/teacher", {
            method,
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(teacherData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message || "Operation failed");
        }

        message.textContent = isEdit?"Teacher updated successfully":"Teacher added successfully";
        message.className = "fw-bold text-success";

        setTimeout(() => {
            message.textContent = ""
            message.className = "fw-bold text-danger";
        }, 3000);

        currentEditRow = null;
        showTeachers();
    } catch (error) {
        console.error(error);
        message.textContent = error.message || "Error saving teacher";
        message.className = "fw-bold text-danger";
    }
}

function getSelectedTeachers() {
    const checkboxes = document.querySelectorAll(".teacher-checkbox:checked");
    return Array.from(checkboxes).map(cb => cb.value);
}

function updateButtonStates() {
    const selected = getSelectedTeachers();
    const hasEditableRow = document.querySelector(".editable-row") !== null;
    const hasTeachers = document.querySelectorAll(".teacher-checkbox").length > 0;
    addTeacherBtn.disabled = hasEditableRow;
    editTeacherBtn.disabled = selected.length !== 1 || hasEditableRow;
    deleteTeacherBtn.disabled = selected.length === 0 || hasEditableRow;

    //Disable "Select All" if no teachers
    selectAllCheckbox.disabled = !hasTeachers;
    if (!hasTeachers) {
        selectAllCheckbox.checked = false;
    }
}

// Add Teacher Button
addTeacherBtn.addEventListener("click", () => {
    const tbody = document.querySelector("#teacherTable tbody");
    const editableRow = createEditableRow();
    tbody.insertBefore(editableRow, tbody.firstChild);
    updateButtonStates();
    message.textContent = "Enter new teacher details";
});

// Edit Teacher Button
editTeacherBtn.addEventListener("click", async () => {
    const selected = getSelectedTeachers();
    if (selected.length !== 1) return;

    try {
        const response = await fetch("http://localhost:3000/teacher");
        const data = await response.json();
        const teacher = data.data.find(t => t.TeacherID === selected[0]);

        if (!teacher) {
            message.textContent = "Teacher not found";
            return;
        }

        const checkbox = document.querySelector(`.teacher-checkbox[value="${selected[0]}"]`);
        const currentRow = checkbox.closest("tr");
        const editableRow = createEditableRow(teacher);

        currentRow.replaceWith(editableRow);
        currentEditRow = editableRow;
        updateButtonStates();
        message.textContent = "Editing Teacher: " + teacher.TeacherID;

    } catch (error) {
        console.error(error);
        message.textContent = "Error loading teacher data";
    }
});

// Delete Selected Button
deleteTeacherBtn.addEventListener("click", async () => {
    const selected = getSelectedTeachers();
    if (selected.length === 0) return;

    const confirmMsg = selected.length === 1
    ? "Are you sure want to delete this teacher?"
    : `Are you sure want to delete ${selected.length} teachrs?`;

    if (!confirm(confirmMsg)) return

    try {
        let response;
        
        if (selected.length === 1) {
            response = await fetch("http://localhost:3000/teacher", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ TeacherID: selected[0] })
            });
        } else {
            response = await fetch("http://localhost:3000/teacher/bulk", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ TeacherIDs: selected })
            });
        }

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message || "Delete failed");
        }

        message.textContent = result.message;
        message.className = "fw-bold text-success";

        setTimeout(() => {
            message.textContent = "";
            message.className = "fw-bold text-danger";
        }, 3000);

        showTeachers();

    } catch (error) {
        console.error(error);
        message.textContent = error.message || "Error deleting teacher(s)";
    }
});

selectAllCheckbox.addEventListener("change", (e) => {
    const checkboxes = document.querySelectorAll(".teacher-checkbox");
    checkboxes.forEach(cb => cb.checked = e.target.checked);
    updateButtonStates();
});

showTeachers();

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

    xhr.upload.onprogress = (e) => { //onprogress is using socket.io in backend
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

    const response = await fetch("http://localhost:3000/download/sample.pdf", {
        headers: {
            Range: `bytes=${downloadedBytes}-`
        },
        signal: controller.signal
    });

    const reader = response.body.getReader();
    const contentLength = +response.headers.get("Content-Length") || +response.headers.get("Content-Range")?.split('/')[1];
    const totalLength = downloadedBytes + contentLength;

    let received = 0;
    const chunks = [];

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        chunks.push(value);
        received += value.length;
        downloadedBytes += value.length;

        downloadProgressBar.value = (downloadedBytes / totalLength) * 100;
    }

    const blob = new Blob(chunks);
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "file";
    a.click();
}

pauseBtn.addEventListener("click", () => {
    if (controller) {
        controller.abort();
        pauseBtn.disabled = true;
        resumeBtn.disabled = false;
    }
});

resumeBtn.addEventListener("click", () => {
    startDownload();
    pauseBtn.disabled = false;
    resumeBtn.disabled = true;
});