#include<iostream>
#include<cmath>
#include<vector>
/*
std::vector<int> arr <- initializes "arr" as a vector of ints
std::vector::at() <- returns value
faster: for (int i = 0; i < v.size(); i++) {arr[i]}
*/
#include<map>

/*
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 * 7
15 = 3 * 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
*/

bool isPrime(int n) {
  if(n < 0) {
    n *= -1;
  }

  if(n == 0 || n == 1) {
    return false;
  }

  if(n == 2) {
    return true;
  }

  int rn = std::ceil(std::sqrt(n));
  for(int x = 2; x <= rn; x++) {
    if(n % x == 0) {
      return false;
    }
  }

  return true;
}

int smallestPrimeFactor(int n) {
  for(int x=2; x <= n; x++) {
    if(isPrime(x) && n % x == 0) {
      return x;
      break;
    }
  }
}

std::map<int, int> number_of_factors;

int number_of_prime_factors (int n, std::map<int, int> &map) {
  int original_n = n;
  auto it = map.find(n);
  if(it != map.end()) {
    return map[n];
  } else {
    if(n <= 1) {
      return 0;
    }
    int p = smallestPrimeFactor(n);
    while(n % p == 0) {
      n = n/p;
    }
    int nf = number_of_prime_factors(n, map);
    map[original_n] = 1 + nf;
    return 1 + nf;
  }
}

int main() {
  int i = 2*3*5*7;
  bool done = false;
  while(!done) {
    if(i % 25000 == 0) {
      std::cout << i << " checked." << std::endl;
    }

    int i1 = i + 1;
    int i2 = i + 2;
    int i3 = i + 3;
    int ni = number_of_prime_factors(i, number_of_factors);
    int ni1 = number_of_prime_factors(i1, number_of_factors);
    int ni2 = number_of_prime_factors(i2, number_of_factors);
    int ni3 = number_of_prime_factors(i3, number_of_factors);
    if(ni == 4 && ni1 == 4 && ni2 == 4 && ni3 == 4) {
      done = true;
      std::cout << i << std::endl;
    }
    i++;
  }
  return 0;
}