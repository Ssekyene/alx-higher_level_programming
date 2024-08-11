#!/usr/bin/node
// a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const l in list) {
    if (list[l] === searchElement) {
      count++;
    }
  }
  return count;
};
