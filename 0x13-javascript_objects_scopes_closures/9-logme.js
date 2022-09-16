#!/usr/bin/node
let print = 0;
exports.logMe = function (item) {
  console.log(`${print}: ${item}`);
  print++;
};
