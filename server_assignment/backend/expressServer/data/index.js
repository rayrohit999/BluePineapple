import fs from "fs/promises";

export async function readFromCSV(path) {
    try {
        const data = await fs.readFile(path, "utf-8");

        const lines = data.trim().split("\n");
        const headers = lines[0].split(",");

        return lines.slice(1).map(line => {
            const values = line.split(",");
            let obj = {};

            headers.forEach((header, index) => {
                obj[header.trim()] = values[index]?.trim();
            });

            return obj;
        });
    } catch (error) {
        console.error("Error reading CSV:", error);
        return [];
    }
}

export async function writeToCSV(data, path) {
    if (!Array.isArray(data)) {
        throw new Error("Data must be an array of objects");
    }

    const existingData = await readFromCSV(path);
    const updatedData = [...existingData, ...data];

    await saveCSV(updatedData, path);
}

export async function editCSV(newData, path) {
    const records = await readFromCSV(path);

    const updatedRecords = records.map(record =>
        record.TeacherID === newData.TeacherID
            ? { ...record, ...newData }
            : record
    );

    await saveCSV(updatedRecords, path);
}
export async function deleteFromCSV(id, path) {
    const records = await readFromCSV(path);

    const filteredRecords = records.filter(
        record => record.TeacherID !== id
    );

    await saveCSV(filteredRecords, path);
}
async function saveCSV(data, path) {
    if (data.length === 0) {
        throw new Error("No data to save");
    }

    const headers = Object.keys(data[0]).join(",");
    const rows = data.map(obj =>
        Object.values(obj).join(",")
    );

    const csvContent = [headers, ...rows].join("\n");

    await fs.writeFile(path, csvContent, "utf-8");
}
