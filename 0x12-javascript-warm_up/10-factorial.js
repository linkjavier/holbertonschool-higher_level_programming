#!/usr/bin/node
/* Script that computes and prints a factorial */

function factorialRecursivo (n) {
  if (!n) {
    return 1;
  }
  return n * factorialRecursivo(n - 1);
}
console.log(factorialRecursivo(parseInt(process.argv[2])));
