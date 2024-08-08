#!/usr/bin/node
// prints a square using character `X`
const size = parseInt(process.argv[2], 10);
let count = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (; count < size; count++) {
    console.log('X'.repeat(size));
  }
}
