#include<iostream>

int elt1 = 1;
int elt2 = 2;
int temp, current;
int res = 2;

int main() {
  current = elt1 + elt2;

  while(current < 4000000) {
    if(current % 2 == 0) {
      res += current;
    }
    temp = elt2;
    elt2 = current;
    elt1 = temp;
    current = elt1 + elt2;
  }

  std::cout << res << "\n";

  return 0;
}