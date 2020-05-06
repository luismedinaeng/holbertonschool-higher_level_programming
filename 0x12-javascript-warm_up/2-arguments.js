#!/usr/bin/node
const len = process.argv.length - 2;
let message;
if (len === 0) {
  message = 'No argument';
} else if (len === 1) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}
console.log(message);
