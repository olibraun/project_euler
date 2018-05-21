/*
Find the difference between the sum of the squares 
of the first one hundred natural numbers and the 
square of the sum.
*/

function sumUpTo(n) {
  // Gauß
  return n*(n+1)/2;
}

function sumOfSquares(n) {
  // Gauß as well?
  return n*(n+1)*(2*n+1)/6;
}

const sum = sumUpTo(100);
const SOS = sumOfSquares(100);
const final = sum*sum - SOS;
console.log(final);
// ​​​​​25164150​​​​​