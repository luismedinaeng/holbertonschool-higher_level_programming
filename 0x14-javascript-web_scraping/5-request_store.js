#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv.slice(2)[0];
const file = process.argv.slice(2)[1];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) console.log(error);
    });
  }
});
