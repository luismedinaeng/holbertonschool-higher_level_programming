#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let s = 0;
  list.forEach(function (element) {
    if (element === searchElement) {
      s++;
    }
  });
  return s;
};
