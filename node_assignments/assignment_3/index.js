class Calculator {
    constructor(num = 0) {
        this.num = num;
    }

    add(val) {
        this.num += val;
        return this;
    }

    subtract(val) {
        this.num -= val;
        return this;
    }

    multiply(val) {
        this.num *= val;
        return this;
    }

    divide(val) {
        this.num /= val;
        return this;
    }

    getResult() {
        return this.num;
    }
}

const calc = new Calculator();
console.log(calc.add(5).subtract(2).multiply(3).divide(2).getResult()); // Output: 4.5


function fetchData() {
    return new Promise((resolve, reject) => {
        const success = true; //can be toggled to see reject part of Promise

        setTimeout(() => {
            if(success) {
                resolve("Data Fetched successfully");
            }else {
                reject("Error: failed to fetch");
            }
        },2000);
    });
}

fetchData()
 .then(message => {
    console.log(message);
 })
 .catch(error => {
    console.error(error);
 });