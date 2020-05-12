#!/usr/bin/node
const file = process.argv.slice(2)[0];
const data = process.argv.slice(2)[1];
const fs = require('fs');
fs.writeFile(file, data, 'utf8', function (err) {
  if (err) console.log(err);
});
