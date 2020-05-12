#!/usr/bin/node
const SquareBase = require('./5-square');

const Square = class Square extends SquareBase {
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
module.exports = Square;
