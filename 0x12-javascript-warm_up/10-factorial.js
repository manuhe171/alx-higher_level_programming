#!/usr/bin/node
const arg = process.argv;
const num = parseInt(arg[2]);
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(num));
