#!/usr/bin/node
const value = parseInt(process.argv[2]);

function factorial (a) {
  if (!a || a <= 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(value));
