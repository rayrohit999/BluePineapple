import fs from "fs/promises";
import { createObjectCsvWriter } from 'csv-writer';

export async function readFromCSV(path) {
    try {
        const data = await fs.readFile(path, "utf-8");
        const lines = data.trim().split("\n");
        
        if (lines.length === 0 || lines[0].trim() === "") {
            return [];
        }
        
        const headers = lines[0].split(",");

        return lines.slice(1).map(line => {
            const values = line.split(",");
            let obj = {};

            headers.forEach((header, index) => {
                obj[header.trim()] = values[index]?.trim() || "";
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

export async function deleteFromCSV(teacherID, filePath) {
    try {
        // Read existing data
        const data = await readFromCSV(filePath);
        
        // Filter out the teacher to delete
        const filteredData = data.filter(teacher => teacher.TeacherID !== teacherID);
        
        // Use saveCSV instead to maintain consistency
        await saveCSV(filteredData, filePath);
        
        return true;
    } catch (error) {
        console.error('Error in deleteFromCSV:', error);
        throw error;
    }
}

async function saveCSV(data, path) {
    // Allow saving empty data - just write headers
    const headers = ["TeacherID", "Name", "Subject", "Phone"];
    
    if (data.length === 0) {
        // Write just the headers when no data
        await fs.writeFile(path, headers.join(",") + "\n", "utf-8");
        return;
    }

    const rows = data.map(obj =>
        headers.map(header => obj[header] || "").join(",")
    );

    const csvContent = [headers.join(","), ...rows].join("\n");

    await fs.writeFile(path, csvContent, "utf-8");
}

// readFromCSV("D:/Bluepineapple/server_assignment/backend/expressServer/data/teachers.csv");