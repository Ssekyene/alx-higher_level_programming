#!/usr/bin/node
/*
  displays the status code of a GET request
  arg1: URL to request (GET)
*/
const request = require('request');
const address = process.argv[2];
request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
