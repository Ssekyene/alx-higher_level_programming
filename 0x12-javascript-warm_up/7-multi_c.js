#!/usr/bin/node
// prints `x` times “C is fun”
const x = parseInt(process.argv[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let count = 0; x > count; count++) {
    console.log('C is fun');
  }
}
