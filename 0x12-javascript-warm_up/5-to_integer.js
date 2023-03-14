#!/usr/bin/node

let argv = process.argv.slice(2);
let num = parseInt(argv[0]);
if (isNaN(num)) console.log('Not a number');
else console.log(`My number: ${num}`);
