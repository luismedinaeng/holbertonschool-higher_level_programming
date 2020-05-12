#!/usr/bin/node
const request = require('request');

const filmId = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + filmId + '/';
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(function (charac) {
      request.get(charac, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
