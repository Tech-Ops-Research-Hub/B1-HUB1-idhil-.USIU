//Convert to arrow:
//function add(a, b) { return a + b }
const add = (a,b) => a + b;


//Convert to one-line implicit return:
//const square = (x) => { return x * x }
const square = x => x * x;


//Fix object return:
//const makeItem = () => { id: 1 }
const makeItem = () => ({ id: 1 });

//replace arguments
//const sum = () => arguments[0] + arguments[1]
const sum = (...args) => {
    return args[0] + args[1];
}

//explain this
const obj = { val: 20, getVal: () => this.val }
//The arrow function does not have its own 'this', so 'this.val' refers to the surrounding context, 
// which may not have 'val' defined.


//Write incrementAll(arr) → return a new array where each number is increased by 1 using map
const arr = [1, 2, 3, 4];
const incrementAll = arr.map(x => x + 1);
console.log(incrementAll); // [2, 3, 4, 5]


//Write filterEven(arr) → return only even numbers using filter.
const array = [1, -2, 3, 10,15, -6];
const filterEven = arr.filter(x => x % 2 === 0);
console.log(filterEven); // [-2, 10, -6]


//Write sumArray(arr) → return the total using reduce.
const numbers = [10,20,30,40];
const sumArray = arr.reduce((total, x) => total + x, 0);
console.log(sumArray); // 100

//Create an object with a method that uses this correctly (no arrow function in the method). markdown
const user ={
    name: 'idhil',
    getName() {
        return this.name;
    }
};
    console.log(user.getName()); // idhil

