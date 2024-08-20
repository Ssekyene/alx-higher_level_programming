#!/usr/bin/node
/*
 reads and prints the content of a file
 arg1: file path
 Example usage: ./0-readme.js cisfun
*/
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
