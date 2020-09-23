#!/usr/bin/node
/* Script that writes a string to a file. */
const fs = require('fs');
const fileName = process.argv[2];
const data = process.argv[3];

fs.writeFile(fileName, data, (err) => {
  if (err) {
    console.log(err);
  }
});
