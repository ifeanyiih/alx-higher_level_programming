#!/usr/bin/node

const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 0; i < this.height; i++) {
      let text = '';
      for (let j = 0; j < this.width; j++) {
        text += c;
      }
      console.log(text);
    }
  }
}

module.exports = Square;
