#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    const character = c || 'X';
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += character;
      }
      console.log(str);
    }
  }
}
module.exports = Square;
