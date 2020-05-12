#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let rec_print = '';
    for (let i = 0; i < this.width; i++) {
      rec_print += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rec_print);
    }
  }
};
module.exports = Rectangle;
