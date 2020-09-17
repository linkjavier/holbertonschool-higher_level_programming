#!/usr/bin/node
/* Script that prints x square passed by argv */
let i;
const number = parseInt(process.argv[2]);
if (number) {
  for (i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
