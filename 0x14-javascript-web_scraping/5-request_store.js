#!/usr/bin/node
/*
 gets the contents of a webpage and stores it in a file
 arg1: URL to request
 arg2: file path to store the body response
 Example usage: ./5-request_store.js http://loripsum.net/api loripsum
*/
const request = require('request');
const address = process.argv[2];
request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) { console.log(err); }
    });
  }
});
