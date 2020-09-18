#!/usr/bin/node
/* Script that computes and prints a factorial */
let i;
let total = 1;
const n = parseInt(process.argv[2]);
if (n) {
  for (i = 1; i <= n; i++) {
    total = total * i;
  }
  console.log(total);
} else {
  console.log(1);
}
