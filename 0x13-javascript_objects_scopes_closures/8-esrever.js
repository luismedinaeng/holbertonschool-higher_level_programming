#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  while (list.length > 0) {
    tsil.push(list.pop());
  }
  return tsil;
};
