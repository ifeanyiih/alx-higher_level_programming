#!/usr/bin/node

const size = parseInt(process.argv.slice(2)[0]);
if (isNaN(size)) console.log('Missing size');
else {
  for (let i = 0; i < size; i++) {
    let txt = '';
    for (let j = 0; j < size; j++) {
      txt += 'X';
    }
    console.log(txt);
  }
}
