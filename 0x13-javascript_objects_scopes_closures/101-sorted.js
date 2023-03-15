#!/usr/bin/node

const dict = require('./100-data').dict;
const entries = Object.entries(dict);
const newObj = {};
for (const [key, value] of entries) {
  if (newObj[value] === undefined) newObj[value] = [];
  newObj[value].push(key);
}

console.log(newObj);
