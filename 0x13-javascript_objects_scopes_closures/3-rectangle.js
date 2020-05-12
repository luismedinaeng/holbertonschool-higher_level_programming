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
};
module.exports = Rectangle;
