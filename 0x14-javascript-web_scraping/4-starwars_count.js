#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  const numFilms = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
  console.log(`${numFilms}`);
});
