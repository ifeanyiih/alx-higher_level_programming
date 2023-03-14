#!/usr/bin/node

function callMeMoby (count, func) {
  while (count > 0) {
    func();
    --count;
  }
}

module.exports = { callMeMoby };
