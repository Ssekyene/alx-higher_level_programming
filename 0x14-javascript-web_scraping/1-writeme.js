#!/usr/bin/node
/* writes a string to a file
   arg1: file path
   arg2: string to write
*/
const file = process.argv[2];
const string = process.argv[3];
const fs = require('fs');
fs.writeFile(file, string, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
