#!/usr/bin/node
const arg = process.argv;
const num1 = parseInt(arg[2]);
const num2 = parseInt(arg[3]);
function add (a, b) {
  console.log(a + b);
}

add(num1, num2);
