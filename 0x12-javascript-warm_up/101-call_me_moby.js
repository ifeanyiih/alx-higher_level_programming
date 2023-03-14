#!/usr/bin/node

function callMeMoby (count, func) {
  while (count) {
    func();
    --count;
  }
}

module.exports = { callMeMoby };
