#!/usr/bin/node
const size = parseInt(process.argv[2]);
let str = '';
if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    str = str + 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(str);
  }
}
