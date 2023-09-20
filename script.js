
//var example
function example_var() {
  var x = 10;
  if (true) {
    var y = 20;
  }
  console.log(x); // 10
  console.log(y); // 20
}

//let example
function example_let() {
  let x = 10;
  if (true) {
    let y = 20;
  }
  console.log(x); // 10
  console.log(y); // ReferenceError: y is not defined
}

//const example
function example_const() {
  const x = 10;
  if (true) {
    const y = 20;
  }
  console.log(x); // 10
  console.log(y); // ReferenceError: y is not defined
}

// If trying to change a const value:
const z = 5;
z = 7; // TypeError: Assignment to constant variable



//hoisting function example
hoistedFunction(); // Output: "Hello, world!"

function hoistedFunction() {
  console.log("Hello, world!");
}