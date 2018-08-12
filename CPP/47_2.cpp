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

std::vector<int> primeList;

int NumberOfPrimeFactors(int number) {
  int nod = 0;
  bool pf;
  int remain = number;

  for(int i = 0; i < primeList.size(); i++) {
    if(primeList[i] * primeList[i] > number) {
      return ++nod;
    }

    pf = false;
    while(remain % primeList[i] == 0) {
      pf = true;
      remain = remain / primeList[i];
    }
    if(pf) {
      nod++;
    }

    if(remain == 1) {
      return nod;
    }
  }
  return nod;
}

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

int main() {
  // Fill primeList
  for(int i = 1; i <= 1000000; i++) {
    if(isPrime(i)) {
      primeList.push_back(i);
    }
  }
  std::cout << "primeList set up." << std::endl;

  int targetpf = 4;
  int targetConsec = 4;
  int consec = 1;
  int result = 2*3*5*7;

  while(consec < targetConsec) {
    result++;
    if(NumberOfPrimeFactors(result) >= targetpf) {
      consec++;
    } else {
      consec = 0;
    }
  }
  std::cout << result-3 << std::endl;
}