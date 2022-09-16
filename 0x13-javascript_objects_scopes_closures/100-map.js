#!/usr/bin/node
const list = require('./100-data').list;
const newArr = list.map((elem, index) => elem * index);
console.log(list);
console.log(newArr);
