#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

const Square = class extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = Square;
