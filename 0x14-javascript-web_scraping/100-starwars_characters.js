#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, function (error, response, body) {
  if (error) console.log(error);
  const film = JSON.parse(body);
  for (const character of film.characters) {
    request(character, function (error, response, body) {
      if (error) console.log(error);
      const characterObj = JSON.parse(body);
      console.log(characterObj.name);
    });
  }
});
