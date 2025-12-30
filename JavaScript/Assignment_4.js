const generateRandom = function () {
    return Math.floor(Math.random() * 100) + 1;
}

let numberArray = [];

for(let i = 1; i <= 10; i++) {
    numberArray.push(generateRandom());
}

console.log("Our Array: ", numberArray);

//lagerst number
const largestNumber = Math.max(...numberArray);
console.log("Largest number among them is ", largestNumber);

//smallest number
const smallestNumber = Math.min(...numberArray);
console.log("Smallest number among them is ",smallestNumber);

//average
let sum = 0;
for (let num of numberArray) {
    sum += num;
}
const average = sum / numberArray.length;
console.log("Averange of the array is", average);