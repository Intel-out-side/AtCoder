#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll deposit = 100;
  ll X;
  cin >> X;

  ll n = 0;
  while (true) {
    deposit = deposit * 1.01;
    n++;
    if (deposit >= X) break;
  }

  cout << n << endl;
  return 0;
}
