#!/usr/bin/node
/*
 prints all characters of a Star Wars movie in the right order
 arg1: Movie ID - example: 3 = "Return of the Jedi"
 Example usage: ./101-starwars_characters.js 3
 Refer to Star Wars API: https://swapi-api.alx-tools.com/
*/
const request = require('request');
const address = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const addresses = JSON.parse(body).characters;
    const promises = [];
    for (const chrAdd of addresses) {
      promises.push(
        new Promise(function (resolve, reject) {
          request(chrAdd, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        })
      );
    }
    Promise.all(promises).then((all) => {
      for (const prm of all) {
        console.log(prm);
      }
    });
  }
});
