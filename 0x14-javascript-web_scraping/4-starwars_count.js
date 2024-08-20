#!/usr/bin/node
/*
  prints the number of movies where the character “Wedge Antilles” is present
  Wedge Antilles is character ID 18
  arg1: API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
  Example usage: ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
  Refer to https://swapi-api.alx-tools.com for more Star wars API details
*/
const request = require('request');
const address = process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      for (const chr of results[i].characters) {
        if (chr.search('/18/') > 0) { count += 1; }
      }
    }
    console.log(count);
  }
});
