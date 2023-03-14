#!/usr/bin/node

const txt = 'C is fun';
let count = process.argv.slice(2)[0];
if (count === undefined) console.log('Missing number of occurrences');
else if (count >= 0) {
  while (count) {
    console.log(txt);
    --count;
  }
}
