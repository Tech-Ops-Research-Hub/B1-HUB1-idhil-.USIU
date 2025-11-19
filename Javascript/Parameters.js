Define parameters and arguments and explain the difference.
parameters are the placeholders for values that will be passed when the function is called while arguments are the actual values being passed when function is called 



What happens when a function does not include a return statement?
it returns undefined 

Write a function with default and rest parameters to calculate average scores.
function calculateAverage({ subject = "Unknown", scores = [] } = {}) {
  if (scores.length === 0) {
    return { subject, average: 0, message: `No scores provided for ${subject}.` };
  }

  const total = scores.reduce((sum, score) => sum + score, 0);
  const average = total / scores.length;

  return { subject, average };
}

// Example object
const studentRecord = {
  subject: "Math",
  scores: [80, 90, 70, 100]
};


const { subject, average } = calculateAverage(studentRecord);
console.log(`${subject} average: ${average.toFixed(2)}`); // Math average: 85.00



How can multiple values be returned from one function? Show both array and object methods.
//using arrays
function getScores() {
  return [85, 90, 78]; 
}

const [math, science, english] = getScores();
console.log(math, science, english); // 85 90 78

//using objects
function getStudentInfo() {
  return { name: "Alice", grade: "A", age: 17 };
}

const { name, grade, age } = getStudentInfo();
console.log(name, grade, age); // Alice A 17



Explain why mutating parameters inside functions is discouraged.
it changes data outside the function causing bugs which are hard to track

Implement a function calculateBMI(weight, height) that returns both BMI value and category.
function calculateBMI(weight, height) {
  const bmi = weight / (height * height);

  let category;
  if (bmi < 18.5) {
    category = "Underweight";
  } else if (bmi < 25) {
    category = "Normal weight";
  } else if (bmi < 30) {
    category = "Overweight";
  } else {
    category = "Obesity";
  }

  return { bmi: bmi.toFixed(2), category };
}

// Example
const result = calculateBMI(70, 1.75);
console.log(result);

How does destructuring in parameters simplify function usage? Provide an example.
destructing allows you to unpack values directly from arrays or objects right inside the function parameters

What is the purpose of default parameters in function definitions?
they are used when no arguments are provided 

Demonstrate control flow using return in conditional branches.
function checkNumber(num) {
  if (num > 0) {
    return "Positive number";
  } else if (num < 0) {
    return "Negative number";
  } else {
    return "Zero";
  }
}

console.log(checkNumber(5));   // Positive number
console.log(checkNumber(-3));  // Negative number
console.log(checkNumber(0));   // Zero


Comment your code using JSDoc to describe parameters and return values for a simple function.
/**
 * Calculates the area of a rectangle.
 *
 * @param {number} length - The length of the rectangle.
 * @param {number} width - The width of the rectangle.
 * @returns {number} The area of the rectangle.
 */
function calculateArea(length, width) {
  return length * width;
}


console.log(calculateArea(5, 3)); // Output: 15
