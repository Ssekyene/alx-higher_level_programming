#!/usr/bin/node
/*
  a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence with the following instructions:
  Your script must import dict from the file 101-data.js
  In the new dictionary:
    - A key is a number of occurrences
    - A value is the list of user ids
  Print the new dictionary at the end
*/
const dict = require('./101-data').dict;

const newDic = {};
for (const key in dict) {
  if (newDic[dict[key]] === undefined) {
    newDic[dict[key]] = [];
  }
  newDic[dict[key]].push(key);
}

console.log(newDic);
