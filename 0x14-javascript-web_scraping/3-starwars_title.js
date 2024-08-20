#!/usr/bin/node
/*
 prints the title of a Star Wars movie where the episode number matches a given integer
 arg1: movie ID
 Example usage: ./3-starwars_title.js 1
 Refer to Star Wars API (https://swapi-api.alx-tools.com/) for more details
*/
const request = require('request');
const num = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + num, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
