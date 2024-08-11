#!/usr/bin/node
/*
  a function that prints the number of arguments already printed and the new argument value. (see example below)
  0: Hello
  1: Best
  2: School
  note: this uses a closure concept
*/
let num = -1;
exports.logMe = function (item) {
  num++;
  console.log(num + ': ' + item);
};
