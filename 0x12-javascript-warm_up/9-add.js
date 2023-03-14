#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const argv = process.argv.slice(2);
const rel = add(parseInt(argv[0]), parseInt(argv[1]));
console.log(rel);
