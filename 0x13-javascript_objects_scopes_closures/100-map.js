#!/usr/bin/node

const list = require('./100-data');
const mapList = list.map((n, i) => n * i);
console.log(list);
console.log(mapList);
