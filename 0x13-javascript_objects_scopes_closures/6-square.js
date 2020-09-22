#!/usr/bin/node
/*  Class Square that defines a square and inherits
    from Rectangle of 4-rectangle.js
    charPrint(c): Prints the rectangle using the character c
*/
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
