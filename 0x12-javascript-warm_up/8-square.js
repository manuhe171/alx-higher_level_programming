#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let str = '';
    for (let j = 0; j < num; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
