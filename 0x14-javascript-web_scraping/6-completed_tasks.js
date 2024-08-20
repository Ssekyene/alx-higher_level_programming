#!/usr/bin/node
/*
 computes the number of tasks completed by user id
 arg1: API URL: https://jsonplaceholder.typicode.com/todos
 Example usage: ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
*/
const request = require('request');
const address = process.argv[2];

request(address, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = {};
    const dataObj = JSON.parse(body)
    for (const td of dataObj) {
      if (td.completed) {
        if (results[td.userId] === undefined) { results[td.userId] = 0; }
        results[td.userId] += 1;
      }
    }
    console.log(results);
  }
});
