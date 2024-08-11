#!/usr/bin/node
/*
  a function that converts a number from base 10 to another base passed as argument
  Note: this uses a closure concept
*/
exports.converter = function (base) {
  function convert (n) {
    return n.toString(base);
  }
  return convert;
};
