#!/usr/bin/node
/*
 prints all characters of a Star Wars movie
 arg1: Movie ID - example: 3 = "Return of the Jedi"
 Example usage: ./100-starwars_characters.js 3
 Refer to Star wars API: https://swapi-api.alx-tools.com/
*/
const request = require('request');
const address = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const addresses = JSON.parse(body).characters;
    for (const chrAdd of addresses) {
      request(chrAdd, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
