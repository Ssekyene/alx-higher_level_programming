#!/usr/bin/node
/*
  a class `Square` that defines a square and inherits from Square of 5-square.js with the following instructions:
  You must use the class notation for defining your class and extends
  Create an instance method called charPrint(c) that prints the rectangle using the character c
    If c is undefined, use the character X
*/
const BaseSquare = require('./5-square.js');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
