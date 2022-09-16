#!/usr/bin/node
const arg = process.argv;
if (arg.length === 2 || arg.length === 3) {
  console.log(0);
} else {
  const args = arg.slice(2);
  const newArr = [];
  const max = Math.max(...args);
  let secondLargest;
  for (const i in args) {
    newArr.push(max - args[i]);
    for (const j in newArr) {
      if (newArr[j] === 0) {
        newArr[j] = max;
      }
      const min = Math.min(...newArr);
      if (newArr[j] === min) {
        const secondIndex = j;
        secondLargest = args[secondIndex];
      }
    }
  }
  console.log(secondLargest);
}
