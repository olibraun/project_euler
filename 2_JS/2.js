/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*/

let fibs = [1, 2];

// fill the array
const l = fibs.length;
console.log(l);
let current = fibs[l - 1] + fibs[l - 2];
console.log(current);
while(current <= 4000000) {
//for(let n = 0; n < 1000; n++) {
  fibs.push(current);
  const l = fibs.length;
  current = fibs[l - 1] + fibs[l - 2];
}
let sum = 0;
fibs.forEach(n => {
  if(n % 2 == 0) {
    sum += n;
  }
});
console.log(current);
console.log(fibs.length);
console.log(sum);
//4613732