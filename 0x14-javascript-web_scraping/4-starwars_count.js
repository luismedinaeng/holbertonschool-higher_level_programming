#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let sum = 0;
    films.forEach(function (film) {
      film.characters.forEach(function (charac) {
        if (charac.includes('18')) sum++;
      });
    });
    console.log(sum);
  }
});
