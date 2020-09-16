#!/usr/bin/node
/* Script that prints x times “C is fun” passed by argv */
let i;
if (process.argv[2] > 0) {
  for (i = process.argv[2]; i > 0; i--) {
    console.log('C is fun');
  }
} else if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
