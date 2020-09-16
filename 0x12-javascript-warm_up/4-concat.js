#!/usr/bin/node
/* Script that prints two arguments passed to it, in the following format: “ is ” */
let i = 0;
while (process.argv[i]) {
  i++;
}
if (i === 2) {
  console.log('undefined is undefined');
} else if (i === 3) {
  console.log(process.argv[2] + ' is ' + 'undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
