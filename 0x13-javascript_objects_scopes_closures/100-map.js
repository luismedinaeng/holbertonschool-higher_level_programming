#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
console.log(list.map(function (x) {
  return list.indexOf(x) * x;
}));
