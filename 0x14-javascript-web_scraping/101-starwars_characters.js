#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, async function (error, response, body) {
  if (error) console.log(error);
  const film = JSON.parse(body);

  function handleCharacter (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  }

  for (const c of film.characters) {
    const name = await handleCharacter(c);
    console.log(name);
  }
});
