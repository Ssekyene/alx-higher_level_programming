#!/usr/bin/node
/*
  a script that concats 2 files:
  The first argument is the file path of the first source file
  The second argument is the file path of the second source file
  The third argument is the file path of the destination
  Usage: ./101.concat.js src1 src2 dest
  Try: `echo "C is fun!" > src1` and `echo "Python is Cool!!!" > src2`
*/
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, textA + textB);
