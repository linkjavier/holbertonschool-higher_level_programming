#!/usr/bin/node
/* Script that prints the title of a Star Wars movie where
    the episode number matches a given integer.
*/
const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err == null) {
    const json = JSON.parse(body);
    const results = json.results;
    let counter = 0;
    results.forEach(result => {
      const filmsObject = result.characters;
      if (filmsObject.find(element => element === 'https://swapi-api.hbtn.io/api/people/18/')) counter++;
    });
    // FilmsCounter = 0
    // for (i = 0; i < FilmsSize; i++) {
    //   FilmsObject = JSON.parse(body).results[i].characters
    //   if (FilmsObject.find(element => element === 'https://swapi-api.hbtn.io/api/people/18/')) {
    //     FilmsCounter++
    //   }
    // }

    console.log(counter);
  }
});
