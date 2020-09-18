#!/usr/bin/node
/*  Script that prints the addition of 2 integers
    The function must be visible from outside
*/

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
