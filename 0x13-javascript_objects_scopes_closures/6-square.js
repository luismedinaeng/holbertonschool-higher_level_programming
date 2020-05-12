#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let recPrint = '';
    for (let i = 0; i < this.width; i++) {
      recPrint += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(recPrint);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
module.exports = Rectangle;

const Square1 = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = Square1;

const Square2 = class Square extends Square1 {
  charPrint (c) {
    c = c || 'X';
    let recPrint = '';
    for (let i = 0; i < this.width; i++) {
      recPrint += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(recPrint);
    }
  }
};
module.exports = Square2;
