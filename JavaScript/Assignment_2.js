let number1 = 85;
let number2 = 74;

console.log("Addition of " + number1 + " and "+ number2 + " is: ", number1 + number2)
console.log("Substraction of " + number1 + " and "+ number2 + " is: ", number1 - number2)
console.log("Multiplication of " + number1 + " and "+ number2 + " is: ", number1 * number2)
console.log("Division of " + number1 + " and "+ number2 + " is: ", number1 / number2)

result = number1 / number2;

if (result > 10) {
    console.log("Division is greater than 10");
} else if (result < 10) {
    console.log("Division is less than 10");
} else {
    console.log("Division is exactly 10");
}