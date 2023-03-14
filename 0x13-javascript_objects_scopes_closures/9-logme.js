#!/usr/bin/node

let logCount = 0;

function logMe (item) {
  console.log(`${logCount}: ${item}`);
  ++logCount;
}

module.exports = { logMe };
