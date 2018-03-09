/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

function isPrime(n) {
  const wn = Math.sqrt(n);
  for(let i = 2; i <= wn; i++) {
    if(n % i == 0) {
      return false;
      break;
    }
  }
  return true;
}

function smallestPrimeDivisor(n) {
  let current = 2;
  while(true) {
    if(isPrime(current) && n % current == 0) {
      return current;
    }
    current++;
  }
}

function primeFactors(n) {
  if(isPrime(n)) {
    return [n];
  } else {
    const p = smallestPrimeDivisor(n);
    return  [p].concat(primeFactors(n/p));
  }
}

const factors = primeFactors(600851475143);

console.log(Math.max(...factors));
//6857