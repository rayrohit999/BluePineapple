function calculateArea(length, width) {
    if (length < 0 || width < 0) {
        return undefined
    }
    return length * width;
}

console.log("Length: 5 Width: 2 Area:", calculateArea(5,2));
console.log("Length: 15 Width: 2 Area:", calculateArea(15,2));
console.log("Length: 5 Width: 0 Area:", calculateArea(5,0));
console.log("Length: 0 Width: 2 Area:", calculateArea(0,2));
console.log("Length: -5 Width: 2 Area:", calculateArea(-5,2));