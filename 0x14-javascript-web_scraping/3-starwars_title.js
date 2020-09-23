#!/usr/bin/node
/* Script that prints the title of a Star Wars movie where
    the episode number matches a given integer.
*/
const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${id}`, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
