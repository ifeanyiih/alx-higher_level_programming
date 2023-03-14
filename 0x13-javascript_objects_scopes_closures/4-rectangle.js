#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0) return;
    if (h <= 0) return;
    if (w === undefined || h === undefined) return;
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let text = '';
      for (let j = 0; j < this.width; j++) {
        text += 'X';
      }
      console.log(text);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    let temp = this.width * 2;
    this.width = temp;
    temp = this.height * 2;
    this.height = temp;
  }
}

module.exports = Rectangle;
