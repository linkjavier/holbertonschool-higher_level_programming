#!/usr/bin/node
/* Script that converts the first argument to integer */
const mynumber = parseInt(process.argv[2]);
if (mynumber) {
  console.log('My number: ' + mynumber);
} else {
  console.log('Not a number');
}
