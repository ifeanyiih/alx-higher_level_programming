#!/usr/bin/node

function fac (n) {
  if (n === 0) return 1;
  if (isNaN(n)) return 1;
  return (n * fac(n - 1));
}

const argv = process.argv.slice(2);
const rel = fac(parseInt(argv[0]));
console.log(rel);
