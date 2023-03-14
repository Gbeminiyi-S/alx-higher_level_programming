#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let symbol = '';
      for (let j = 0; j < this.width; j++) {
        symbol += 'X';
      }
      console.log(symbol);
    }
  }
}

module.exports = Rectangle;
