/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

let found = false;
let current = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19;
while(!found) {
  if(current % 5 == 0
  && current % 7 == 0
  && current % 9 == 0
  && current % 11 == 0
  && current % 13 == 0
  && current % 16 == 0
  && current % 17 == 0
  && current % 19 == 0) {
    found = true;
  }
  current++;
}
console.log(current - 1);
// 232792560