#!/usr/bin/node
/* Script that prints the addition of 2 integers */

const Mynumber1 = parseInt(process.argv[2]);
const Mynumber2 = parseInt(process.argv[3]);

if (Mynumber1 && Mynumber2) {
    console.log(Mynumber1 + Mynumber2);
  } else {
  console.log('NaN');
}
