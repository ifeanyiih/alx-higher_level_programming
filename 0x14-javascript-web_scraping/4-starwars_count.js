#!/usr/bin/node

const request = require('request');

const id = '18';

request('https://swapi-api.alx-tools.com/api/films', function (error, response, body) {
  if (error) console.log(error);
  body = JSON.parse(body);
  const films = body.results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes(id)) count += 1;
    }
  }
  console.log(count);
});
