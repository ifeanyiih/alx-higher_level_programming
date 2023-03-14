#!/usr/bin/node

let argv = process.argv.slice(2);
argv = argv.map(n => parseInt(n));
argv.sort((a,b) => a - b);
if (argv.length === 0 || argv.length === 1) console.log(0);
else console.log(argv[argv.length - 2]);
