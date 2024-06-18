#!/usr/bin/node

const i = parseInt(process.argv[2], 10);

function factorial (i) {
  if (isNaN(i) || i === 0) {
    return (1);
  }
  return (i * factorial(i - 1));
}
console.log(factorial(i));
