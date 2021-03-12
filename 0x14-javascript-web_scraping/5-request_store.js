#!/usr/bin/node
/* Script that prints the title of a Star Wars movie where
    the episode number matches a given integer.
*/
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');

request.get(url, function (err, response, body) {
  if (err == null) {
    fs.writeFile(fileName, body, 'utf8', function (err) {
      if (err) throw err;
    });
  }
});
