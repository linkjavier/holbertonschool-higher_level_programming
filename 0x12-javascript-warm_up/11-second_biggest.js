#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments. */

if (process.argv.length > 3) {
  const Mysort = process.argv.sort(function (a, b) { return b - a; });
  console.log(Mysort[3]);
} else {
  console.log(0);
}
