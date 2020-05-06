#!/usr/bin/node
const list = process.argv.slice(2).map(Number);
let first; let second = 0;
for (let i = 0; i < list.length; i++) {
  if (i === 0) { first = list[i]; }
  if (list[i] > first) {
    second = first;
    first = list[i];
  } else if (list[i] > second && !(i === 0)) {
    second = list[i];
  }
}
console.log(second);
