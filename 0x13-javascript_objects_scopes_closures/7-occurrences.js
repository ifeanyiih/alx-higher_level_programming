#!/usr/bin/node

function nbOccurences (list, se) {
  let count = 0;
  for (const item of list) {
    if (se === item) count++;
  }
  return (count);
}

module.exports = { nbOccurences };
